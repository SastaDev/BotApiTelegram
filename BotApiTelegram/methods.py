from . import types
import requests
import json

requests_session = requests.Session()

def parse_buttons(buttons):
    try:
        buttons[0][0]
    except:
        buttons = [buttons]
    return buttons

def parse_url(url):
    query = requests.utils.urlparse(url).query
    params = dict(x.split('=') for x in query.split('&'))
    return params


class getMe:
    def __init__(self, bot):
        bot_token = bot.bot_token
        url = bot.bot_url + '/getMe'
        r = requests_session.get(url)
        if r.status_code != 200:
            bot.check(r.json(), url)
        else:
            self.result = types.getMe(r.json()['result'])

    def get_me(self):
        return self.result

    def __repr__(self):
        msg = self.result
        return str(msg)

class sendMessage:
    def __init__(self, bot, chat_id, text, buttons=None, reply_to=None, link_preview=True, parse_mode='markdown', **kwargs):
        self.bot = bot
        self.chat_id = chat_id
        self.text = text
        self.buttons = buttons
        self.reply_to = reply_to
        self.link_preview = link_preview
        self.parse_mode = parse_mode
        self.extra = kwargs

    def send_message(self):
        url = '/sendMessage?chat_id={}&text={}'.format(self.chat_id, self.text)
        if self.buttons:
            btns = parse_buttons(self.buttons)
            btns = json.dumps({"inline_keyboard": btns})
            url += '&reply_markup={}'.format(btns)
        if self.reply_to:
            url += '&reply_to_message_id={}'.format(self.reply_to)
        if self.link_preview:
            url += '&disable_web_page_preview={}'.format(self.link_preview)
        if self.parse_mode:
            url += '&parse_mode={}'.format(self.parse_mode)
        r = requests_session.get(self.bot.bot_url + url, params=self.extra)
        if r.status_code != 200:
            self.bot.check(r.json(), url)
        else:
            self.result = types.Message(self.bot, r.json()['result'])
            return self.result

    def __repr__(self):
        msg = self.result
        return str(msg)

class editMessageText:
    def __init__(self, bot, chat_id, message_id, text, link_preview=True, parse_mode='markdown', **kwargs):
        self.bot = bot
        self.chat_id = chat_id
        self.message_id = message_id
        self.text = text
        self.link_preview = link_preview
        self.parse_mode = parse_mode
        self.extra = kwargs

    def edit_message(self):
        url = '/editMessageText?chat_id={}&message_id={}&text={}'.format(self.chat_id, self.message_id, self.text)
        if self.link_preview:
            url += '&disable_web_page_preview={}'.format(self.link_preview)
        if self.parse_mode:
            url += '&parse_mode={}'.format(self.parse_mode)
        r = requests_session.get(self.bot.bot_url + url, params=self.extra)
        if r.status_code != 200:
            self.bot.check(r.json(), url)
        else:
            self.result = types.Message(self.bot, r.json()['result'])
            return self.result

    def __repr__(self):
        msg = self.result
        return str(msg)

class deleteMessage:
    def __init__(self, bot, chat_id, message_id):
        self.bot = bot
        self.chat_id = chat_id
        self.message_id = message_id

    def delete_message(self):
        url = '/deleteMessage?chat_id={}&message_id={}'.format(self.chat_id, self.message_id)
        r = requests_session.get(self.bot.bot_url + url)
        if r.status_code != 200:
            self.bot.check(r.json(), url)
        else:
            return r.json().get('result')

    def __repr__(self):
        msg = self.result
        return str(msg)

class answerCallbackQuery:
    def __init__(self, bot, callback_query_id, text, show_alert, url, cache_time):
        self.bot = bot
        self.callback_query_id = callback_query_id
        self.text = text
        self.show_alert = show_alert
        self.url = url
        self.cache_time = cache_time

    def answer_callback_query(self):
        url = '/answerCallbackQuery?callback_query_id={}&text={}'.format(self.callback_query_id, self.text)
        if self.show_alert:
            url += '&show_alert={}'.format(self.show_alert)
        if self.url:
            url += '&url={}'.format(self.url)
        if self.cache_time:
            url += '&cache_time={}'.format(self.cache_time)
        r = requests_session.get(self.bot.bot_url + url)
        if r.status_code != 200:
            self.bot.check(r.json(), url)
        else:
            return r.json().get('result')

    def __repr__(self):
        msg = self.msg.__dict__
        return str(msg)

class getChat:
    def __init__(self, bot, chat_id):
        self.bot = bot
        self.chat_id = chat_id

    def get_chat(self):
        url = '/getChat?chat_id={}'.format(self.chat_id)
        r = requests_session.get(self.bot.bot_url + url)
        if r.status_code != 200:
            self.bot.check(r.json(), url)
        else:
            self.result = types.Chat(r.json()['result'])
            return self.result

    def __repr__(self):
        msg = self.result
        return str(msg)

class getChatAdministrators:
    def __init__(self, bot, chat_id):
        self.bot = bot
        self.chat_id = chat_id

    def get_chat_administrators(self):
        url = '/getChatAdministrators?chat_id={}'.format(self.chat_id)
        r = requests_session.get(self.bot.bot_url + url)
        if r.status_code != 200:
            self.bot.check(r.json(), url)
        else:
            self.result = types.ChatMember(r.json()['result'])
            return self.result

    def __repr__(self):
        msg = self.result
        return str(msg)