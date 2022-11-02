# Bot-Api-Telegram || started on 9 October, 2022 at 08:04:55 PM (IST).

import requests
from . import exceptions, types, methods, conversation as conv, database, filters as Filters
import functools
import signal
import json
import time
import sys
import os
import re

requests_session = requests.Session() # to make it faster.

class TelegramBot:
    def __init__(self, database_path=None, bot_token=None):
        self.bot = self
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
                        if chat.chat_id in f.chat:
                            f.function(types.Message_(update.message))
                user = getattr(update.message, 'user', None)
                if user:
                    if isinstance(f, Filter.user):
                        if user.user_id in Filters.user:
                            f.function(types.Message_(update.message))
                text = getattr(update.message, 'text', None)
                if text:
                    if isinstance(f, Filters.text):
                        if text in f.text:
                            f.function(types.Message_(self.bot, update.message))
                    if isinstance(f, Filters.command):
                        splited_text = text.split()
                        cmd_starts_with = splited_text[0][0]
                        cmd = splited_text[0][1:]
                        if cmd_starts_with in self.COMMAND_STARTS_WITH or cmd_starts_with in f.starts_with:
                            if cmd in f.command:
                                f.function(types.Message_(self.bot, update.message))
            if update.callback_query:
                data = getattr(update.callback_query, 'data', None)
                if data:
                    if isinstance(f, Filters.CallbackQuery):
                        if data in f.data:
                            f.function(types.CallbackQuery_(self.bot, update.callback_query))
            if update.chat_member:
                chat_member = update.chat_member
                old_member = chat_member.old_chat_member
                new_member = chat_member.new_chat_member
                if isinstance(f, Filters.chat):
                    if True in f.chat or None in f.chat or chat_member.chat.chat_id in f.chat:
                        # Chat Joined.
                        if True in f.joined or new_member.user.user_id in f.joined:
                            if old_member.status == 'left' and chat_member.from_user.user_id == new_member.user.user_id:
                                f.function(types.Message_(self.bot, types.ChatJoined(update.chat_member)))
                        # Chat Left.
                        if True in f.left or new_member.user.user_id in f.left:
                            if new_member.status == 'left':
                                f.function(types.Message_(self.bot, types.ChatLeft(update.chat_member)))
                        # Chat Added.
                        if True in f.added or new_member.user.user_id in f.added:
                            if chat_member.from_user.user_id != new_member.user.user_id:
                                f.function(types.Message_(self.bot, types.ChatAdded(update.chat_member)))

    def check(self, data, url):
        des = data['description'][13:]
        m = methods.parse_url(url)
        if des == 'chat not found':
            raise exceptions.ChatNotFound(m.get('chat_id'))
        elif des == 'message text is empty':
            raise exceptions.MessageTextIsEmpty()
        elif des == 'field "inline_keyboard" of the InlineKeyboardMarkup must be an Array of Arrays':
            raise exceptions.InvalidKeyboardMarkup(array_of_array=True)
        elif des == 'there are no administrators in the private chat':
            raise exceptions.NoAdministratorsInPrivateChat(m.get('chat_id'))
        else:
            raise exceptions.UnKnownError(data['description'])

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

    def conversation(self, chat_id):
        if isinstance(chat_id, types.Chat):
            _chat_id = chat_id.chat_id
        elif isinstance(chat_id, types.User):
            _chat_id = chat_id.user_id
        elif isinstance(chat_id, types.Message):
            _chat_id = chat_id.chat.chat_id
        else:
            _chat_id = chat_id
        c = conv.Conversation(bot=self.bot, chat_id=_chat_id)
        self.conversations.append(c)
        return c

    def get_me(self):
        return methods.getMe(self.bot).get_me()

    def send_message(self, chat_id, text, parse_mode=None, entities=None, link_preview=None, disable_web_page_preview=None, disable_notification=None, protect_content=None, reply_to=None, reply_to_message_id=None, allow_sending_without_reply=None, buttons=None, reply_markup=None, **kwargs):
        if isinstance(chat_id, types.Chat):
            _chat_id = chat_id.chat_id
        elif isinstance(chat_id, types.User):
            _chat_id = chat_id.user_id
        elif isinstance(chat_id, types.Message):
            _chat_id = chat_id.chat.chat_id
        else:
            _chat_id = chat_id
        if parse_mode is None:
            parse_mode = self.parse_mode
        if not link_preview:
            disable_web_page_preview = self.default_settings.link_preview
        else:
            disable_web_page_preview = link_preview
        if reply_to:
            reply_to_message_id = reply_to
        if buttons:
            reply_markup = buttons
        msg = methods.sendMessage(bot=self.bot, chat_id=_chat_id, text=text, parse_mode=parse_mode, entities=entities, disable_notification=disable_notification, protect_content=protect_content, reply_to_message_id=reply_to_message_id, reply_markup=reply_markup, **kwargs).send_message()
        return types.Message_(bot=self.bot, msg=msg)

    def delete_message(self, chat_id, message_id, *args, **kwargs):
        if isinstance(chat_id, types.Chat):
            _chat_id = chat_id.chat_id
        elif isinstance(chat_id, types.User):
            _chat_id = chat_id.user_id
        elif isinstance(chat_id, types.Message):
            _chat_id = chat_id.chat.chat_id
        else:
            _chat_id = chat_id
        if isinstance(message_id, list):
            success = []
            for msg_id in message_id:
                d = methods.deleteMessage(bot=self.bot, chat_id=_chat_id, message_id=msg_id).delete_message()
                success.append(d)
            return d
        else:
            return methods.deleteMessage(bot=self.bot, chat_id=_chat_id, message_id=message_id, *args, **kwargs).delete_message()

    def forward_message(self, chat_id, from_chat_id, message_id, disable_notification=None, protect_content=None, **kwargs):
        if isinstance(chat_id, types.Chat):
            _chat_id = chat_id.chat_id
        elif isinstance(chat_id, types.Message):
            _chat_id = chat_id.chat.chat_id
        else:
            _chat_id = chat_id
        if isinstance(message_id, (types.Message, types._Message, types.MessageId)):
            _message_id = message_id.message_id
        else:
            _message_id = message_id
        return methods.forwardMessage(bot=self.bot, chat_id=_chat_id, disable_notification=disable_notification, protect_content=protect_content, message_id=_message_id).forward_message()

    def copy_message(self, chat_id, from_chat_id, message_id, caption=None, parse_mode=None, caption_entities=None, disable_notification=None, protect_content=None, reply_to=None, reply_to_message_id=None, allow_sending_without_reply=None, buttons=None, reply_markup=None, **kwargs):
        if isinstance(chat_id, types.Chat):
            _chat_id = chat_id.chat_id
        elif isinstance(chat_id, types.User):
            _chat_id = chat_id.user_id
        elif isinstance(chat_id, types.Message):
            _chat_id = chat_id.chat.chat_id
        else:
            _chat_id = chat_id
        if isinstance(from_chat_id, types.Chat):
            _from_chat_id = from_chat_id.chat_id
        elif isinstance(chat_id, types.User):
            _from_chat_id = from_chat_id.user_id
        elif isinstance(from_chat_id, types.Message):
            _from_chat_id = from_chat_id.chat.chat_id
        else:
            _from_chat_id = from_chat_id
        if isinstance(message_id, (types.Message, types._Message, types.MessageId)):
            _message_id = message_id.message_id
        else:
            _message_id = message_id
        if reply_to:
            reply_to_message_id = reply_to
        if buttons:
            reply_markup = buttons
        return methods.copyMessage(bot=self.bot, chat_id=_chat_id, from_chat_id=_from_chat_id, message_id=_message_id, caption=caption, parse_mode=parse_mode, caption_entities=caption_entities, disable_notification=disable_notification, protect_content=protect_content, reply_to_message_id=reply_to_message_id, allow_sending_without_reply=allow_sending_without_reply, reply_markup=reply_markup, **kwargs)

    def send_photo(self, chat_id, photo, caption=None, parse_mode=None, caption_entities=None, disable_notification=False, protect_content=False, reply_to=None, reply_to_message_id=None, allow_sending_without_reply=None, buttons=None, reply_markup=None, **kwargs):
        if isinstance(chat_id, types.Chat):
            _chat_id = chat_id.chat_id
        elif isinstance(chat_id, types.Message):
            _chat_id = chat_id.chat.chat_id
        else:
            _chat_id = chat_id
        if not parse_mode:
            parse_mode = self.default_settings.parse_mode
        if not link_preview:
            disable_web_page_preview = self.default_settings.link_preview
        else:
            disable_web_page_preview = link_preview
        if reply_to:
            reply_to_message_id = reply_to
        if buttons:
            reply_markup = buttons
        msg = methods.sendPhoto(bot=self.bot, chat_id=_chat_id, photo=photo, caption=caption, parse_mode=parse_mode, caption_entities=caption_entities, disable_notification=disable_notification, protect_content=protect_content, reply_to_message_id=reply_to_message_id, allow_sending_without_reply=allow_sending_without_reply, reply_markup=reply_markup, **kwargs).send_photo()
        return types.Message_(msg)

    def send_video(self, chat_id, video, duration=None, width=None, height=None, thumb=None, caption=None, parse_mode=None, caption_entities=None, supports_streaming=None, disable_notification=False, protect_content=False, reply_to=None, reply_to_message_id=None, allow_sending_without_reply=None, buttons=None, reply_markup=None, **kwargs):
        if isinstance(chat_id, types.Chat):
            _chat_id = chat_id.chat_id
        elif isinstance(chat_id, types.Message):
            _chat_id = chat_id.chat.chat_id
        else:
            _chat_id = chat_id
        if not parse_mode:
            parse_mode = self.default_settings.parse_mode
        if reply_to:
            reply_to_message_id = reply_to
        if buttons:
            reply_markup = buttons
        msg = methods.sendVideo(bot=self.bot, chat_id=_chat_id, video=video, duration=duration, width=width, height=height, caption=caption, parse_mode=parse_mode, caption_entities=caption_entities, supports_streaming=supports_streaming, disable_notification=disable_notification, protect_content=protect_content, reply_to_message_id=reply_to_message_id, allow_sending_without_reply=allow_sending_without_reply, reply_markup=reply_markup, **kwargs).send_video()
        return types.Message_(msg)

    def send_audio(self, chat_id, audio, caption=None, parse_mode=None, caption_entities=None, duration=None, performer=None, title=None, thumb=None, disable_notification=None, protect_content=False, reply_to=None, reply_to_message_id=None, allow_sending_without_reply=None, buttons=None, reply_markup=None, **kwargs):
        if isinstance(chat_id, types.Chat):
            _chat_id = chat_id.chat_id
        elif isinstance(chat_id, types.Message):
            _chat_id = chat_id.chat.chat_id
        else:
            _chat_id = chat_id
        if not parse_mode:
            parse_mode = self.default_settings.parse_mode
        if reply_to:
            reply_to_message_id = reply_to
        if buttons:
            reply_markup = buttons
        msg = methods.sendAudio(bot=self.bot, chat_id=_chat_id, audio=audio, caption=caption, parse_mode=parse_mode, caption_entities=caption_entities, duration=duration, performer=performer, title=title, thumb=thumb, disable_notification=disable_notification, protect_content=protect_content, reply_to_message_id=reply_to_message_id, allow_sending_without_reply=allow_sending_without_reply, reply_markup=reply_markup, **kwargs).send_audio()
        return types.Message_(msg)

    def send_document(self, chat_id, document, thumb=None, caption=None, parse_mode=None, caption_entities=None, disable_content_type_detection=None, disable_notification=None, protect_content=False, reply_to=None, reply_to_message_id=None, allow_sending_without_reply=None, buttons=None, reply_markup=None, **kwargs):
        if isinstance(chat_id, types.Chat):
            _chat_id = chat_id.chat_id
        elif isinstance(chat_id, types.Message):
            _chat_id = chat_id.chat.chat_id
        else:
            _chat_id = chat_id
        if not parse_mode:
            parse_mode = self.default_settings.parse_mode
        if reply_to:
            reply_to_message_id = reply_to
        if buttons:
            reply_markup = buttons
        msg = methods.sendDocument(bot=self.bot, chat_id=_chat_id, document=document, caption=caption, parse_mode=parse_mode, caption_entities=caption_entities, disable_content_type_detection=disable_content_type_detection, disable_notification=disable_notification, protect_content=protect_content, reply_to_message_id=reply_to_message_id, allow_sending_without_reply=allow_sending_without_reply, reply_markup=reply_markup, **kwargs).send_document()
        return types.Message_(msg)

    def send_animation(self, chat_id, animation, duration=None, width=None, height=None, thumb=None, caption=None, parse_mode=None, caption_entities=None, disable_notification=None, protect_content=False, reply_to=None, reply_to_message_id=None, allow_sending_without_reply=None, buttons=None, reply_markup=None, **kwargs):
        if isinstance(chat_id, types.Chat):
            _chat_id = chat_id.chat_id
        elif isinstance(chat_id, types.Message):
            _chat_id = chat_id.chat.chat_id
        else:
            _chat_id = chat_id
        if not parse_mode:
            parse_mode = self.default_settings.parse_mode
        if reply_to:
            reply_to_message_id = reply_to
        if buttons:
            reply_markup = buttons
        msg = methods.sendAnimation(bot=self.bot, chat_id=_chat_id, animation=animation, duration=duration, width=width, height=height, thumb=thumb, caption=caption, parse_mode=parse_mode, caption_entities=caption_entities, disable_notification=disable_notification, protect_content=protect_content, reply_to_message_id=reply_to_message_id, allow_sending_without_reply=allow_sending_without_reply, reply_markup=reply_markup, **kwargs).send_animation()
        return types.Message_(msg)

    def send_voice(self, chat_id, voice, caption=None, parse_mode=None, caption_entities=None, duration=None, disable_notification=None, protect_content=False, reply_to=None, reply_to_message_id=None, allow_sending_without_reply=None, buttons=None, reply_markup=None, **kwargs):
        if isinstance(chat_id, types.Chat):
            _chat_id = chat_id.chat_id
        elif isinstance(chat_id, types.Message):
            _chat_id = chat_id.chat.chat_id
        else:
            _chat_id = chat_id
        if not parse_mode:
            parse_mode = self.default_settings.parse_mode
        if reply_to:
            reply_to_message_id = reply_to
        if buttons:
            reply_markup = buttons
        msg = methods.sendVoice(bot=self.bot, chat_id=_chat_id, voice=voice, width=width, caption=caption, parse_mode=parse_mode, caption_entities=caption_entities, duration=duration, disable_notification=disable_notification, protect_content=protect_content, reply_to_message_id=reply_to_message_id, allow_sending_without_reply=allow_sending_without_reply, reply_markup=reply_markup, **kwargs).send_voice()
        return types.Message_(msg)

    def send_video_note(self, chat_id, video_note, duration=None, length=None, thumb=None, disable_notification=False, protect_content=False, reply_to=None, reply_to_message_id=None, allow_sending_without_reply=None, buttons=None, reply_markup=None, **kwargs):
        if isinstance(chat_id, types.Chat):
            _chat_id = chat_id.chat_id
        elif isinstance(chat_id, types.Message):
            _chat_id = chat_id.chat.chat_id
        else:
            _chat_id = chat_id
        if reply_to:
            reply_to_message_id = reply_to
        if buttons:
            reply_markup = buttons
        msg = methods.sendVideoNote(bot=self.bot, chat_id=_chat_id, video_note=video_note, duration=duration, width=width, length=None, caption_entities=caption_entities, disable_notification=disable_notification, protect_content=protect_content, reply_to_message_id=reply_to_message_id, allow_sending_without_reply=allow_sending_without_reply, reply_markup=reply_markup, **kwargs).send_video_note()
        return types.Message_(msg)

    def send_media_group(self, chat_id, media, disable_notification=None, protect_content=None, reply_to=None, reply_to_message_id=None, allow_sending_without_reply=None, **kwargs):
        if isinstance(chat_id, types.Chat):
            _chat_id = chat_id.chat_id
        elif isinstance(chat_id, types.Message):
            _chat_id = chat_id.chat.chat_id
        else:
            _chat_id = chat_id
        if reply_to:
            reply_to_message_id = reply_to
        msg = methods.sendMediaGroup(boy=self.bot, chat_id=_chat_id, media=media, disable_notification=disable_notification, protect_content=protect_content, reply_to_message_id=reply_to_message_id, allow_sending_without_reply=allow_sending_without_reply, **kwargs).send_media_group()
        return types.Message_(msg)

    def send_location(self, chat_id, latitude, longitude, horizontal_accuracy=None, live_period=None, heading=None, proximity_alert_radius=None, disable_notification=None, protect_content=None, reply_to=None, reply_to_message_id=None, allow_sending_without_reply=None, buttons=None, reply_markup=None, **kwargs):
        if isinstance(chat_id, types.Chat):
            _chat_id = chat_id.chat_id
        elif isinstance(chat_id, types.Message):
            _chat_id = chat_id.chat.chat_id
        else:
            _chat_id = chat_id
        if reply_to:
            reply_to_message_id = reply_to
        if buttons:
            reply_markup = buttons
        msg = methods.sendLocation(bot=self.bot, chat_id=_chat_id, latitude=latitude, longitude=longitude, horizontal_accuracy=horizontal_accuracy, live_period=live_period, heading=heading, proximity_alert_radius=proximity_alert_radius, disable_notification=disable_notification, protect_content=protect_content, reply_to_message_id=reply_to_message_id, allow_sending_without_reply=allow_sending_without_reply, reply_markup=reply_markup, **kwargs)
        return types.Message_(msg)

    def edit_message_live_location(self, latitude, longitude, chat_id=None, message_id=None, inline_message_id=None, heading=None, proximity_alert_radius=None, buttons=None, reply_markup=None, **kwargs):
        if isinstance(chat_id, types.Chat):
            _chat_id = chat_id.chat_id
        elif isinstance(chat_id, types.Message):
            _chat_id = chat_id.chat.chat_id
        else:
            _chat_id = chat_id
        if isinstance(message_id, (types.Message, types._Message, types.MessageId)):
            _message_id = message_id.message_id
        else:
            _message_id = message_id
        if reply_to:
            reply_to_message_id = reply_to
        if buttons:
            reply_markup = buttons
        msg = methods.editMessageLiveLocation(bot=self.bot, chat_id=_chat_id, message_id=_message_id, inline_message_id=inline_message_id, latitude=latitude, longitude=longitude, horizontal_accuracy=horizontal_accuracy, heading=heading, proximity_alert_radius=proximity_alert_radius, reply_markup=reply_markup, **kwargs)
        return types.Message_(msg)

    def send_venue(self, chat_id, latitude, longitude, title, address, foursquare_id=None, foursquare_type=None, google_place_id=None, google_place_type=None, disable_notification=None, protect_content=None, reply_to=None, reply_to_message_id=None, allow_sending_without_reply=None, buttons=None, reply_markup=None, **kwargs):
        if isinstance(chat_id, types.Chat):
            _chat_id = chat_id.chat_id
        elif isinstance(chat_id, types.Message):
            _chat_id = chat_id.chat.chat_id
        else:
            _chat_id = chat_id
        if reply_to:
            reply_to_message_id = reply_to
        if buttons:
            reply_markup = buttons
        msg = methods.sendVenue(bot=self.bot, chat_id=_chat_id, latitude=latitude, longitude=longitude, title=title, address=address, foursquare_id=foursquare_id, foursquare_type=foursquare_type, google_place_id=google_place_id, google_place_type=google_place_type, disable_notification=disable_notification, protect_content=protect_content, reply_to_message_id=reply_to_message_id, allow_sending_without_reply=allow_sending_without_reply, reply_markup=reply_markup, **kwargs).send_venue()

    def send_poll(self, bot, chat_id, question, options, is_anonymous=None, type=None, allows_multiple_answers=None, correct_option_id=None, explanation=None, explanation_parse_mode=None, explanation_entities=None, open_period=None, close_date=None, is_closed=None, disable_notification=None, protect_content=None, reply_to=None, reply_to_message_id=None, allow_sending_without_reply=None, buttons=None, reply_markup=None, **kwargs):
        if isinstance(chat_id, types.Chat):
            _chat_id = chat_id.chat_id
        elif isinstance(chat_id, types.Message):
            _chat_id = chat_id.chat.chat_id
        else:
            _chat_id = chat_id
        if reply_to:
            reply_to_message_id = reply_to
        if buttons:
            reply_markup = buttons
        msg = methods.sendPoll(bot=self.bot, chat_id=_chat_id, question=question, options=options, is_anonymous=is_anonymous, type=type, allows_multiple_answers=allows_multiple_answers, correct_option_id=correct_option_id, explanation=explanation, explanation_parse_mode=explanation_parse_mode, explanation_entities=explanation_entities, open_period=open_period, close_date=close_date, is_closed=is_closed, disable_notification=disable_notification, protect_content=protect_content, reply_to_message_id=reply_to_message_id, allow_sending_without_reply=allow_sending_without_reply, reply_markup=reply_markup, **kwargs).send_poll()
        return types.Message_(msg)

    def send_dice(self, chat_id, emoji=None, disable_notification=None, protect_content=None, reply_to=None, reply_to_message_id=None, allow_sending_without_reply=None, buttons=None, reply_markup=None, **kwargs):
        if isinstance(chat_id, types.Chat):
            _chat_id = chat_id.chat_id
        elif isinstance(chat_id, types.Message):
            _chat_id = chat_id.chat.chat_id
        else:
            _chat_id = chat_id
        if reply_to:
            reply_to_message_id = reply_to
        if buttons:
            reply_markup = buttons
        msg = methods.sendDice(bot=self.bot, chat_id=_chat_id, emoji=emoji, disable_notification=disable_notification, protect_content=protect_content, reply_to_message_id=reply_to_message_id, allow_sending_without_reply=allow_sending_without_reply, reply_markup=reply_markup, **kwargs)
        return types.Message_(msg)

    def send_action(self, chat_id, action, **kwargs):
        if isinstance(chat_id, types.Chat):
            _chat_id = chat_id.chat_id
        elif isinstance(chat_id, types.Message):
            _chat_id = chat_id.chat.chat_id
        else:
            _chat_id = chat_id
        return methods.sendAction(bot=self.bot, chat_id=_chat_id, action=action, **kwargs).send_action()

    def get_user_profile_photos(self, user_id, offset=None, limit=None, **kwargs):
        if isinstance(user_id, types.User):
            _user_id = user_id.chat_id
        elif isinstance(chat_id, types.Message):
            _user_id = user_id.user.user_id
        else:
            _user_id = user_id
        return methods.getUserProfilePhotos(bot=self.bot, user_id=_user_id, offset=offset, limit=limit, **kwargs).get_user_profile_photos()

    def get_file(self, file_id, **kwargs):
        return methods.getFile(bot=self.bot, file_id=file_id, **kwargs).get_file()

    def ban_user(self, chat_id, user_id, until_date=None, revoke_messages=None, *args, **kwargs):
        if isinstance(chat_id, types.Chat):
            _chat_id = chat_id.chat_id
        elif isinstance(chat_id, types.User):
            _chat_id = chat_id.user_id
        elif isinstance(chat_id, types.Message):
            _chat_id = chat_id.chat.chat_id
        else:
            _chat_id = chat_id
        if isinstance(user_id, types.User):
            _user_id = user_id.user_id
        elif isinstance(user_id, types.Message):
            _user_id = user_id.user.user_id
        else:
            _user_id = user_id
        return methods.banChatMember(bot=self.bot, chat_id=_chat_id, user_id=_user_id, until_date=until_date, revoke_messages=revoke_messages, *args, **kwargs).ban_chat_member()

    def unban_user(self, chat_id, user_id, only_if_banned, *args, **kwargs):
        if isinstance(chat_id, types.Chat):
            _chat_id = chat_id.chat_id
        elif isinstance(chat_id, types.Message):
            _chat_id = chat_id.chat.chat_id
        else:
            _chat_id = chat_id
        if isinstance(user_id, types.User):
            _user_id = user_id.user_id
        elif isinstance(user_id, types.Message):
            _user_id = user_id.user.user_id
        else:
            _user_id = user_id
        return methods.unbanChatMember(bot=self.bot, chat_id=_chat_id, user_id=_user_id, only_if_banned=only_if_banned, *args, **kwargs).unban_chat_member()

    def restrict_user(self, chat_id, user_id, permissions, until_date, *args, **kwargs):
        if isinstance(chat_id, types.Chat):
            _chat_id = chat_id.chat_id
        elif isinstance(chat_id, types.Message):
            _chat_id = chat_id.chat.chat_id
        else:
            _chat_id = chat_id
        if isinstance(user_id, types.User):
            _user_id = user_id.user_id
        elif isinstance(user_id, types.Message):
            _user_id = user_id.user.user_id
        else:
            _user_id = user_id
        return methods.restrictChatMember(bot=self.bot, chat_id=_chat_id, permissions=permissions, until_date=until_date, *args, **kwargs).restrict_chat_member()

    def promote_user(self, chat_id, user_id, is_anonymous=None, can_manage_chat=None, can_post_messages=None, can_edit_messages=None, can_delete_messages=None, can_manage_video_chats=None, can_restrict_members=None, can_promote_members=None, can_change_info=None, can_invite_users=None, can_pin_messages=None, **kwargs):
        if isinstance(chat_id, types.Chat):
            _chat_id = chat_id.chat_id
        elif isinstance(chat_id, types.Message):
            _chat_id = chat_id.chat.chat_id
        else:
            _chat_id = chat_id
        if isinstance(user_id, types.User):
            _user_id = user_id.user_id
        elif isinstance(user_id, types.Message):
            _user_id = user_id.user.user_id
        else:
            _user_id = user_id
        return methods.promoteChatMember(bot=self.bot, chat_id=_chat_id, user_id=_user_id, is_anonymous=is_anonymous, can_manage_chat=can_manage_chat, can_post_messages=can_post_messages, can_edit_messages=can_edit_messages, can_delete_messages=can_delete_messages, can_manage_video_chats=can_manage_video_chats, can_restrict_members=can_restrict_members, can_promote_members=can_promote_members, can_change_info=can_change_info, can_invite_users=can_invite_users, can_pin_messages=can_pin_messages, **kwargs).promote_chat_member()

    def set_chat_administrator_custom_title(self, chat_id, user_id, custom_title, **kwargs):
        if isinstance(chat_id, types.Chat):
            _chat_id = chat_id.chat_id
        elif isinstance(chat_id, types.Message):
            _chat_id = chat_id.chat.chat_id
        else:
            _chat_id = chat_id
        if isinstance(user_id, types.User):
            _user_id = user_id.user_id
        elif isinstance(user_id, types.Message):
            _user_id = user_id.user.user_id
        else:
            _user_id = user_id
        return methods.setChatAdministratorCustomTitle(bot=self.bot, chat_id=_chat_id, user_id=_user_id, custom_title=custom_title, **kwargs).set_chat_administrator_custom_title()

    def ban_chat(self, chat_id, sender_chat_id, *args, **kwargs):
        if isinstance(chat_id, types.Chat):
            _chat_id = chat_id.chat_id
        elif isinstance(chat_id, types.Message):
            _chat_id = chat_id.chat.chat_id
        else:
            _chat_id = chat_id
        if isinstance(sender_chat_id, types.Chat):
            _sender_id = sender_chat_id.chat_id
        elif isinstance(sender_chat_id, types.Message):
            _sender_id = sender_chat_id.chat.chat_id
        else:
            _sender_id = sender_chat_id
        return methods.banChatSenderChat(bot=self.bot, chat_id=_chat_id, sender_chat_id=_sender_chat_id, *args, **kwargs).ban_chat_sender_chat()

    def unban_chat(self, chat_id, sender_chat_id, *args, **kwargs):
        if isinstance(chat_id, types.Chat):
            _chat_id = chat_id.chat_id
        elif isinstance(chat_id, types.Message):
            _chat_id = chat_id.chat.chat_id
        else:
            _chat_id = chat_id
        if isinstance(sender_chat_id, types.Chat):
            _sender_id = sender_chat_id.chat_id
        elif isinstance(sender_chat_id, types.Message):
            _sender_id = sender_chat_id.chat.chat_id
        else:
            _sender_id = sender_chat_id
        return methods.unbanChatSenderChat(bot=self.bot, chat_id=_chat_id, sender_chat_id=_sender_chat_id, *args, **kwargs).unban_chat_sender_chat()

    def set_chat_permissions(self, chat_id, permissions, **kwargs):
        if isinstance(chat_id, types.Chat):
            _chat_id = chat_id.chat_id
        elif isinstance(chat_id, types.Message):
            _chat_id = chat_id.chat.chat_id
        else:
            _chat_id = chat_id
        return methods.setChatPermissions(bot=self.bot, chat_id=_chat_id, permissions=permissions, **kwargs).set_chat_permissions()

    def export_chat_invite_link(self, chat_id, **kwargs):
        if isinstance(chat_id, types.Chat):
            _chat_id = chat_id.chat_id
        elif isinstance(chat_id, types.Message):
            _chat_id = chat_id.chat.chat_id
        else:
            _chat_id = chat_id
        return methods.exportChatInviteLink(bot=self.bot, chat_id=_chat_id, **kwargs).export_chat_invite_link()

    def create_chat_invite_link(self, chat_id, name=None, expire_date=None, member_limit=None, creates_join_request=None, **kwargs):
        if isinstance(chat_id, types.Chat):
            _chat_id = chat_id.chat_id
        elif isinstance(chat_id, types.Message):
            _chat_id = chat_id.chat.chat_id
        else:
            _chat_id = chat_id
        return methods.createChatInviteLink(bot=self.bot, chat_id=_chat_id, name=name, expire_date=expire_date, member_limit=member_limit, creates_join_request=creates_join_request, **kwargs).create_chat_invite_link()

    def edit_chat_invite_link(self, chat_id, invite_link, name=None, expire_date=None, member_limit=None, creates_join_request=None, **kwargs):
        if isinstance(chat_id, types.Chat):
            _chat_id = chat_id.chat_id
        elif isinstance(chat_id, types.Message):
            _chat_id = chat_id.chat.chat_id
        else:
            _chat_id = chat_id
        return methods.editChatInviteLink(bot=self.bot, chat_id=_chat_id, invite_link=invite_link, name=name, expire_date=expire_date, member_limit=member_limit, creates_join_request=creates_join_request, **kwargs).editChatInviteLink()

    def revoke_chat_invite_link(self, chat_id, invite_link, **kwargs):
        if isinstance(chat_id, types.Chat):
            _chat_id = chat_id.chat_id
        elif isinstance(chat_id, types.Message):
            _chat_id = chat_id.chat.chat_id
        else:
            _chat_id = chat_id
        return methods.revokeChatInviteLink(bot=self.bot, chat_id=_chat_id, invite_link=invite_link, **kwargs).revoke_chat_invite_link()

    def approve_chat_join_request(self, chat_id, user_id, **kwargs):
        if isinstance(chat_id, types.Chat):
            _chat_id = chat_id.chat_id
        elif isinstance(chat_id, types.Message):
            _chat_id = chat_id.chat.chat_id
        else:
            _chat_id = chat_id
        if isinstance(user_id, types.User):
            _user_id = user_id.user_id
        elif isinstance(user_id, types.Message):
            _user_id = user_id.user.chat_id
        else:
            _user_id = user_id
        return methods.approveChatJoinRequest(bot=self.bot, chat_id=_chat_id, user_id=_user_id, **kwargs).approve_chat_join_request()

    def decline_chat_join_request(self, chat_id, user_id, **kwargs):
        if isinstance(chat_id, types.Chat):
            _chat_id = chat_id.chat_id
        elif isinstance(chat_id, types.Message):
            _chat_id = chat_id.chat.chat_id
        else:
            _chat_id = chat_id
        if isinstance(user_id, types.User):
            _user_id = user_id.user_id
        elif isinstance(user_id, types.Message):
            _user_id = user_id.user.chat_id
        else:
            _user_id = user_id
        return methods.declineChatJoinRequest(bot=self.bot, chat_id=_chat_id, user_id=_user_id, **kwargs).decline_chat_join_request()

    def set_chat_photo(self, chat_id, photo, **kwargs):
        if isinstance(chat_id, types.Chat):
            _chat_id = chat_id.chat_id
        elif isinstance(chat_id, types.Message):
            _chat_id = chat_id.chat.chat_id
        else:
            _chat_id = chat_id
        return methods.setChatPhoto(bot=self.bot, chat_id=_chat_id, photo=photo, **kwargs).set_chat_photo()

    def delete_chat_photo(self, chat_id, **kwargs):
        if isinstance(chat_id, types.Chat):
            _chat_id = chat_id.chat_id
        elif isinstance(chat_id, types.Message):
            _chat_id = chat_id.chat.chat_id
        else:
            _chat_id = chat_id
        return methods.deleteChatPhoto(bot=self.bot, chat_id=_chat_id, **kwargs).delete_chat_photo()

    def set_chat_title(self, chat_id, title, **kwargs):
        if isinstance(chat_id, types.Chat):
            _chat_id = chat_id.chat_id
        elif isinstance(chat_id, types.Message):
            _chat_id = chat_id.chat.chat_id
        else:
            _chat_id = chat_id
        return methods.setChatTitle(bot=self.bot, chat_id=_chat_id, title=title, **kwargs).set_chat_title()

    def set_chat_description(self, chat_id, description, **kwargs):
        if isinstance(chat_id, types.Chat):
            _chat_id = chat_id.chat_id
        elif isinstance(chat_id, types.Message):
            _chat_id = chat_id.chat.chat_id
        else:
            _chat_id = chat_id
        return methods.setChatDescription(bot=self.bot, description=description).set_chat_description()

    def pin_chat_message(self, chat_id, message_id, disable_notification=None, **kwargs):
        if isinstance(chat_id, types.Chat):
            _chat_id = chat_id.chat_id
        elif isinstance(chat_id, types.Message):
            _chat_id = chat_id.chat.chat_id
        else:
            _chat_id = chat_id
        if isinstance(message_id, (types.Message, types._Message, types.MessageId)):
            _message_id = message_id.message_id
        else:
            _message_id = message_id
        return methods.pinChatMessage(bot=self.bot, message_id=_message_id, disable_notification=disable_notification, **kwargs).pin_chat_message()

    # Short-Hand-Method for pin_chat_message.
    def pin_message(self, chat_id, message_id, disable_notification=None, **kwargs):
        return self.pin_chat_message(chat_id=chat_id, message_id=message_id, disable_notification=disable_notification, **kwargs)

    def unpin_chat_message(self, chat_id, message_id, **kwargs):
        if isinstance(chat_id, types.Chat):
            _chat_id = chat_id.chat_id
        elif isinstance(chat_id, types.Message):
            _chat_id = chat_id.chat.chat_id
        else:
            _chat_id = chat_id
        if isinstance(message_id, (types.Message, types._Message, types.MessageId)):
            _message_id = message_id.message_id
        else:
            _message_id = message_id
        return methods.unpinChatMessage(bot=self.bot, message_id=_message_id, **kwargs).unpin_chat_message()

    # Short-Hand-Method for unpin_chat_message.
    def unpin_message(self, chat_id, message_id, disable_notification=None, **kwargs):
        return self.unpin_chat_message(chat_id=chat_id, message_id=message_id, disable_notification=disable_notification, **kwargs)

    def unpin_all_chat_messages(self, chat_id, **kwargs):
        if isinstance(chat_id, types.Chat):
            _chat_id = chat_id.chat_id
        elif isinstance(chat_id, types.Message):
            _chat_id = chat_id.chat.chat_id
        else:
            _chat_id = chat_id
        return methods.unpinAllChatMessages(bot=self.bot, chat_id=_chat_id, **kwargs).unpin_all_chat_messages()

    # Short-Hand-Method for unpin_all_chat_messages.
    def unpin_all_messages(self, chat_id):
        return self.unpin_all_chat_messages(chat_id=chat_id)

    def leave_chat(self, chat_id, **kwargs):
        if isinstance(chat_id, types.Chat):
            _chat_id = chat_id.chat_id
        elif isinstance(chat_id, types.Message):
            _chat_id = chat_id.chat.chat_id
        else:
            _chat_id = chat_id
        return methods.leaveChat(bot=self.bot, chat_id=_chat_id, **kwargs).leave_chat()

    def get_chat(self, chat_id, *args, **kwargs):
        if isinstance(chat_id, types.Chat):
            _chat_id = chat_id.chat_id
        elif isinstance(chat_id, types.User):
            _chat_id = chat_id.user_id
        elif isinstance(chat_id, types.Message):
            _chat_id = chat_id.chat.chat_id
        else:
            _chat_id = chat_id
        return methods.getChat(bot=self.bot, chat_id=_chat_id, **kwargs).get_chat()

    def get_chat_administrators(self, chat_id, **kwargs):
        if isinstance(chat_id, types.Chat):
            _chat_id = chat_id.chat_id
        elif isinstance(chat_id, types.User):
            _chat_id = chat_id.user_id
        elif isinstance(chat_id, types.Message):
            _chat_id = chat_id.chat.chat_id
        else:
            _chat_id = chat_id
        return methods.getChatAdministrators(bot=self.bot, chat_id=_chat_id, **kwargs).get_chat_administrators()

    # Short-Hand-Method for get_chat_administrators.
    def getAdmins(self, chat_id, **kwargs):
        return self.get_chat_administrators(chat_id=chat_id, **kwargs)

    def get_chat_member_count(self, chat_id):
        if isinstance(chat_id, types.Chat):
            _chat_id = chat_id.chat_id
        elif isinstance(chat_id, types.Message):
            _chat_id = chat_id.chat.chat_id
        else:
            _chat_id = chat_id
        return methods.getChatMemberCount(bot=self.bot, chat_id=_chat_id, **kwargs).get_chat_member_count()

    def get_chat_member(self, chat_id, user_id, *args, **kwargs):
        if isinstance(chat_id, types.Chat):
            _chat_id = chat_id.chat_id
        elif isinstance(chat_id, types.Message):
            _chat_id = chat_id.chat.chat_id
        else:
            _chat_id = chat_id
        if isinstance(user_id, types.User):
            _user_id = user_id.user_id
        elif isinstance(user_id, types.Message):
            _user_id = user_id.user.user_id
        else:
            _user_id = user_id
        return methods.getChatMember(bot=self.bot, chat_id=_chat_id, user_id=_user_id, **kwargs).get_chat_member()

    def set_chat_sticker_set(self, chat_id, sticker_set_name, **kwargs):
        if isinstance(chat_id, types.Chat):
            _chat_id = chat_id.chat_id
        elif isinstance(chat_id, types.Message):
            _chat_id = chat_id.chat.chat_id
        else:
            _chat_id = chat_id
        return methods.setChatStickerSet(bot=self.bot, sticker_set_name=sticker_set_name, **kwargs).set_chat_sticker_set()

    def delete_chat_sticker_set(self, chat_id, **kwargs):
        if isinstance(chat_id, types.Chat):
            _chat_id = chat_id.chat_id
        elif isinstance(chat_id, types.Message):
            _chat_id = chat_id.chat.chat_id
        else:
            _chat_id = chat_id
        return methods.deleteChatStickerSet(bot=self.bot, **kwargs).delete_chat_sticker_set()

    def answer_callback_query(self, callback_query_id, text=None, show_alert=False, url=None, cache_time=0, **kwargs):
        return methods.answerCallbackQuery(bot=self.bot, callback_query_id=callback_query_id, text=text, show_alert=show_alert, url=url, cache_time=cache_time, **kwargs).answer_callback_query()

    def set_my_commands(self, commands, scope=None, language_code=None, **kwargs):
        return methods.setMyCommands(bot=self.bot, commands=commands, scope=scope, language_code=language_code, **kwargs).set_my_commands()

    def delete_my_commands(self, scope=None, language_code=None, **kwargs):
        return methods.deleteMyCommands(bot=self.bot, scope=scope, language_code=language_code, **kwargs).delete_my_commands()

    def get_my_commands(self, scope=None, language_code=None, **kwargs):
        return methods.getMyCommands(bot=self.bot, scope=scope, language_code=language_code, **kwargs).get_my_commands()

    def set_chat_menu_button(self, chat_id=None, menu_button=None, **kwargs):
        return methods.setChatMenuButton(bot=self.bot, chat_id=chat_id, menu_button=menu_button).set_chat_menu_button()

    def get_chat_menu_button(self, chat_id=None, **kwargs):
        return methods.setChatMenuButton(bot=self.bot, chat_id=chat_id).get_chat_menu_button()

    def set_my_default_administrator_rights(self, rights=None, for_channels=None, **kwargs):
        return methods.setMyDefaultAdministratorRights(bot=self.bot, rights=rights, for_channels=for_channels, **kwargs).set_my_default_administrator_rights()

    def get_my_default_administrator_rights(self, for_channels=None, **kwargs):
        return methods.setMyDefaultAdministratorRights(bot=self.bot, for_channels=for_channels, **kwargs).get_my_default_administrator_rights()

    def edit_message_text(self, text, chat_id=None, message_id=None, inline_message_id=None, parse_mode=None, entities=None, link_preview=None, disable_web_page_preview=None, buttons=None, reply_markup=None, **kwargs):
        if isinstance(chat_id, types.Chat):
            _chat_id = chat_id.chat_id
        elif isinstance(chat_id, types.User):
            _chat_id = chat_id.user_id
        elif isinstance(chat_id, types.Message):
            _chat_id = chat_id.chat.chat_id
        else:
            _chat_id = chat_id
        if isinstance(message_id, (types.Message, types._Message, types.MessageId)):
            _message_id = message_id.message_id
        else:
            _message_id = message_id
        if not parse_mode:
            parse_mode = self.default_settings.parse_mode
        if not link_preview:
            disable_web_page_preview = self.default_settings.link_preview
        else:
            disable_web_page_preview = link_preview
        if buttons:
            reply_markup = buttons
        msg = methods.editMessageText(bot=self.bot, chat_id=_chat_id, message_id=_message_id, inline_message_id=inline_message_id, text=text, parse_mode=parse_mode, entities=entities, disable_web_page_preview=disable_web_page_preview, reply_markup=reply_markup, **kwargs).edit_message_text()
        if msg is True:
            return msg
        else:
            return types.Message_(bot=self.bot, msg=msg)

    def edit_message_caption(self, chat_id=None, message_id=None, inline_message_id=None, caption=None, parse_mode=None, caption_entities=None, buttons=None, reply_markup=None, **kwargs):
        if isinstance(chat_id, types.Chat):
            _chat_id = chat_id.chat_id
        elif isinstance(chat_id, types.User):
            _chat_id = chat_id.user_id
        elif isinstance(chat_id, types.Message):
            _chat_id = chat_id.chat.chat_id
        else:
            _chat_id = chat_id
        if isinstance(message_id, (types.Message, types._Message, types.MessageId)):
            _message_id = message_id.message_id
        else:
            _message_id = message_id
        if not parse_mode:
            parse_mode = self.default_settings.parse_mode
        if buttons:
            reply_markup = buttons
        msg = methods.editMessageCaption(bot=self.bot, chat_id=_chat_id, message_id=_message_id, inline_message_id=inline_message_id, caption=caption, parse_mode=parse_mode, caption_entities=caption_entities, reply_markup=reply_markup, **kwargs).edit_message_caption()
        if msg is True:
            return msg
        else:
            return types.Message_(bot=self.bot, msg=msg)

    def edit_message_media(self, media, chat_id=None, message_id=None, inline_message_id=None, buttons=None, reply_markup=None, **kwargs):
        if isinstance(chat_id, types.Chat):
            _chat_id = chat_id.chat_id
        elif isinstance(chat_id, types.User):
            _chat_id = chat_id.user_id
        elif isinstance(chat_id, types.Message):
            _chat_id = chat_id.chat.chat_id
        else:
            _chat_id = chat_id
        if isinstance(message_id, (types.Message, types._Message, types.MessageId)):
            _message_id = message_id.message_id
        else:
            _message_id = message_id
        if not parse_mode:
            parse_mode = self.default_settings.parse_mode
        if buttons:
            reply_markup = buttons
        msg = methods.editMessageMedia(bot=self.bot, chat_id=_chat_id, message_id=_message_id, inline_message_id=inline_message_id, media=media, reply_markup=reply_markup, **kwargs).edit_message_media()
        if msg is True:
            return msg
        else:
            return types.Message_(bot=self.bot, msg=msg)

    def edit_message_reply_markup(self, chat_id=None, message_id=None, inline_message_id=None, buttons=None, reply_markup=None, **kwargs):
        if isinstance(chat_id, types.Chat):
            _chat_id = chat_id.chat_id
        elif isinstance(chat_id, types.User):
            _chat_id = chat_id.user_id
        elif isinstance(chat_id, types.Message):
            _chat_id = chat_id.chat.chat_id
        else:
            _chat_id = chat_id
        if isinstance(message_id, (types.Message, types._Message, types.MessageId)):
            _message_id = message_id.message_id
        else:
            _message_id = message_id
        if not parse_mode:
            parse_mode = self.default_settings.parse_mode
        if buttons:
            reply_markup = buttons
        msg = methods.editMessageReplyMarkup(bot=self.bot, chat_id=_chat_id, message_id=_message_id, inline_message_id=inline_message_id, reply_markup=reply_markup, **kwargs).edit_message_reply_markup()
        if msg is True:
            return msg
        else:
            return types.Message_(bot=self.bot, msg=msg)

    def stop_poll(self, chat_id, message_id, buttons=None, reply_markup=None, **kwargs):
        if isinstance(chat_id, types.Chat):
            _chat_id = chat_id.chat_id
        elif isinstance(chat_id, types.User):
            _chat_id = chat_id.user_id
        elif isinstance(chat_id, types.Message):
            _chat_id = chat_id.chat.chat_id
        else:
            _chat_id = chat_id
        if isinstance(message_id, (types.Message, types._Message, types.MessageId)):
            _message_id = message_id.message_id
        else:
            _message_id = message_id
        if buttons:
            reply_markup = buttons
        return methods.stopPoll(bot=self.bot, chat_id=_chat_id, message_id=_message_id, reply_markup=reply_markup, **kwargs)

    def send_sticker(self, chat_id, sticker, disable_notification=None, protect_content=None, reply_to=None, reply_to_message_id=None, allow_sending_without_reply=None, buttons=None, reply_markup=None, **kwargs):
        if isinstance(chat_id, types.Chat):
            _chat_id = chat_id.chat_id
        elif isinstance(chat_id, types.User):
            _chat_id = chat_id.user_id
        elif isinstance(chat_id, types.Message):
            _chat_id = chat_id.chat.chat_id
        else:
            _chat_id = chat_id
        if isinstance(message_id, (types.Message, types._Message, types.MessageId)):
            _message_id = message_id.message_id
        else:
            _message_id = message_id
        if reply_to:
            reply_markup = reply_to
        if buttons:
            reply_markup = buttons
        msg = methods.sendSticker(bot=self.bot, chat_id=chat_id, sticker=sticker, disable_notification=disable_notification, protect_content=protect_content, reply_to_message_id=reply_to_message_id, allow_sending_without_reply=allow_sending_without_reply, reply_markup=reply_markup, **kwargs).send_sticker()
        return types.Message_(bot=self.bot, msg=msg)

    def get_sticker_set(self, name, **kwargs):
        return methods.getStickerSet(bot=self.bot, name=name, **kwargs)

    def get_custom_emoji_sticker(self, custom_emoji_ids, **kwargs):
        return methods.getCustomEmojiStickers(bot=self.bot, custom_emoji_ids=custom_emoji_ids, **kwargs)

    def upload_sticker_file(self, user_id, png_sticker, **kwargs):
        if isinstance(user_id, types.User):
            _user_id = user_id.user_id
        elif isinstance(user_id, types.Message):
            _user_id = user_id.user.user_id
        else:
            _user_id = user_id
        return methods.uploadStickerFile(bot=self.bot, user_id=_user_id, png_sticker=png_sticker, **kwargs)

    # Short-Hand-Method for upload_sticker_file.
    def upload_sticker(self, user_id, png_sticker, **kwargs):
        return self.upload_sticker_file(user_id=user_id, png_sticker=png_sticker, **kwargs)

    def create_new_sticker_set(self, user_id, name, title, emojis, png_sticker=None, tgs_sticker=None, webm_sticker=None, sticker_type=None, mask_position=None, **kwargs):
        if isinstance(user_id, types.User):
            _user_id = user_id.user_id
        elif isinstance(user_id, types.Message):
            _user_id = user_id.user.user_id
        else:
            _user_id = user_id
        return methods.createNewStickerSet(bot=self.bot, user_id=user_id, name=name, title=title, emojis=emojis, png_sticker=png_sticker, tgs_sticker=tgs_sticker, webm_sticker=webm_sticker, sticker_type=sticker_type, mask_position=mask_position, **kwargs).create_new_sticker_set()

    def add_sticker_to_set(self, user_id, name, emojis, png_sticker=None, tgs_sticker=None, webm_sticker=None, mask_position=None, **kwargs):
        if isinstance(user_id, types.User):
            _user_id = user_id.user_id
        elif isinstance(user_id, types.Message):
            _user_id = user_id.user.user_id
        else:
            _user_id = user_id
        return methods.addStickerToSet(bot=self.bot, user_id=user_id, name=name, emojis=emojis, png_sticker=png_sticker, tgs_sticker=tgs_sticker, webm_sticker=webm_sticker, mask_position=mask_position, **kwargs).add_sticker_to_set()

    def set_sticker_position_in_set(self, sticker, position, **kwargs):
        return methods.setStickerPositionInSet(bot=self.bot, sticker=sticker, position=position, **kwargs).set_sticker_position_in_set()

    def delete_sticker_from_set(self, sticker, **kwargs):
        return methods.deleteStickerFromSet(bot=self.bot, sticker=sticker, **kwargs).delete_sticker_from_set()

    def set_sticker_set_thumb(self, name, user_id, thumb=None, **kwargs):
        if isinstance(user_id, types.User):
            _user_id = user_id.user_id
        elif isinstance(user_id, types.Message):
            _user_id = user_id.user.user_id
        else:
            _user_id = user_id
        return methods.setStickerSetThumb(bot=self.bot, user_id=_user_id, thumb=thumb, **kwargs).set_sticker_set_thumb()

    # Own created methods.
    def get_permissions(self, chat_id, user_id=None, **kwargs):
        if isinstance(chat_id, types.Chat):
            _chat_id = chat_id.chat_id
        elif isinstance(chat_id, types.Message):
            _chat_id = chat_id.chat.chat_id
        else:
            _chat_id = chat_id
        if isinstance(user_id, types.User):
            _user_id = user_id.user_id
        elif isinstance(user_id, types.Message):
            _user_id = user_id.user.user_id
        else:
            _user_id = user_id
        return methods.getPermissions(bot=self.bot, chat_id=_chat_id, user_id=_user_id, **kwargs).get_permissions()

def signal_handler(signal, frame):
    print('[Bot Api Telegram]: Quiting...')
    sys.exit(0)

signal.signal(signal.SIGINT, signal_handler)

__version__ = '0.0.5'
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