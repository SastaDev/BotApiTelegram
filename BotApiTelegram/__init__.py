# Bot-Api-Telegram || started on 9 October, 2022 at 08:04:55 PM (IST).

import requests
from . import exceptions, types, methods, conversation as conv, database
import functools
import signal
import sys
import os

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
        self.update_on_new_message = []
        self.update_on_added_to_chat = []
        self.update_on_callback_data = []
        self.conversations = []
        self.commands = []
        self.COMMAND_STARTS_WITH = ['/']
        self.parse_mode = 'markdown'
        self.bot_db = database.BotDB(self.bot, database_path)
        if database_path:
            x = self.bot_db.dat_file()
            if x.get('bot_token'):
                self.bot_token = x.get('bot_token')
                self.bot_url = self.bot_url.format(self.bot_token)

    def is_valid_bot_token(self, bot_token):
        if bot_token:
            r = requests_session.get('https://api.telegram.org/bot{}'.format(bot_token) + '/getMe')
        else:
            r = requests_session.get(self.bot_url + '/getMe')
        if r.status_code != 200:
            return False
        else:
            return True

    def get_updates(self, timeout):
        offset = 1
        while self.GetUpdates is True:
            d = {
                'offset': offset,
                'timeout': timeout
            }
            try:
                self.retry = 0
                r = requests_session.get(self.bot_url + '/getUpdates', data=d)
            except requests.exceptions.ConnectionError:
                print('Connection Error: Retrying for {} time.')
            if r.status_code != 200:
                url = r.url
                raise self.check(r.json(), url)
            else:
                result = r.json()['result']
                if result:
                    update = types.Updates(self.bot, result[0])
                    self.send_update(update=update)
                    offset = update.update_id + 1

    def send_update(self, update):
        if update.message:
            cmd = getattr(update.message, 'text', None)
            if cmd:
                if cmd[0] in self.COMMAND_STARTS_WITH:
                    _cmd = cmd[1:].split()
                    for command in self.commands:
                        if command['command'] == _cmd[0]:
                            command['function'](update.message)
                for command in self.commands:
                    if command.get('cmd_type'):
                        if cmd[0] in command['cmd_type']:
                            _cmd = cmd[1:].split()
                            if _cmd:
                                if command['command'] == _cmd[0]:
                                    command['function'](update.message)
            for func in self.update_on_new_message:
                func['function'](update.message)
        if update.my_chat_member:
            my_chat_member = update.my_chat_member
            if getattr(my_chat_member, 'new_chat_member'):
                new_chat_member = getattr(my_chat_member, 'new_chat_member')
                for chat in self.update_on_added_to_chat:
                    if chat['chats'] == my_chat_member.chat.chat_id or chat['chats'] == my_chat_member.chat.username or chat['chats'] is True:
                        old = my_chat_member.old_chat_member.chat_member
                        if old['status'] == 'left':
                            chat['function'](types.Message_(self.bot, types.BotAdded(update.my_chat_member)))
                for chat in self.update_on_chat_join:
                    if chat['chats'] == my_chat_member.chat.chat_id or chat['chats'] == my_chat_member.chat.username or chat['chats'] is True:
                        old = my_chat_member.old_chat_member.chat_member
                        if old['status'] == 'left':
                            chat['function'](types.Message_(self.bot, types.ChatJoined(update.my_chat_member)))
        if update.callback_query:
            callback_query = update.callback_query
            for i in self.update_on_callback_data:
                for j in i['data']:
                    if j is True or j == callback_query.data:
                        i['function'](types.CallbackQuery_(self.bot, callback_query))

        # Conversation
        if update.message:
            if update.message.chat:
                for c in self.conversations:
                    chat = update.message.chat.chat_id
                    if c['chat_id'] == chat:
                        co = self.conversation(self.bot, chat)
                        print('appending')
                        co.append_update(update.message)

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
            raise exceptions.NoAdministratorsInPrivateChat()
        raise exceptions.UnKnownError(des)

    def add_command(self, command, function, cmd_type=[]):
        data = {
            'command': command,
            'function': function,
            'cmd_type': cmd_type
        }
        self.commands.append(data)

    def add_callback_data(self, data, function):
        data_ = {
            'data': data,
            'function': function
        }
        self.update_on_callback_data.append(data_)

    def on_update(self, func=None, command=None, new_message=False, added_to_chat=False, callback_data=False):
        @functools.wraps(func)
        def _on(func, command=command, new_message=new_message, added_to_chat=added_to_chat, callback_data=callback_data):
            if new_message is not False:
                if not isinstance(new_message, list):
                    new_message = [new_message]
                for chat in new_message:
                    self.update_on_new_message.append({
                        'chats': chat,
                        'function': func
                    })
            if command:
                if not isinstance(command, list):
                    command = [command]
                for cmd in command:
                    self.commands.append({
                        'command': cmd,
                        'function': func
                    })
            if added_to_chat is not False:
                if not isinstance(added_to_chat, list):
                    added_to_chat = [added_to_chat]
                for chat in added_to_chat:
                    if added_to_chat is True:
                        self.update_on_added_to_chat.append({
                            'chats': True,
                            'function': func
                        })
                    else:
                        self.update_on_added_to_chat.append({
                            'chats': added_to_chat,
                            'function': func
                        })
            if callback_data is not False:
                if not isinstance(callback_data, list):
                    callback_data = [callback_data]
                for chat in callback_data:
                    if callback_data is True:
                        self.update_on_callback_data.append({
                            'data': True,
                            'function': func
                        })
                    else:
                        self.update_on_callback_data.append({
                            'data': callback_data,
                            'function': func
                        })
        return _on

    def start_polling(self, timeout=60):
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
        self.get_updates(timeout=timeout)

    def get_me(self):
        return methods.getMe(self.bot).get_me()

    def conversation(self, chat, update=None):
        c = conv.Conversation(self.bot, chat)
        if update is not None:
            c.append_update(update)
        return c

    def send_message(self, chat_id, text, buttons=None, reply_to=None, link_preview=True, parse_mode=None, *args, **kwargs):
        if parse_mode is None:
            parse_mode = self.parse_mode
        if isinstance(chat_id, types.Chat):
            _chat_id = chat_id.chat_id
        elif isinstance(chat_id, types.Message):
            _chat_id = chat_id.chat.chat_id
        elif str(chat_id)[0] == '@':
            try:
                _chat_id = methods.getChat(chat_id).user_id
            except:
                _chat_id = chat_id
        else:
            _chat_id = chat_id
        msg = methods.sendMessage(self.bot, chat_id=_chat_id, text=text, buttons=buttons, reply_to=reply_to, link_preview=link_preview, parse_mode=parse_mode, *args, **kwargs).send_message()
        return types.Message_(self.bot, msg)

    def edit_message(self, chat_id, text, buttons=None, link_preview=True, parse_mode=None, *args, **kwargs):
        if parse_mode is None:
            parse_mode = self.parse_mode
        if isinstance(chat_id, types.Chat):
            _chat_id = chat_id.chat_id
        elif isinstance(chat_id, types.Message):
            _chat_id = chat_id.chat.chat_id
        elif str(chat_id)[0] == '@':
            _chat_id = methods.getChat(chat_id)
        else:
            _chat_id = chat_id
        msg = methods.editMessageText(self.bot, chat_id=_chat_id, text=text, buttons=buttons, link_preview=link_preview, parse_mode=parse_mode, *args, **kwargs).edit_message()
        return types.Message_(self.bot, msg)

    def delete_message(self, chat_id, message_id):
        if isinstance(chat_id, types.Chat):
            _chat_id = chat_id.chat_id
        elif isinstance(chat_id, types.Message):
            _chat_id = chat_id.chat.chat_id
        elif str(chat_id)[0] == '@':
            _chat_id = methods.getChat(chat_id)
        else:
            _chat_id = chat_id
        if isinstance(message_id, list):
            success = []
            for msg_id in message_id:
                d = methods.deleteMessage(self.bot, chat_id=_chat_id, message_id=msg_id).delete_message()
                success.append(d)
            return d
        else:
            return methods.deleteMessage(self.bot, chat_id=_chat_id, message_id=message_id).delete_message()

    def answer_callback_query(self, callback_query_id, text, show_alert=False, url=None, cache_time=0):
        return methods.answerCallbackQuery(
            self.bot,
            callback_query_id=callback_query_id,
            text=text,
            show_alert=show_alert,
            url=url,
            cache_time=cache_time
            ).answer_callback_query()

    def get_chat(self, chat_id):
        if isinstance(chat_id, types.Chat):
            _chat_id = chat_id.chat_id
        elif isinstance(chat_id, types.Message):
            _chat_id = chat_id.chat.chat_id
        elif str(chat_id)[0] == '@':
            _chat_id = chat_id[1:]
        return methods.getChat(self.bot, _chat_id).get_chat()

    def get_chat_administrators(self, chat_id):
        if isinstance(chat_id, types.Chat):
            _chat_id = chat_id.chat_id
        elif isinstance(chat_id, types.Message):
            _chat_id = chat_id.chat.chat_id
        elif str(chat_id)[0] == '@':
            _chat_id = chat_id[1:]
        return getattr(methods.getChatAdministrators(self.bot, _chat_id).get_chat_administrators(), 'chat_member', None)

    # Short-Hand-Method for get_chat_administrators(self, chat_id).
    def getAdmins(self, chat_id):
        return self.get_chat_administrators(chat_id)

def signal_handler(signal, frame):
    print('[Bot Api Telegram]: Quiting...')
    sys.exit(0)

signal.signal(signal.SIGINT, signal_handler)

__version__ = '0.0.1'
__credits__ = '(Copyright) Sasta Dev.'
__docs__ = '''
Telegram Updates Channel: @BotApiTelegram.
Telegram Help Support Chat: @BotApiTelegramChat.
'''