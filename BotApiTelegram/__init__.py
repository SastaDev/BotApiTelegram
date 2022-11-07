# Bot-Api-Telegram || started on 9 October, 2022 at 08:04:55 PM (IST).

import requests
from . import exceptions, types, methods, conversation as conv, database, filters as Filters, bot
import functools
import signal
import json
import time
import sys
import os
import re

requests_session = requests.Session() # To make requests faster.

class TelegramBot(bot.Bot):
    def __init__(self, database_path=None, bot_token=None):
        self.bot = self # TelegramBot class.
        self.bot_token = bot_token
        self.bot_url = 'https://api.telegram.org/bot{}'
        if bot_token:
            self.bot_url.format(bot_token)
        self.is_authorized = None
        self.GetUpdates = None
        if bot_token:
            v = self.is_valid_bot_token(bot_token)
            if v is True:
                self.is_authorized = True
            else:
                self.is_authorized = False
                raise exceptions.UnAuthorizedBotToken(bot_token)
        self.conversations = []
        self.on_update_filters = []
        self.COMMAND_STARTS_WITH = ['/']
        self.parse_mode = 'markdown'
        self.bot_db = database.BotDB(self.bot, database_path)
        if database_path:
            x = self.bot_db.dat_file()
            if x.get('bot_token'):
                self.bot_token = x.get('bot_token')
                self.bot_url = self.bot_url.format(self.bot_token)
        self.default_settings = types.DefaultSettings()

    def is_valid_bot_token(self, bot_token):
        if bot_token:
            r = requests_session.get('https://api.telegram.org/bot{}'.format(bot_token) + '/getMe')
        else:
            r = requests_session.get(self.bot_url + '/getMe')
        if r.status_code != 200:
            return False
        else:
            return True

    def get_updates(self, limit=100, timeout=60, allowed_updates=[], skip_pending_updates=False):
        skipped = None
        ignored = None
        offset = 1
        if not allowed_updates:
            allowed_updates = types.allowed_updates_all_types # along with chat_member.
        if skip_pending_updates is True:
            skipped = False
            ignored = False
        while self.GetUpdates is True:
            d = {
                'offset': offset,
                'limit': limit,
                'timeout': timeout,
                'allowed_updates': json.dumps(allowed_updates)
            }
            retry = 0
            while skipped is False:
                try:
                    e = d
                    e['offset'] = -1
                    r = requests_session.get(self.bot_url + '/getUpdates', params=e)
                    skiped_updates = r.json().get('result')
                    skipped = True
                except requests.exceptions.ConnectionError:
                    retry += 1
                    print('Connection Error: Sleeping for 5 seconds and then Retrying for {} time.'.format(retry))
                    time.sleep(5)
            x = True
            while x is True:
                try:
                    r = requests_session.get(self.bot_url + '/getUpdates', params=d)
                    x = False
                except requests.exceptions.ConnectionError:
                    retry += 1
                    print('Connection Error: Sleeping for 5 seconds and then Retrying for {} time.'.format(retry))
                    time.sleep(5)
            if ignored is False:
                ignored = True
                offset = skiped_updates[0]['update_id'] + 1
                continue
            if r.status_code != 200:
                url = r.url
                raise self.check(r.json(), url)
            else:
                result = r.json().get('result')
                if result:
                    update = types.Updates(result[0])
                    self.send_update(update=update)
                    offset = update.update_id + 1

    def send_update(self, update):
        for c in self.conversations:
            c.append_update(update.message)
        for f in self.on_update_filters:
            if update.message:
                chat = getattr(update.message, 'chat', None)
                if chat:
                    if isinstance(f, Filters.chat):
                        if f.chat:
                            if chat.id in f.chat:
                                f.function(types.Message_(bot=self.bot, msg=update.message))
                        else:
                            f.function(types.Message_(bot=self.bot, msg=update.message))
                user = getattr(update.message, 'user', None)
                if user:
                    if isinstance(f, Filter.user):
                        if user.id in Filters.user:
                            f.function(types.Message_(bot=self.bot, msg=update.message))
                text = getattr(update.message, 'text', None)
                if text:
                    if isinstance(f, Filters.text):
                        if text in f.text:
                            f.function(types.Message_(bot=self.bot, msg=update.message))
                    if isinstance(f, Filters.command):
                        splited_text = text.split()
                        cmd_starts_with = splited_text[0][0]
                        cmd = splited_text[0][1:]
                        if cmd_starts_with in self.COMMAND_STARTS_WITH or cmd_starts_with in f.starts_with:
                            if cmd in f.command:
                                f.function(types.Message_(bot=self.bot, msg=update.message))
                    if isinstance(f, Filters.regex):
                        compiles = [re.compile(x) for x in f.regex]
                        matches = [c.match(text) for c in compiles]
                        for m in matches:
                            if m:
                                update.message.regex_string = m.string
                                update.message.pattern_match = m
                                f.function(types.Message_(bot=self.bot, msg=update.message))
                animation = getattr(update.message, 'animation', None)
                if animation:
                    if isinstance(f, Filters.animation):
                        execution = True
                        if f.only_mime_type:
                            if animation.mine_type in f.only_mime_type:
                                execution = True
                            else:
                                execution = False
                        if execution is True:
                            del execution
                            f.function(types.Message_(bot=self.bot, msg=update.message))
                audio = getattr(update.message, 'audio', None)
                if audio:
                    if isinstance(f, Filters.audio):
                        execution = True
                        if f.only_mime_type:
                            if audio.mine_type in f.only_mime_type:
                                execution = True
                            else:
                                execution = False
                        if execution is True:
                            del execution
                            f.function(types.Message_(bot=self.bot, msg=update.message))
                document = getattr(update.message, 'document', None)
                if document:
                    if isinstance(f, Filters.document):
                        execution = True
                        if f.only_mime_type:
                            if document.mine_type in f.only_mime_type:
                                execution = True
                            else:
                                execution = False
                        if execution is True:
                            del execution
                            f.function(types.Message_(bot=self.bot, msg=update.message))
                photo = getattr(update.message, 'photo', None)
                if photo:
                    if isinstance(f, Filters.photo):
                        f.function(types.Message_(bot=self.bot, msg=update.message))
                sticker = getattr(update.message, 'sticker', None)
                if sticker:
                    if isinstance(f, Filters.sticker):
                        execution = True
                        if f.only_type:
                            if sticker.type in f.only_type:
                                execution = True
                            else:
                                execution = False
                        if f.only_animated:
                            if sticker.is_animated == f.only_animated:
                                execution = True
                        if f.only_video:
                            if sticker.is_video == f.only_video:
                                execution = True
                            else:
                                execution = False
                        if f.only_premium_animation:
                            if getattr(sticker, 'premium_animation', None) and f.only_premium_animation is True:
                                execution = True
                            else:
                                execution = False
                        if f.only_custom_emoji:
                            if getattr(sticker, 'custom_emoji_id', None) and f.only_custom_emoji is True:
                                execution = True
                            else:
                                execution = False
                        if execution is True:
                            del execution
                            f.function(types.Message_(bot=self.bot, msg=update.message))
                video = getattr(update.message, 'video', None)
                if video:
                    if isinstance(f, Filters.video):
                        execution = True
                        if f.only_mime_type:
                            if video.mine_type in f.only_mime_type:
                                execution = True
                            else:
                                execution = False
                        if execution is True:
                            del execution
                            f.function(types.Message_(bot=self.bot, msg=update.message))
                video_note = getattr(update.message, 'video_note', None)
                if video_note:
                    if isinstance(f, Filters.video_note):
                        f.function(types.Message_(bot=self.bot, msg=msg))
                voice = getattr(update.message, 'voice', None)
                if voice:
                    if isinstance(f, Filters.voice):
                        execution = True
                        if f.only_mime_type:
                            if voice.mime_type in f.only_mime_type:
                                execution = True
                            else:
                                execution = False
                        if execution is True:
                            del execution
                            f.function(types.Message_(bot=self.bot, msg=update.message))
                contact = getattr(update.message, 'contact', None)
                if contact:
                    if isinstance(f, Filters.contact):
                        execution = True
                        if f.only_phone_number:
                            if contact.phone_number == f.only_phone_number:
                                execution = True
                            else:
                                execution = False
                        if f.users:
                            if contact.user_id in f.users:
                                execution = True
                            else:
                                execution = False
                        if f.only_vcard:
                            if contact.vcard:
                                execution = True
                            else:
                                execution = False
                        if execution is True:
                            del execution
                            f.function(types.Message_(bot=self.bot, msg=update.message))
                dice = getattr(update.message, 'dice', None)
                if dice:
                    if isinstance(f, Filters.dice):
                        f.function(types.Message_(bot=self.bot, msg=update.message))
                game = getattr(update.message, 'game', None)
                if game:
                    if isinstance(f, Filters.game):
                        f.function(types.Message_(bot=self.bot, msg=update.message))
                poll = getattr(update.message, 'poll', None)
                if poll:
                    if isinstance(f, Filters.poll):
                        execution = True
                        if f.only_closed:
                            if poll.is_closed is True:
                                execution = True
                            else:
                                execution= False
                        if f.only_anonymous:
                            if poll.is_anonymous is True:
                                execution = True
                            else:
                                execution = False
                        if f.poll_type:
                            if poll.type in f.poll_type:
                                execution = True
                            else:
                                execution = False
                        if execution is True:
                            del execution
                            f.function(types.Message_(bot=self.bot, msg=update.message))
                venue = getattr(update.message, 'venue', None)
                if venue:
                    if isinstance(f, Filters.venue):
                        f.function(types.Message_(bot=self.bot, msg=update.message))
                location = getattr(update.message, 'location', None)
                if location:
                    if isinstance(f, Filters.location):
                        f.function(types.Message_(bot=self.bot, msg=update.message))
                pinned_message = getattr(update.message, 'pinned_message', None)
                if pinned_message:
                    if isinstance(f, Filters.pinned_message):
                        f.function(types.Message_(bot=self.bot, msg=update.message))
                invoice = getattr(update.message, 'invoice', None)
                if invoice:
                    if isinstance(f, Filters.invoice):
                        f.function(types.Message_(bot=self.bot, msg=update.message))
            if update.callback_query:
                data = getattr(update.callback_query, 'data', None)
                if data:
                    if isinstance(f, Filters.regex):
                        compiles = [re.compile(x) for x in f.regex]
                        matches = [c.match(data) for c in compiles]
                        for m in matches:
                            if m:
                                update.callback_query.pattern_match = m
                                f.function(types.CallbackQuery_(bot=self.bot, callback_query=update.callback_query))
                    elif isinstance(f, Filters.CallbackQuery):
                        if data in f.data:
                            f.function(types.CallbackQuery_(bot=self.bot, callback_query=update.callback_query))
            if update.chat_member:
                chat_member = update.chat_member
                old_member = chat_member.old_chat_member
                new_member = chat_member.new_chat_member
                if isinstance(f, Filters.chat):
                    if True in f.chat or None in f.chat or chat_member.chat.id in f.chat:
                        # Chat Joined.
                        if True in f.joined or new_member.user.id in f.joined:
                            if old_member.status == 'left' and chat_member.from_user.id == new_member.user.id:
                                f.function(types.Message_(bot=self.bot, msg=types.ChatJoined(update.chat_member)))
                        # Chat Left.
                        if True in f.left or new_member.user.id in f.left:
                            if new_member.status == 'left':
                                f.function(types.Message_(bot=self.bot, msg=types.ChatLeft(update.chat_member)))
                        # Chat Added.
                        if True in f.added or new_member.user.id in f.added:
                            if chat_member.from_user.id != new_member.user.id:
                                f.function(types.Message_(bot=self.bot, msg=types.ChatAdded(update.chat_member)))

    def check(self, data, url):
        des = data['description']
        m = methods.parse_url(url)
        if des == 'Bad Request: chat not found':
            raise exceptions.ChatNotFound()
        elif des == 'Bad Request: message text is empty':
            raise exceptions.MessageTextIsEmpty()
        elif des == 'Bad Request: field "inline_keyboard" of the InlineKeyboardMarkup must be an Array of Arrays':
            raise exceptions.InvalidKeyboardMarkup(array_of_array=True)
        elif des == 'Bad Request: there are no administrators in the private chat':
            raise exceptions.NoAdministratorsInPrivateChat()
        elif des == 'Forbidden: bot was blocked by the user':
            raise exceptions.UserBlockedBot()
        elif des == 'Bad Request: unsupported parse_mode':
            raise exceptions.UnSupportedParseMode()
        elif des == 'Bad Request: query is too old and response timeout expired or query ID is invalid':
            raise exceptions.QueryError()
        else:
            raise exceptions.UnKnownError(des)

    def on_update(self, Filter, func=None):
        @functools.wraps(func)
        def _on(func, Filter=Filter):
            Filter.function = func
            self.on_update_filters.append(Filter)
        return _on

    def start_polling(self, limit=100, timeout=60, allowed_updates=[], skip_pending_updates=False):
        if self.bot_token is None:
            while True:
                b = input('Enter your bot token: ')
                if self.is_valid_bot_token(b) is False:
                    print('Invalid bot token, please try again!')
                else:
                    self.bot_token = b
                    self.bot_url = self.bot_url.format(b)
                    self.bot_db.save(bot_token=b)
                    print('Started polling!')
                    break
        self.GetUpdates = True
        self.get_updates(limit=limit, timeout=timeout, allowed_updates=allowed_updates, skip_pending_updates=skip_pending_updates)

    def log_out(self):
        url = self.bot_url + '/logOut'
        r = requests_session.get(url)
        if r.status_code != 200:
            bot.check(r.json(), url)
        else:
            return r.json().get('result')

    def close(self):
        url = self.bot_url + '/close'
        r = requests_session.get(url)
        if r.status_code != 200:
            bot.check(r.json(), url)
        else:
            return r.json().get('result')

    def conversation(self, chat_id, global_timeout):
        if isinstance(chat_id, types.Chat):
            _chat_id = chat_id.id
        elif isinstance(chat_id, types.User):
            _chat_id = chat_id.user_id
        elif isinstance(chat_id, types.Message):
            _chat_id = chat_id.chat.id
        else:
            _chat_id = chat_id
        c = conv.Conversation(bot=self.bot, chat_id=_chat_id, global_timeout=global_timeout)
        self.conversations.append(c)
        return c

def signal_handler(signal, frame):
    print('[Bot Api Telegram]: Quiting...')
    sys.exit(0)

signal.signal(signal.SIGINT, signal_handler)

__version__ = '0.0.7'
__author__ = 'Author: Sasta Dev.'
__credits__ = '''
<-----credits----->
1. Sasta Dev (Author/Dev).
'''
__copyright__ = '(c) Sasta Dev.'
__docs__ = '''
Documentation Link: https://BotApiTelegram.tk.
Telegram Updates Channel: @BotApiTelegram.
Telegram Help Support Chat: @BotApiTelegramChat.
'''