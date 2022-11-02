from . import types
import requests
import json

requests_session = requests.Session()

def parse_buttons(buttons):
    try:
        buttons[0][0]
        btns = buttons
    except:
        btns = [buttons]
    if isinstance(buttons, list):
        b = buttons[0]
        if isinstance(b, list):
            b = b[0]
    x = b.get('_')
    if x == 'inline_keyboard':
        c = {
            'inline_keyboard': btns
        }
    elif x == 'keyboard':
        c = {
            'keyboard': btns
        }
    else:
        c = None
    return c

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
            self.result = types.getMe(r.json().get('result'))

    def get_me(self):
        return self.result

    def __repr__(self):
        msg = self.result
        return str(msg)

class sendMessage:
    def __init__(self, bot, chat_id, text, parse_mode=None, entities=None, disable_web_page_preview=None, disable_notification=None, protect_content=None, reply_to_message_id=None, allow_sending_without_reply=None, reply_markup=None, **kwargs):
        self.bot = bot
        self.chat_id = chat_id
        self.text = text
        self.parse_mode = parse_mode
        self.entities = entities
        self.disable_web_page_preview = disable_web_page_preview
        self.protect_content = protect_content
        self.reply_to_message_id = reply_to_message_id
        self.allow_sending_without_reply = allow_sending_without_reply
        self.reply_markup = reply_markup
        self.extra = kwargs

    def send_message(self):
        url = '/sendMessage?chat_id={}&text={}'.format(self.chat_id, self.text)
        if self.parse_mode:
            url += '&parse_mode={}'.format(self.parse_mode)
        if self.entities:
            url += '&entities={}'.format(entities)
        if self.disable_web_page_preview:
            url += '&disable_web_page_preview={}'.format(self.disable_web_page_preview)
        if self.protect_content:
            url += '&protect_content={}'.format(self.protect_content)
        if self.reply_to_message_id:
            url += '&reply_to_message_id={}'.format(self.reply_to_message_id)
        if self.allow_sending_without_reply:
            url += '&allow_sending_without_reply={}'.format(self.allow_sending_without_reply)
        if self.reply_markup:
            btns = parse_buttons(self.reply_markup)
            btns = json.dumps(btns)
            url += '&reply_markup={}'.format(btns)
        r = requests_session.get(self.bot.bot_url + url, params=self.extra)
        if r.status_code != 200:
            self.bot.check(r.json(), url)
        else:
            self.result = types.Message(r.json().get('result'))
            return self.result

    def __repr__(self):
        msg = self.result
        return str(msg)

class forwardMessage:
    def __init__(self, bot, chat_id, from_chat_id, message_id, disable_notification=None, protect_content=None, *kwargs):
        self.bot = bot
        self.chat_id = chat_id
        self.from_chat_id = from_chat_id
        self.disable_notification = disable_notification
        self.protect_content = protect_content
        self.message_id = message_id
        self.extra = kwargs

    def forward_message(self):
        url = '/forwardMessage?chat_id={}&from_chat_id={}&message_id={}'.format(self.chat_id, self.from_chat_id, self.message_id)
        if self.disable_notification:
            url += '&disable_notification={}'.format(self.disable_notification)
        if self.protect_content:
            url += '&protect_content={}'.format(self.protect_content)
        r = requests_session.get(self.bot.bot_url + url, params=self.extra)
        if r.status_code != 200:
            self.bot.check(r.json(), url)
        else:
            self.result = types.Message(r.json().get('result'))
            return self.result

    def __repr__(self):
        msg = self.__dict__
        return str(msg)

class copyMessage:
    def __init__(self, bot, chat_id, from_chat_id, message_id, caption=None, parse_mode=None, caption_entities=None, disable_notification=None, protect_content=None, reply_to_message_id=None, allow_sending_without_reply=None, reply_markup=None, *kwargs):
        self.bot = bot
        self.chat_id = chat_id
        self.from_chat_id = from_chat_id
        self.message_id = message_id
        self.caption = caption
        self.parse_mode = parse_mode
        self.caption_entities = caption_entities
        self.disable_notification = disable_notification
        self.protect_content = protect_content
        self.reply_to_message_id = reply_to_message_id or reply_to
        self.allow_sending_without_reply = allow_sending_without_reply
        self.reply_markup = reply_markup
        self.extra = kwargs

    def copy_message(self):
        url = '/copyMessage&chat_id={}&from_chat_id={}&message_id={}'.format(self.chat_id, self.from_chat_id, self.message_id)
        if self.caption:
            url += '&caption={}'.format(self.caption)
        if self.parse_mode:
            url += '&parse_mode={}'.format(self.parse_mode)
        if self.caption_entities:
            url += '&caption_entities={}'.format(self.caption_entities)
        if self.disable_notification:
            url += '&disable_notification={}'.format(self.disable_notification)
        if self.protect_content:
            url += '&protect_content={}'.format(self.protect_content)
        if self.reply_to_message_id:
            url += '&reply_to_message_id={}'.format(self.reply_to_message_id)
        if self.allow_sending_without_reply:
            url += '&allow_sending_without_reply={}'.format(self.allow_sending_without_reply)
        if self.reply_markup:
            btns = parse_buttons(self.reply_markup)
            btns = json.dumps(btns)
            url += '&reply_markup={}'.format(btns)
        r = requests_session.get(self.bot.bot_url + url, params=self.extra)
        if r.status_code != 200:
            self.bot.check(r.json(), url)
        else:
            self.result = types(r.json().get('result'))
            return self.result

    def __repr__(self):
        msg = self.__dict__
        return str(msg)

class sendPhoto:
    def __init__(self, bot, chat_id, photo, caption=None, parse_mode=None, caption_entities=None, disable_notification=None, protect_content=None, reply_to_message_id=None, allow_sending_without_reply=None, reply_markup=None, **kwargs):
        self.bot = bot
        self.chat_id = chat_id
        self.photo = photo
        self.caption = caption
        self.parse_mode = parse_mode
        self.caption_entities = caption_entities
        self.disable_notification = disable_notification
        self.protect_content = protect_content
        self.reply_to_message_id = reply_to_message_id or reply_to
        self.allow_sending_without_reply = allow_sending_without_reply
        self.reply_markup = reply_markup
        self.extra = kwargs

    def send_photo(self):
        url = '/sendPhoto?chat_id={}&photo={}'.format(self.chat_id, self.photo)
        if self.caption:
            url += '&caption={}'.format(self.caption)
        if self.parse_mode:
            url += '&parse_mode={}'.format(self.parse_mode)
        if self.caption_entities:
            url += '&caption_entities={}'.format(self.caption_entities)
        if self.disable_notification:
            url += '&disable_notification={}'.format(self.disable_notification)
        if self.protect_content:
            url += '&protect_content={}'.format(self.protect_content)
        if self.reply_to_message_id:
            url += '&reply_to_message_id={}'.format(self.reply_to_message_id)
        if self.allow_sending_without_reply:
            url += '&allow_sending_without_reply={}'.format(self.allow_sending_without_reply)
        if self.reply_markup:
            btns = parse_buttons(self.reply_markup)
            btns = json.dumps(btns)
            url += '&reply_markup={}'.format(btns)
        r = requests_session.get(self.bot.bot_url + url, params=self.extra)
        if r.status_code != 200:
            self.bot.check(r.json(), url)
        else:
            self.result = types.Message(r.json().get('result'))
            return self.result

    def __repr__(self):
        msg = self.__dict__
        return str(msg)

class sendVideo:
    def __init__(self, bot, chat_id, video, duration=None, width=None, height=None, caption=None, parse_mode=None, caption_entities=None, supports_streaming=None, disable_notification=None, protect_content=None, reply_to_message_id=None, allow_sending_without_reply=None, reply_markup=None, **kwargs):
        self.bot = bot
        self.chat_id = chat_id
        self.video = video
        self.duration = duration
        self.width = width
        self.height = height
        self.caption = caption
        self.parse_mode = parse_mode
        self.caption_entities = caption_entities
        self.supports_streaming = supports_streaming
        self.disable_notification = disable_notification
        self.protect_content = protect_content
        self.reply_to_message_id = reply_to_message_id or reply_to
        self.allow_sending_without_reply = allow_sending_without_reply
        self.reply_markup = reply_markup
        self.extra = kwargs

    def send_video(self):
        url = '/sendVideo?chat_id={}&video={}'.format(self.chat_id, self.video)
        if self.duration:
            url += '&duration={}'.format(self.duration)
        if self.width:
            url += '&width={}'.format(self.width)
        if self.height:
            url += '&height={}'.format(self.height)
        if self.caption:
            url += '&caption={}'.format(self.caption)
        if self.parse_mode:
            url += '&parse_mode={}'.format(self.parse_mode)
        if self.caption_entities:
            url += '&caption_entities={}'.format(self.caption_entities)
        if self.supports_streaming:
            url += '&supports_streaming={}'.format(self.supports_streaming)
        if self.disable_notification:
            url += '&disable_notification={}'.format(self.disable_notification)
        if self.protect_content:
            url += '&protect_content={}'.format(self.protect_content)
        if self.reply_to_message_id:
            url += '&reply_to_message_id={}'.format(self.reply_to_message_id)
        if self.allow_sending_without_reply:
            url += '&allow_sending_without_reply={}'.format(self.allow_sending_without_reply)
        if self.reply_markup:
            btns = parse_buttons(self.reply_markup)
            btns = json.dumps(btns)
            url += '&reply_markup={}'.format(btns)
        r = requests_session.get(self.bot.bot_url + url, params=self.extra)
        if r.status_code != 200:
            self.bot.check(r.json(), url)
        else:
            self.result = types.Message(r.json().get('result'))
            return self.result

    def __repr__(self):
        msg = self.__dict__
        return str(msg)

class sendAudio:
    def __init__(self, bot, chat_id, audio, caption=None, parse_mode=None, caption_entities=None, duration=None, performer=None, title=None, thumb=None, disable_notification=None, protect_content=None, reply_to_message_id=None, allow_sending_without_reply=None, reply_markup=None, **kwargs):
        self.bot = bot
        self.chat_id = chat_id
        self.photo = photo
        self.caption = caption
        self.parse_mode = parse_mode
        self.caption_entities = caption_entities
        self.duration = duration
        self.performer = performer
        self.title = title
        self.thumb = thumb
        self.disable_notification = disable_notification
        self.protect_content = protect_content
        self.reply_to_message_id = reply_to_message_id
        self.allow_sending_without_reply = allow_sending_without_reply
        self.reply_markup = reply_markup
        self.extra = kwargs

    def send_audio(self):
        url = '/sendAudio?chat_id={}&audio={}'.format(self.chat_id, self.audio)
        if self.caption:
            url += '&caption={}'.format(self.caption)
        if self.parse_mode:
            url += '&parse_mode={}'.format(self.parse_mode)
        if self.caption_entities:
            url += '&caption_entities={}'.format(self.caption_entities)
        if self.duration:
            url += '&duration={}'.format(self.duration)
        if self.performer:
            url += '&performer={}'.format(self.performer)
        if self.title:
            url += '&title={}'.format(self.title)
        if self.thumb:
            url += '&thumb={}'.format(self.thumb)
        if self.disable_notification:
            url += '&disable_notification={}'.format(self.disable_notification)
        if self.protect_content:
            url += '&protect_content={}'.format(self.protect_content)
        if self.reply_to_message_id:
            url += '&reply_to_message_id={}'.format(self.reply_to_message_id)
        if self.allow_sending_without_reply:
            url += '&allow_sending_without_reply={}'.format(self.allow_sending_without_reply)
        if self.reply_markup:
            btns = parse_buttons(self.reply_markup)
            btns = json.dumps(btns)
            url += '&reply_markup={}'.format(btns)
        r = requests_session.get(self.bot.bot_url + url, params=self.extra)
        if r.status_code != 200:
            self.bot.check(r.json(), url)
        else:
            self.result = types.Message(r.json().get('result'))
            return self.result

    def __repr__(self):
        msg = self.__dict__
        return str(msg)

class sendDocument:
    def __init__(self, bot, chat_id, document, thumb=None, caption=None, parse_mode=None, caption_entities=None, disable_content_type_detection=None, disable_notification=None, protect_content=None, reply_to_message_id=None, allow_sending_without_reply=None, reply_markup=None, **kwargs):
        self.bot = bot
        self.chat_id = chat_id
        self.document = document
        self.thumb = thumb
        self.caption = caption
        self.parse_mode = parse_mode
        self.caption_entities = caption_entities
        self.disable_content_type_detection = disable_content_type_detection
        self.disable_notification = disable_notification
        self.protect_content = protect_content
        self.reply_to_message_id = reply_to_message_id
        self.allow_sending_without_reply = allow_sending_without_reply
        self.reply_markup = reply_markup
        self.extra = kwargs

    def send_document(self):
        url = '/sendDocument?chat_id={}&document={}'.format(self.chat_id, self.audio)
        if self.thumb:
            url += '&thumb={}'.format(self.thumb)
        if self.caption:
            url += '&caption={}'.format(self.caption)
        if self.parse_mode:
            url += '&parse_mode={}'.format(self.parse_mode)
        if self.caption_entities:
            url += '&caption_entities={}'.format(self.caption_entities)
        if url.disable_content_type_detection:
            url += '&disable_content_type_detection'.format(self.disable_content_type_detection)
        if self.disable_notification:
            url += '&disable_notification={}'.format(self.disable_notification)
        if self.protect_content:
            url += '&protect_content={}'.format(self.protect_content)
        if self.reply_to_message_id:
            url += '&reply_to_message_id={}'.format(self.reply_to_message_id)
        if self.allow_sending_without_reply:
            url += '&allow_sending_without_reply={}'.format(self.allow_sending_without_reply)
        if self.reply_markup:
            btns = parse_buttons(self.reply_markup)
            btns = json.dumps(btns)
            url += '&reply_markup={}'.format(btns)
        r = requests_session.get(self.bot.bot_url + url, params=self.extra)
        if r.status_code != 200:
            self.bot.check(r.json(), url)
        else:
            self.result = types.Message(r.json().get('result'))
            return self.result

    def __repr__(self):
        msg = self.__dict__
        return str(msg)

class sendAnimation:
    def __init__(self, bot, chat_id, animation, width=None, height=None, thumb=None, caption=None, parse_mode=None, caption_entities=None, disable_notification=None, protect_content=None, reply_to_message_id=None, allow_sending_without_reply=None, reply_markup=None, **kwargs):
        self.bot = bot
        self.chat_id = chat_id
        self.animation = animation
        self.width = width
        self.height = height
        self.thumb = thumb
        self.caption = caption
        self.parse_mode = parse_mode
        self.caption_entities = caption_entities
        self.disable_notification = disable_notification
        self.protect_content = protect_content
        self.reply_to_message_id = reply_to_message_id
        self.allow_sending_without_reply = allow_sending_without_reply
        self.reply_markup = reply_markup
        self.extra = kwargs

    def send_animation(self):
        url = '/sendAnimation?chat_id={}&animation={}'.format(self.chat_id, self.animation)
        if self.width:
            url += '&width={}'.format(self.width)
        if self.height:
            url += '&height={}'.format(self.height)
        if self.thumb:
            url += '&thumb={}'.format(self.thumb)
        if self.caption:
            url += '&caption={}'.format(self.caption)
        if self.parse_mode:
            url += '&parse_mode={}'.format(self.parse_mode)
        if self.caption_entities:
            url += '&caption_entities={}'.format(self.caption_entities)
        if self.disable_notification:
            url += '&disable_notification={}'.format(self.disable_notification)
        if self.protect_content:
            url += '&protect_content={}'.format(self.protect_content)
        if self.reply_to_message_id:
            url += '&reply_to_message_id={}'.format(self.reply_to_message_id)
        if self.allow_sending_without_reply:
            url += '&allow_sending_without_reply={}'.format(self.allow_sending_without_reply)
        if self.reply_markup:
            btns = parse_buttons(self.reply_markup)
            btns = json.dumps(btns)
            url += '&reply_markup={}'.format(btns)
        r = requests_session.get(self.bot.bot_url + url, params=self.extra)
        if r.status_code != 200:
            self.bot.check(r.json(), url)
        else:
            self.result = types.Message(r.json().get('result'))
            return self.result

    def __repr__(self):
        msg = self.__dict__
        return str(msg)

class sendVoice:
    def __init__(self, bot, chat_id, voice, caption=None, parse_mode=None, caption_entities=None, duration=None, disable_notification=None, protect_content=None, reply_to_message_id=None, allow_sending_without_reply=None, reply_markup=None, **kwargs):
        self.bot = bot
        self.chat_id = chat_id
        self.voice = voice
        self.caption = caption
        self.parse_mode = parse_mode
        self.caption_entities = caption_entities
        self.duration = duration
        self.disable_notification = disable_notification
        self.protect_content = protect_content
        self.reply_to_message_id = reply_to_message_id
        self.allow_sending_without_reply = allow_sending_without_reply
        self.reply_markup = reply_markup
        self.extra = kwargs

    def send_voice(self):
        url = '/sendVoice?chat_id={}&voice={}'.format(self.chat_id, self.animation)
        if self.caption:
            url += '&caption={}'.format(self.caption)
        if self.parse_mode:
            url += '&parse_mode={}'.format(self.parse_mode)
        if self.caption_entities:
            url += '&caption_entities={}'.format(self.caption_entities)
        if self.duration:
            url += '&duration={}'.format(self.duration)
        if self.disable_notification:
            url += '&disable_notification={}'.format(self.disable_notification)
        if self.protect_content:
            url += '&protect_content={}'.format(self.protect_content)
        if self.reply_to_message_id:
            url += '&reply_to_message_id={}'.format(self.reply_to_message_id)
        if self.allow_sending_without_reply:
            url += '&allow_sending_without_reply={}'.format(self.allow_sending_without_reply)
        if self.reply_markup:
            btns = parse_buttons(self.reply_markup)
            btns = json.dumps(btns)
            url += '&reply_markup={}'.format(btns)
        r = requests_session.get(self.bot.bot_url + url, params=self.extra)
        if r.status_code != 200:
            self.bot.check(r.json(), url)
        else:
            self.result = types.Message(r.json().get('result'))
            return self.result

    def __repr__(self):
        msg = self.__dict__
        return str(msg)

class sendVideoNote:
    def __init__(self, bot, chat_id, video_note, duration=None, length=None, disable_notification=None, protect_content=None, reply_to_message_id=None, allow_sending_without_reply=None, reply_markup=None, **kwargs):
        self.bot = bot
        self.chat_id = chat_id
        self.video_note = video_note
        self.duration = duration
        self.length = length
        self.disable_notification = disable_notification
        self.protect_content = protect_content
        self.reply_to_message_id = reply_to_message_id or reply_to
        self.allow_sending_without_reply = allow_sending_without_reply
        self.reply_markup = reply_markup
        self.extra = kwargs

    def send_video_note(self):
        url = '/sendVideoNote?chat_id={}&video_note={}'.format(self.chat_id, self.video_note)
        if self.duration:
            url += '&duration={}'.format(self.duration)
        if self.length:
            url += '&length={}'.format(self.length)
        if self.disable_notification:
            url += '&disable_notification={}'.format(self.disable_notification)
        if self.protect_content:
            url += '&protect_content={}'.format(self.protect_content)
        if self.reply_to_message_id:
            url += '&reply_to_message_id={}'.format(self.reply_to_message_id)
        if self.allow_sending_without_reply:
            url += '&allow_sending_without_reply={}'.format(self.allow_sending_without_reply)
        if self.reply_markup:
            btns = parse_buttons(self.reply_markup)
            btns = json.dumps(btns)
            url += '&reply_markup={}'.format(btns)
        r = requests_session.get(self.bot.bot_url + url, params=self.extra)
        if r.status_code != 200:
            self.bot.check(r.json(), url)
        else:
            self.result = types.Message(r.json().get('result'))
            return self.result

    def __repr__(self):
        msg = self.__dict__
        return str(msg)

class sendMediaGroup:
    def __init__(self, bot, chat_id, media, disable_notification=None, protect_content=None, reply_to_message_id=None, allow_sending_without_reply=None, **kwargs):
        self.bot = bot
        self.chat_id = chat_id
        self.media = media
        self.disable_notification = disable_notification
        self.protect_content = protect_content
        self.reply_to_message_id = reply_to_message_id
        self.allow_sending_without_reply = allow_sending_without_reply
        self.extra = kwargs

    def send_media_group(self):
        url = '/sendMediaGroup?chat_id={}&media={}'.format(self.chat_id, self.media)
        if self.disable_notification:
            url += '&disable_notification={}'.format(self.disable_notification)
        if self.protect_content:
            url += '&protect_content={}'.format(self.protect_content)
        if self.reply_to_message_id:
            url += '&reply_to_message_id={}'.format(self.reply_to_message_id)
        if self.allow_sending_without_reply:
            url += '&allow_sending_without_reply={}'.format(self.allow_sending_without_reply)
        r = requests_session.get(self.bot.bot_url + url, params=self.extra)
        if r.status_code != 200:
            self.bot.check(r.json(), url)
        else:
            self.result = types.Message(r.json().get('result'))
            return self.result

    def __repr__(self):
        msg = self.__dict__
        return str(msg)

class sendLocation:
    def __init__(self, bot, chat_id, latitude, longitude, horizontal_accuracy=None, live_period=None, heading=None, proximity_alert_radius=None, disable_notification=None, protect_content=None, reply_to_message_id=None, allow_sending_without_reply=None, reply_markup=None, *kwargs):
        self.bot = bot
        self.chat_id = chat_id
        self.latitude = latitude
        self.longitude = longitude
        self.horizontal_accuracy = horizontal_accuracy
        self.live_period = live_period
        self.heading = heading
        self.proximity_alert_radius = proximity_alert_radius
        self.disable_notification = disable_notification
        self.protect_content = protect_content
        self.reply_to_message_id = reply_to_message_id
        self.allow_sending_without_reply = allow_sending_without_reply
        self.reply_markup = reply_markup
        self.extra = kwargs

    def send_location(self):
        url = '/sendLocation?chat_id={}&latitude={}&longitude={}'.format(self.chat_id, self.latitude, self.longitude)
        if self.horizontal_accuracy:
            url += '&horizontal_accuracy={}'.format(self.horizontal_accuracy)
        if self.live_period:
            url += '&live_period={}'.format(self.live_period)
        if self.heading:
            url += '&heading={}'.format(self.heading)
        if self.proximity_alert_radius:
            url += '&proximity_alert_radius={}'.format(self.proximity_alert_radius)
        if self.disable_notification:
            url += '&disable_notification={}'.format(self.disable_notification)
        if self.protect_content:
            url += '&protect_content={}'.format(self.protect_content)
        if self.reply_to_message_id:
            url += '&reply_to_message_id={}'.format(self.reply_to_message_id)
        if self.allow_sending_without_reply:
            url += '&allow_sending_without_reply={}'.format(self.allow_sending_without_reply)
        if self.reply_markup:
            btns = parse_buttons(self.reply_markup)
            btns = json.dumps(btns)
            url += '&reply_markup={}'.format(btns)
        r = requests_session.get(self.bot.bot_url + url, params=self.extra)
        if r.status_code != 200:
            self.bot.check(r.json(), url)
        else:
            self.result = types.Message_(r.json().get('result'))
            return self.result

    def __repr__(self):
        msg = self.__dict__
        return str(msg)

class editMessageLiveLocation:
    def __init__(self, bot, latitude, longitude, chat_id=None, message_id=None, inline_message_id=None, horizontal_accuracy=None, heading=None, proximity_alert_radius=None, reply_markup=None, **kwargs):
        self.chat_id = chat_id
        self.message_id = message_id
        self.inline_message_id = inline_message_id
        self.latitude = latitude
        self.longitude = longitude
        self.horizontal_accuracy = horizontal_accuracy
        self.heading = heading
        self.proximity_alert_radius = proximity_alert_radius
        self.reply_markup = reply_markup
        self.extra = kwargs

    def edit_message_live_location(self):
        url = '/editMessageLiveLocation?latitude={}&longitude={}'.format(self.latitude, self.longitude)
        if self.chat_id:
            url += '&chat_id={}'.format(self.chat_id)
        if self.message_id:
            url += '&message_id={}'.format(self.message_id)
        if self.inline_message_id:
            url += '&inline_message_id={}'.format(self.inline_message_id)
        if self.horizontal_accuracy:
            url += '&horizontal_accuracy={}'.format(self.horizontal_accuracy)
        if self.heading:
            url += '&heading={}'.format(self.heading)
        if self.proximity_alert_radius:
            url += '&proximity_alert_radius={}'.format(self.proximity_alert_radius)
        if self.reply_markup:
            btns = parse_buttons(self.reply_markup)
            btns = json.dumps(btns)
            url += '&reply_markup={}'.format(btns)
        r = requests_session.get(self.bot.bot_url + url, params=self.extra)
        if r.status_code != 200:
            self.bot.check(r.json(), url)
        else:
            self.result = types.Message(r.json().get('result'))
            return self.result

    def __repr__(self):
        msg = self.__dict__
        return str(msg)

class stopMessageLiveLocation:
    def __init__(self, bot, chat_id=None, message_id=None, inline_message_id=None, reply_markup=None, *kwargs):
        self.bot = bot
        self.chat_id = chat_id
        self.message_id = message_id
        self.inline_message_id = inline_message_id
        self.reply_markup = reply_markup
        self.extra = kwargs

    def stop_message_live_location(self):
        url = '/stopMessageLiveLocation'
        if self.chat_id:
            url += '&chat_id={}'.format(self.chat_id)
        if self.message_id:
            url += '&message_id={}'.format(self.message_id)
        if self.inline_message_id:
            url += '&inline_message_id={}'.format(self.inline_message_id)
        if self.reply_markup:
            btns = parse_buttons(self.reply_markup)
            btns = json.dumps(btns)
            url += '&reply_markup={}'.format(btns)
        r = requests_session.get(self.bot.bot_url + url, params=self.extra)
        if r.status_code != 200:
            self.bot.check(r.json(), url)
        else:
            self.result = r.json().get('result')
            if self.result is True:
                return self.result
            else:
                return types.Message(self.result)

    def __repr__(self):
        msg = self.__dict__
        return str(msg)

class sendVenue:
    def __init__(self, bot, chat_id, latitude, longitude, title, address, foursquare_id=None, foursquare_type=None, google_place_id=None, google_place_type=None, disable_notification=None, protect_content=None, reply_to_message_id=None, allow_sending_without_reply=None, reply_markup=None, **kwargs):
        self.bot = bot
        self.chat_id = chat_id
        self.latitude = latitude
        self.longitude = longitude
        self.title = title
        self.address = address
        self.foursquare_id = foursquare_id
        self.foursquare_type = foursquare_type
        self.google_place_id = google_place_id
        self.google_place_type = google_place_type
        self.disable_notification = disable_notification
        self.protect_content = protect_content
        self.reply_to_message_id = reply_to_message_id
        self.allow_sending_without_reply = allow_sending_without_reply
        self.reply_markup = reply_markup
        self.extra = kwargs

    def send_venue(self):
        url = '/sendVenue?chat_id={}&latitude={}&longitude={}&title={}&address={}'.format(self.chat_id, self.latitude, self.longitude, self.title, self.address)
        if self.foursquare_id:
            url += '&foursquare_id={}'.format(self.foursquare_id)
        if self.foursquare_type:
            url += '&foursquare_type={}'.format(self.foursquare_type)
        if self.google_place_id:
            url += '&google_place_type={}'.format(self.google_place_type)
        if self.google_place_type:
            url += '&google_place_type={}'.format(self.google_place_type)
        if self.disable_notification:
            url += '&disable_notification={}'.format(self.disable_notification)
        if self.protect_content:
            url += '&protect_content={}'.format(self.protect_content)
        if self.reply_to_message_id:
            url += '&reply_to_message_id={}'.format(self.reply_to_message_id)
        if self.allow_sending_without_reply:
            url += '&allow_sending_without_reply={}'.format(self.allow_sending_without_reply)
        if self.reply_markup:
            btns = parse_buttons(self.reply_markup)
            btns = json.dumps(btns)
            url += '&reply_markup={}'.format(btns)
        r = requests_session.get(self.bot.bot_url + url, params=self.extra)
        if r.status_code != 200:
            self.bot.check(r.json(), url)
        else:
            self.result = types.Message(r.json().get('result'))
            return self.result

    def __repr__(self):
        msg = self.__dict__
        return str(msg)

class sendContact:
    def __init__(self, bot, chat_id, phone_number, first_name, last_name=None, vcard=None, disable_notification=None, protect_content=None, reply_to_message_id=None, allow_sending_without_reply=None, reply_markup=None, **kwargs):
        self.bot = bot
        self.chat_id = chat_id
        self.phone_number = phone_number
        self.first_name = first_name
        self.last_name = last_name
        self.vcard = vcard
        self.disable_notification = disable_notification
        self.protect_content = protect_content
        self.reply_to_message_id = reply_to_message_id
        self.allow_sending_without_reply = allow_sending_without_reply
        self.reply_markup = reply_markup
        self.extra = kwargs

    def send_contact(self):
        url = '/sendContact?chat_id={}&phone_number={}&first_name={}&'.format(self.chat_id, self.phone_number, self.first_name)
        if self.last_name:
            url += '&last_name={}'.format(self.last_name)
        if self.vcard:
            url += '&vcard={}'.format(self.vcard)
        if self.disable_notification:
            url += '&disable_notification={}'.format(self.disable_notification)
        if self.protect_content:
            url += '&protect_content={}'.format(self.protect_content)
        if self.reply_to_message_id:
            url += '&reply_to_message_id={}'.format(self.reply_to_message_id)
        if self.allow_sending_without_reply:
            url += '&allow_sending_without_reply={}'.format(self.allow_sending_without_reply)
        if self.reply_markup:
            btns = parse_buttons(self.reply_markup)
            btns = json.dumps(btns)
            url += '&reply_markup={}'.format(btns)
        r = requests_session.get(self.bot.bot_url + url, params=self.extra)
        if r.status_code != 200:
            self.bot.check(r.json(), url)
        else:
            self.result = types.Message(r.json().get('result'))
            return self.result

    def __repr__(self):
        msg = self.__dict__
        return str(msg)

class sendPoll:
    def __init__(self, bot, chat_id, question, options, is_anonymous=None, type=None, allows_multiple_answers=None, correct_option_id=None, explanation=None, explanation_parse_mode=None, explanation_entities=None, open_period=None, close_date=None, is_closed=None, disable_notification=None, protect_content=None, reply_to_message_id=None, allow_sending_without_reply=None, reply_markup=None, **kwargs):
        self.bot = bot
        self.chat_id = chat_id
        self.question = question
        self.options = options
        self.is_anonymous = is_anonymous
        self.type = type
        self.allows_multiple_answers = allows_multiple_answers
        self.correct_option_id = correct_option_id
        self.explanation = explanation
        self.explanation_parse_mode = explanation_parse_mode
        self.explanation_entities = explanation_entities
        self.open_period = open_period
        self.close_date = close_date
        self.is_closed = is_closed
        self.disable_notification = disable_notification
        self.protect_content = protect_content
        self.reply_to_message_id = reply_to_message_id
        self.allow_sending_without_reply = allow_sending_without_reply
        self.reply_markup = reply_markup
        self.extra = kwargs

    def send_poll(self):
        url = '/sendPoll?chat_id={}&question={}&options={}'.format(self.chat_id, self.question, self.options)
        if self.is_anonymous:
            url += '&is_anonymous={}'.format(self.is_anonymous)
        if self.type:
            url += '&type={}'.format(self.type)
        if self.allows_multiple_answers:
            url += '&allows_multiple_answers={}'.format(self.allows_multiple_answers)
        if self.correct_option_id:
            url += '&correct_option_id={}'.format(self.correct_option_id)
        if self.explanation:
            url += '&explanation={}'.format(self.explanation)
        if self.explanation_parse_mode:
            url += '&explanation_parse_mode={}'.format(self.explanation_parse_mode)
        if self.explanation_entities:
            url += '&explanation_entities={}'.format(self.explanation_entities)
        if self.open_period:
            url += '&open_period={}'.format(self.open_period)
        if self.close_date:
            url += '&close_date={}'.format(self.close_date)
        if self.is_closed:
            url += '&is_closed={}'.format(self.is_closed)
        if self.disable_notification:
            url += '&disable_notification={}'.format(self.disable_notification)
        if self.protect_content:
            url += '&protect_content={}'.format(self.protect_content)
        if self.reply_to_message_id:
            url += '&reply_to_message_id={}'.format(self.reply_to_message_id)
        if self.allow_sending_without_reply:
            url += '&allow_sending_without_reply={}'.format(self.allow_sending_without_reply)
        if self.reply_markup:
            btns = parse_buttons(self.reply_markup)
            btns = json.dumps(btns)
            url += '&reply_markup={}'.format(btns)
        r = requests_session.get(self.bot.bot_url + url, params=self.extra)
        if r.status_code != 200:
            self.bot.check(r.json(), url)
        else:
            self.result = types.Message(r.json().get('result'))
            return self.result

    def __repr__(self):
        msg = self.__dict__
        return str(msg)

class sendDice:
    def __init__(self, bot, chat_id, emoji=None, disable_notification=None, protect_content=None, reply_to_message_id=None, allow_sending_without_reply=None, reply_markup=None, **kwargs):
        self.bot = bot
        self.chat_id = chat_id
        self.emoji = emoji
        self.disable_notification = disable_notification
        self.protect_content = protect_content
        self.reply_to_message_id = reply_to_message_id
        self.allow_sending_without_reply = allow_sending_without_reply
        self.reply_markup = reply_markup
        self.extra = kwargs

    def send_dice(self):
        url = '/sendDice?chat_id={}'.format(self.chat_id)
        r = requests_session.get(self.bot.bot_url + url, params=self.extra)
        if self.emoji:
            url += '&emoji={}'.format(self.emoji)
        if self.disable_notification:
            url += '&disable_notification={}'.format(self.disable_notification)
        if self.protect_content:
            url += '&protect_content={}'.format(self.protect_content)
        if self.reply_to_message_id:
            url += '&reply_to_message_id={}'.format(self.reply_to_message_id)
        if self.allow_sending_without_reply:
            url += '&allow_sending_without_reply={}'.format(self.allow_sending_without_reply)
        if self.reply_markup:
            btns = parse_buttons(self.reply_markup)
            btns = json.dumps(btns)
            url += '&reply_markup={}'.format(btns)
        if r.status_code != 200:
            self.bot.check(r.json(), url)
        else:
            self.result = types.Message(r.json().get('result'))
            return self.result

    def __repr__(self):
        msg = self.__dict__
        return str(msg)

class sendAction:
    def __init__(self, bot, chat_id, action, **kwargs):
        self.bot = bot
        self.chat_id = chat_id
        self.action = action
        self.extra = kwargs

    def send_action(self):
        url = '/sendAction?chat_id={}&action={}'.format(self.chat_id, self.action)
        r = requests_session.get(self.bot.bot_url + url, params=self.extra)
        if r.status_code != 200:
            self.bot.check(r.json(), url)
        else:
            self.result = r.json().get('result')
            return self.result

    def __repr__(self):
        msg = self.__dict__
        return str(msg)

class getUserProfilePhotos:
    def __init__(self, bot, user_id, offset=None, limit=None, **kwargs):
        self.bot = bot
        self.user_id = user_id
        self.offset = offset
        self.limit = limit
        self.extra = kwargs

    def get_user_profile_photos(self):
        url = '/get_user_profile_photos?user_id={}'.format(self.user_id)
        if self.offset:
            url += '&offset={}'.format(self.offset)
        if self.limit:
            url += '&limit={}'.format(self.limit)
        r = requests_session.get(self.bot.bot_url + url, params=self.extra)
        if r.status_code != 200:
            self.bot.check(r.json(), url)
        else:
            self.result = types.UserProfilePhotos(r.json().get('result'))
            return self.result

    def __repr__(self):
        msg = self.__dict__
        return str(msg)

class getFile:
    def __init__(self, bot, file_id, **kwargs):
        self.bot = bot
        self.file_id = file_id
        self.extra = kwargs

    def get_file(self):
        url = '/getFile?file_id={}'.format(self.file_id)
        r = requests_session.get(self.bot.bot_url + url, params=self.extra)
        if r.status_code != 200:
            self.bot.check(r.json(), url)
        else:
            self.result = types.File(r.json().get('result'))
            return self.result

    def __repr__(self):
        msg = self.__dict__
        return str(msg)

class banChatMember:
    def __init__(self, bot, chat_id, user_id, until_date=None, revoke_messages=None, **kwargs):
        self.bot = bot
        self.chat_id = chat_id
        self.user_id = user_id
        self.until_date = until_date
        self.revoke_messages = revoke_messages
        self.extra = kwargs

    def ban_chat_member(self):
        url = '/banChatMember?chat_id={}&user_id={}'.format(self.chat_id, self.user_id)
        if self.until_date:
            url += '&until_date={}'.format(self.until_date)
        if self.revoke_messages:
            url += '&revoke_messages={}'.format(self.revoke_messages)
        r = requests_session.get(self.bot.bot_url + url, params=self.extra)
        if r.status_code != 200:
            self.bot.check(r.json(), url)
        else:
            self.result = r.json().get('result')
            return self.result

    def __repr__(self):
        msg = self.result
        return str(msg)

class unbanChatMember:
    def __init__(self, bot, chat_id, user_id, only_if_banned=None, **kwargs):
        self.bot = bot
        self.chat_id = chat_id
        self.user_id = user_id
        self.only_if_banned = only_if_banned
        self.extra = kwargs

    def unban_chat_member(self):
        url = '/unbanChatMember?chat_id={}&user_id={}'.format(self.chat_id, self.user_id)
        if self.only_if_banned:
            url += '&only_if_banned={}'.format(self.only_if_banned)
        r = requests_session.get(self.bot.bot_url + url, params=self.extra)
        if r.status_code != 200:
            self.bot.check(r.json(), url)
        else:
            self.result = r.json().get('result')
            return self.result

    def __repr__(self):
        msg = self.result
        return str(msg)

class restrictChatMember:
    def __init__(self, bot, chat_id, user_id, permissions, until_date=None, **kwargs):
        self.bot = bot
        self.chat_id = chat_id
        self.user_id = user_id
        if isinstance(permissions, types.ChatPermissions):
            self.permissions = permissions.get_json()
        else:
            self.permissions = permissions
        self.until_date = until_date
        self.extra = kwargs

    def restrict_chat_member(self):
        url = '/restrictChatMember?chat_id={}&user_id={}'.format(self.chat_id, self.user_id)
        if self.until_date:
            url += '&until_date={}'.format(self.until_date)
        d = {
            'permissions': json.dumps(self.permissions)
        }
        d.update(self.extra)
        r = requests_session.get(self.bot.bot_url + url, params=d)
        if r.status_code != 200:
            self.bot.check(r.json(), url)
        else:
            self.result = r.json().get('result')
            return self.result

    def __repr__(self):
        msg = self.result
        return str(msg)

class promoteChatMember:
    def __init__(self, bot, chat_id, user_id, is_anonymous=None, can_manage_chat=None, can_post_messages=None, can_edit_messages=None, can_delete_messages=None, can_manage_video_chats=None, can_restrict_members=None, can_promote_members=None, can_change_info=None, can_invite_users=None, can_pin_messages=None, **kwargs):
        self.bot = bot
        self.chat_id = chat_id
        self.user_id = user_id
        self.is_anonymous = is_anonymous
        self.can_manage_chat = can_manage_chat
        self.can_post_messages = can_post_messages
        self.can_edit_messages = can_edit_messages
        self.can_delete_messages = can_delete_messages
        self.can_manage_video_chats = can_manage_video_chats
        self.can_restrict_members = can_restrict_members
        self.can_promote_members = can_promote_members
        self.can_change_info = can_change_info
        self.can_invite_users = can_invite_users
        self.can_pin_messages = can_pin_messages
        self.extra = kwargs

    def promote_chat_member(self):
        url = '/promoteChatMember?chat_id={}&user_id={}'.format(self.chat_id, self.chat_id)
        if self.is_anonymous:
            url += '&is_anonymous={}'.format(self.is_anonymous)
        if self.can_manage_chat:
            url += '&can_manage_chat={}'.format(self.can_manage_chat)
        if self.can_post_messages:
            url += '&can_post_messages={}'.format(self.can_post_messages)
        if self.can_delete_messages:
            url += '&can_delete_messages={}'.format(self.can_delete_messages)
        if self.can_manage_video_chats:
            url += '&can_manage_video_chats={}'.format(self.can_manage_video_chats)
        if self.can_restrict_members:
            url += '&can_restrict_members={}'.format(self.can_restrict_members)
        if self.can_promote_members:
            url += '&can_promote_members={}'.format(self.can_promote_members)
        if self.can_change_info:
            url += '&can_change_info={}'.format(self.can_change_info)
        if self.can_invite_users:
            url += '&can_invite_users={}'.format(self.can_invite_users)
        if self.can_pin_messages:
            url += '&can_pin_messages={}'.format(self.can_pin_messages)
        r = requests_session.get(self.bot.bot_url + url, params=self.extra)
        if r.status_code != 200:
            self.bot.check(r.json(), url)
        else:
            self.result = r.json().get('result')
            return self.result

    def __repr__(self):
        msg = self.__dict__
        return str(msg)

class setChatAdministratorCustomTitle:
    def __init__(self, bot, chat_id, user_id, custom_title, **kwargs):
        self.bot = bot
        self.chat_id = chat_id
        self.user_id = user_id
        self.custom_title = custom_title
        self.extra = kwargs

    def set_chat_administrator_custom_title(self):
        url = '/setChatAdministratorCustomTitle?chat_id={}&user_id={}&custom_title={}'.format(self.chat_id, self.user_id, self.custom_title)
        r = requests_session.get(self.bot.bot_url + url, params=self.extra)
        if r.status_code != 200:
            self.bot.check(r.json(), url)
        else:
            self.result = r.json().get('result')
            return self.result

    def __repr__(self):
        msg = self.__dict__
        return str(msg)

class banChatSenderChat:
    def __init__(self, bot, chat_id, sender_chat_id, **kwargs):
        self.bot = bot
        self.chat_id = chat_id
        self.sender_chat_id = sender_chat_id
        self.extra = kwargs

    def ban_chat_sender_chat(self):
        url = '/banChatSenderChat?chat_id={}&sender_chat_id={}'.format(self.chat_id, self.sender_chat_id)
        r = requests_session.get(self.bot.bot_url + url, params=self.extra)
        if r.status_code != 200:
            self.bot.check(r.json(), url)
        else:
            self.result = r.json().get('result')
            return self.result

    def __repr__(self):
        msg = self.result
        return str(msg)

class unbanChatSenderChat:
    def __init__(self, bot, chat_id, sender_chat_id, **kwargs):
        self.bot = bot
        self.chat_id = chat_id
        self.sender_chat_id = sender_chat_id
        self.extra = kwargs

    def unban_chat_sender_chat(self):
        url = '/unbanChatSenderChat?chat_id={}&sender_chat_id={}'.format(self.chat_id, self.sender_chat_id)
        r = requests_session.get(self.bot.bot_url + url, params=self.extra)
        if r.status_code != 200:
            self.bot.check(r.json(), url)
        else:
            self.result = r.json().get('result')
            return self.result

    def __repr__(self):
        msg = self.result
        return str(msg)

class setChatPermissions:
    def __init__(self, bot, chat_id, permissions, **kwargs):
        self.bot = bot
        self.chat_id = chat_id
        self.permissions = permissions
        self.extra = kwargs

    def set_chat_permissions(self):
        url = '/setChatPermissions?chat_id={}'.format(self.chat_id)
        if isinstance(self.permissions, types.ChatPermissions):
            permissions = self.permissions.get_json()
        url += '&permissions={}'.format(self.permissions)
        url = json.dumps(url)
        r = requests_session.get(self.bot.bot_url + url, params=self.extra)
        if r.status_code != 200:
            self.bot.check(r.json(), url)
        else:
            self.result = r.json().get('result')
            return self.result

    def __repr__(self):
        msg = self.__dict__
        return str(msg)

class exportChatInviteLink:
    def __init__(self, bot, chat_id, **kwargs):
        self.bot = bot
        self.chat_id = chat_id
        self.extra = kwargs

    def export_chat_invite_link(self):
        url = '/exportChatInviteLink?chat_id={}'.format(self.chat_id)
        r = requests_session.get(self.bot.bot_url + url, params=self.extra)
        if r.status_code != 200:
            self.bot.check(r.json(), url)
        else:
            self.result = r.json().get('result')
            return self.result

    def __repr__(self):
        msg = self.__dict__
        return str(msg)

class createChatInviteLink:
    def __init__(self, bot, chat_id, name=None, expire_date=None, member_limit=None, creates_join_request=None, **kwargs):
        self.bot = bot
        self.chat_id = chat_id
        self.name = name
        self.expire_date = expire_date
        self.member_limit = member_limit
        self.creates_join_request = creates_join_request
        self.extra = kwargs

    def create_chat_invite_link(self):
        url = '/createChatInviteLink?chat_id={}'.format(self.chat_id)
        if self.name:
            url += '&name={}'.format(self.name)
        if self.expire_date:
            url += '&expire_date={}'.format(self.expire_date)
        if self.member_limit:
            url += '&member_limit={}'.format(self.member_limit)
        if self.creates_join_request:
            url += '&creates_join_request={}'.format(self.creates_join_request)
        r = requests_session.get(self.bot.bot_url + url, params=self.extra)
        if r.status_code != 200:
            self.bot.check(r.json(), url)
        else:
            self.result = types.createChatInviteLink(r.json().get('result'))
            return self.result

    def __repr__(self):
        msg = self.__dict__
        return str(msg)

class editChatInviteLink:
    def __init__(self, bot, chat_id, invite_link, name=None, expire_date=None, member_limit=None, creates_join_request=None, **kwargs):
        self.bot = bot
        self.chat_id = chat_id
        self.invite_link = invite_link
        self.name = name
        self.expire_date = expire_date
        self.member_limit = member_limit
        self.creates_join_request = creates_join_request
        self.extra = kwargs

    def edit_chat_invite_link(self):
        url = '/editChatInviteLink?chat_id={}&invite_link={}'.format(self.chat_id, self.invite_link)
        if self.name:
            url += '&name={}'.format(self.name)
        if self.expire_date:
            url += '&expire_date={}'.format(self.expire_date)
        if self.member_limit:
            url += '&member_limit={}'.format(self.member_limit)
        if self.creates_join_request:
            url += '&creates_join_request={}'.format(self.creates_join_request)
        r = requests_session.get(self.bot.bot_url + url, params=self.extra)
        if r.status_code != 200:
            self.bot.check(r.json(), url)
        else:
            self.result = types.createChatInviteLink(r.json().get('result'))
            return self.result

    def __repr__(self):
        msg = self.__dict__
        return str(msg)

class revokeChatInviteLink:
    def __init__(self, bot, chat_id, invite_link, **kwargs):
        self.bot = bot
        self.chat_id = chat_id
        self.invite_link = invite_link
        self.extra = kwargs

    def revoke_chat_invite_link(self):
        url = '/revokeChatInviteLink?chat_id={}&invite_link={}'.format(self.chat_id, self.invite_link)
        r = requests_session.get(self.bot.bot_url + url, params=self.extra)
        if r.status_code != 200:
            self.bot.check(r.json(), url)
        else:
            self.result = types.ChatInviteLink(r.json().get('result'))
            return self.result

    def __repr__(self):
        msg = self.__dict__
        return str(msg)

class approveChatJoinRequest:
    def __init__(self, bot, chat_id, user_id, **kwargs):
        self.bot = bot
        self.chat_id = chat_id
        self.user_id = user_id
        self.extra = kwargs

    def approve_chat_join_request(self):
        url = '/approveChatJoinRequest?chat_id={}&user_id={}'.format(self.chat_id, self.user_id)
        r = requests_session.get(self.bot.bot_url + url, params=self.extra)
        if r.status_code != 200:
            self.bot.check(r.json(), url)
        else:
            self.result = r.json().get('result')
            return self.result

    def __repr__(self):
        msg = self.__dict__
        return str(msg)

class declineChatJoinRequest:
    def __init__(self, bot, chat_id, user_id, **kwargs):
        self.bot = bot
        self.chat_id = chat_id
        self.user_id = user_id
        self.extra = kwargs

    def decline_chat_join_request(self):
        url = '/declineChatJoinRequest?chat_id={}&user_id={}'.format(self.chat_id, self.user_id)
        r = requests_session.get(self.bot.bot_url + url, params=self.extra)
        if r.status_code != 200:
            self.bot.check(r.json(), url)
        else:
            self.result = r.json().get('result')
            return self.result

    def __repr__(self):
        msg = self.__dict__
        return str(msg)

class setChatPhoto:
    def __init__(self, bot, **kwargs):
        self.bot = bot
        self.chat_id = chat_id
        self.photo = photo
        self.extra = kwargs

    def set_chat_photo(self):
        url = '/setChatPhoto?chat_id={}&photo={}'.format(self.chat_id, self.photo)
        r = requests_session.get(self.bot.bot_url + url, params=self.extra)
        if r.status_code != 200:
            self.bot.check(r.json(), url)
        else:
            self.result = r.json().get('result')
            return self.result

    def __repr__(self):
        msg = self.__dict__
        return str(msg)

class deleteChatPhoto:
    def __init__(self, bot, **kwargs):
        self.bot = bot
        self.chat_id = chat_id
        self.extra = kwargs

    def delete_chat_photo(self):
        url = '/deleteChatPhoto?chat_id={}'.format(self.chat_id)
        r = requests_session.get(self.bot.bot_url + url, params=self.extra)
        if r.status_code != 200:
            self.bot.check(r.json(), url)
        else:
            self.result = r.json().get('result')
            return self.result

    def __repr__(self):
        msg = self.__dict__
        return str(msg)

class setChatTitle:
    def __init__(self, bot, chat_id, title, **kwargs):
        self.bot = bot
        self.chat_id = chat_id
        self.title = title
        self.extra = kwargs

    def set_chat_title(self):
        url = '/setChatTitle?chat_id={}'.format(self.chat_id, self.title)
        r = requests_session.get(self.bot.bot_url + url, params=self.extra)
        if r.status_code != 200:
            self.bot.check(r.json(), url)
        else:
            self.result = r.json().get('result')
            return self.result

    def __repr__(self):
        msg = self.__dict__
        return str(msg)

class setChatDescription:
    def __init__(self, bot, chat_id, description, **kwargs):
        self.bot = bot
        self.chat_id = chat_id
        self.description = description
        self.extra = kwargs

    def set_description_title(self):
        url = '/setChatDescription?chat_id={}&description=description'.format(self.chat_id, self.description)
        r = requests_session.get(self.bot.bot_url + url, params=self.extra)
        if r.status_code != 200:
            self.bot.check(r.json(), url)
        else:
            self.result = r.json().get('result')
            return self.result

    def __repr__(self):
        msg = self.__dict__
        return str(msg)

class pinChatMessage:
    def __init__(self, bot, chat_id, message_id, disable_notification=None, **kwargs):
        self.bot = bot
        self.chat_id = chat_id
        self.message_id = message_id
        self.disable_notification = disable_notification
        self.extra = kwargs

    def pin_chat_message(self):
        url = '/pinChatMessage?chat_id={}&message_id={}'.format(self.chat_id, self.message_id)
        if self.disable_notification:
            url += '&disable_notification={}'.format(self.disable_notification)
        r = requests_session.get(self.bot.bot_url + url, params=self.extra)
        if r.status_code != 200:
            self.bot.check(r.json(), url)
        else:
            self.result = r.json().get('result')
            return self.result

    def __repr__(self):
        msg = self.__dict__
        return str(msg)

class unpinChatMessage:
    def __init__(self, bot, chat_id, message_id, **kwargs):
        self.bot = bot
        self.chat_id = chat_id
        self.message_id = message_id
        self.extra = kwargs

    def unpin_chat_message(self):
        url = '/unpinChatMessage?chat_id={}&message_id={}'.format(self.chat_id, self.message_id)
        r = requests_session.get(self.bot.bot_url + url, params=self.extra)
        if r.status_code != 200:
            self.bot.check(r.json(), url)
        else:
            self.result = r.json().get('result')
            return self.result

    def __repr__(self):
        msg = self.__dict__
        return str(msg)

class unpinAllChatMessages:
    def __init__(self, bot, chat_id, **kwargs):
        self.bot = bot
        self.chat_id = chat_id
        self.extra = kwargs

    def unpin_all_chat_messages(self):
        url = '/unpinAllChatMessages?chat_id={}'.format(self.chat_id)
        r = requests_session.get(self.bot.bot_url + url, params=self.extra)
        if r.status_code != 200:
            self.bot.check(r.json(), url)
        else:
            self.result = r.json().get('result')
            return self.result

    def __repr__(self):
        msg = self.__dict__
        return str(msg)

class leaveChat:
    def __init__(self, bot, chat_id, **kwargs):
        self.bot = bot
        self.chat_id = chat_id
        self.extra = kwargs

    def leave_chat(self):
        url = '/leaveChat?chat_id={}'.format(self.chat_id)
        r = requests_session.get(self.bot.bot_url + url, params=self.extra)
        if r.status_code != 200:
            self.bot.check(r.json(), url)
        else:
            self.result = r.json().get('result')
            return self.result

    def __repr__(self):
        msg = self.__dict__
        return str(msg)

class getChat:
    def __init__(self, bot, chat_id, option=None, **kwargs):
        self.bot = bot
        self.chat_id = chat_id
        self.option = option
        self.extra = kwargs

    def get_chat(self):
        url = '/getChat?chat_id={}'.format(self.chat_id)
        r = requests_session.get(self.bot.bot_url + url, params=self.extra)
        if r.status_code != 200:
            if self.option:
                return self.option
            self.bot.check(r.json(), url)
        else:
            self.result = types.Chat(r.json().get('result'))
            return self.result

    def __repr__(self):
        msg = self.result
        return str(msg)

class getChatAdministrators:
    def __init__(self, bot, chat_id, **kwargs):
        self.bot = bot
        self.chat_id = chat_id
        self.extra = kwargs

    def get_chat_administrators(self):
        url = '/getChatAdministrators?chat_id={}'.format(self.chat_id)
        r = requests_session.get(self.bot.bot_url + url, params=self.extra)
        if r.status_code != 200:
            self.bot.check(r.json(), url)
        else:
            self.result = types.ChatMember(r.json().get('result')).do()
            return self.result

    def __repr__(self):
        msg = self.result
        return str(msg)

class getChatMemberCount:
    def __init__(self, bot, chat_id, **kwargs):
        self.bot = bot
        self.chat_id = chat_id
        self.extra = kwargs

    def get_chat_member_count(self):
        url = '/getChatMemberCount?chat_id={}'.format(self.chat_id)
        r = requests_session.get(self.bot.bot_url + url, params=self.extra)
        if r.status_code != 200:
            self.bot.check(r.json(), url)
        else:
            self.result = r.json().get('result')
            return self.result

    def __repr__(self):
        msg = self.result
        return str(msg)

class getChatMember:
    def __init__(self, bot, chat_id, user_id, **kwargs):
        self.bot = bot
        self.chat_id = chat_id
        self.user_id = user_id
        self.extra = kwargs

    def get_chat_member(self):
        url = '/getChatMember?chat_id={}&user_id={}'.format(self.chat_id, self.user_id)
        r = requests_session.get(self.bot.bot_url + url, params=self.extra)
        if r.status_code != 200:
            self.bot.check(r.json(), url)
        else:
            self.result = types.ChatMember(r.json().get('result')).do()
            return self.result

    def __repr__(self):
        msg = self.result
        return str(msg)

class setChatStickerSet:
    def __init__(self, bot, chat_id, sticker_set_name, **kwargs):
        self.bot = bot
        self.chat_id = chat_id
        self.sticker_set_name = sticker_set_name
        self.extra = kwargs

    def set_chat_sticker_set(self):
        url = '/setChatStickerSet?chat_id={}&sticker_set_name={}'.format(self.chat_id, self.sticker_set_name)
        r = requests_session.get(self.bot.bot_url + url, params=self.extra)
        if r.status_code != 200:
            self.bot.check(r.json(), url)
        else:
            self.result = r.json().get('result')
            return self.result

    def __repr__(self):
        msg = self.result
        return str(msg)

class deleteChatStickerSet:
    def __init__(self, bot, chat_id, **kwargs):
        self.bot = bot
        self.chat_id = chat_id
        self.extra = kwargs

    def delete_chat_sticker_set(self):
        url = '/deleteChatStickerSet?chat_id={}'.format(self.chat_id,)
        r = requests_session.get(self.bot.bot_url + url, params=self.extra)
        if r.status_code != 200:
            self.bot.check(r.json(), url)
        else:
            self.result = r.json().get('result')
            return self.result

    def __repr__(self):
        msg = self.result
        return str(msg)

class answerCallbackQuery:
    def __init__(self, bot, callback_query_id, text=None, show_alert=None, url=None, cache_time=None, **kwargs):
        self.bot = bot
        self.callback_query_id = callback_query_id
        self.text = text
        self.show_alert = show_alert
        self.url = url
        self.cache_time = cache_time
        self.extra = kwargs

    def answer_callback_query(self):
        url = '/answerCallbackQuery?callback_query_id={}'.format(self.callback_query_id)
        if self.text:
            url += '&text={}'.format(self.text)
        if self.show_alert:
            url += '&show_alert={}'.format(self.show_alert)
        if self.url:
            url += '&url={}'.format(self.url)
        if self.cache_time:
            url += '&cache_time={}'.format(self.cache_time)
        r = requests_session.get(self.bot.bot_url + url, params=self.extra)
        if r.status_code != 200:
            self.bot.check(r.json(), url)
        else:
            return r.json().get('result')

    def __repr__(self):
        msg = self.msg.__dict__
        return str(msg)

class setMyCommands:
    def __init__(self, bot, commands, scope=None, language_code=None, **kwargs):
        self.bot = bot
        self.commands = commands
        self.scope = scope
        self.language_code = language_code
        self.extra = kwargs

    def set_my_commands(self):
        url = '/setMyCommands?commands={}'.format(self.commands)
        if self.scope:
            url += '&scope={}'.format(self.scope)
        if self.language_code:
            url += '&language_code={}'.format(self.language_code)
        r = requests_session.get(self.bot.bot_url + url, params=self.extra)
        if r.status_code != 200:
            self.bot.check(r.json(), url)
        else:
            self.result = r.json().get('result')
            return self.result

    def __repr__(self):
        msg = self.result
        return str(msg)

class deleteMyCommands:
    def __init__(self, bot, scope=None, language_code=None, **kwargs):
        self.bot = bot
        self.scope = scope
        self.language_code = language_code
        self.extra = kwargs

    def delete_my_commands(self):
        url = '/deleteMyCommands'
        if self.scope:
            url += '&scope={}'.format(self.scope)
        if self.language_code:
            url += '&language_code={}'.format(self.language_code)
        r = requests_session.get(self.bot.bot_url + url, params=self.extra)
        if r.status_code != 200:
            self.bot.check(r.json(), url)
        else:
            self.result = r.json().get('result')
            return self.result

    def __repr__(self):
        msg = self.result
        return str(msg)

class getMyCommands:
    def __init__(self, bot, scope=None, language_code=None, **kwargs):
        self.bot = bot
        self.scope = scope
        self.language_code = language_code
        self.extra = kwargs

    def get_my_commands(self):
        url = '/getMyCommands'
        if self.scope:
            url += '&scope={}'.format(self.scope)
        if self.language_code:
            url += '&language_code={}'.format(self.language_code)
        r = requests_session.get(self.bot.bot_url + url, params=self.extra)
        if r.status_code != 200:
            self.bot.check(r.json(), url)
        else:
            self.result = r.json().get('result')
            return self.result

    def __repr__(self):
        msg = self.result
        return str(msg)

class setChatMenuButton:
    def __init__(self, bot, chat_id=None, menu_button=None, **kwargs):
        self.bot = bot
        self.chat_id = chat_id
        self.menu_button = menu_button
        self.extra = kwargs

    def set_chat_menu_button(self):
        url = '/setChatMenuButton'
        if self.chat_id:
            url += '&chat_id={}'.format(self.chat_id)
        if self.menu_button:
            url += '&menu_button={}'.format(self.menu_button)
        r = requests_session.get(self.bot.bot_url + url, params=self.extra)
        if r.status_code != 200:
            self.bot.check(r.json(), url)
        else:
            self.result = r.json().get('result')
            return self.result

    def __repr__(self):
        msg = self.result
        return str(msg)

class getChatMenuButton:
    def __init__(self, bot, chat_id=None, **kwargs):
        self.bot = bot
        self.chat_id = chat_id
        self.extra = kwargs

    def get_chat_menu_button(self):
        url = '/getChatMenuButton'
        if self.chat_id:
            url += '&chat_id={}'.format(self.chat_id)
        r = requests_session.get(self.bot.bot_url + url, params=self.extra)
        if r.status_code != 200:
            self.bot.check(r.json(), url)
        else:
            self.result = r.json().get('result')
            return self.result

    def __repr__(self):
        msg = self.result
        return str(msg)

class setMyDefaultAdministratorRights:
    def __init__(self, bot, rights=None, for_channels=None, **kwargs):
        self.bot = bot
        self.rights = rights
        self.for_channels = for_channels
        self.extra = kwargs

    def set_my_default_administrator_rights(self):
        url = '/setMyDefaultAdministratorRights'
        if self.rights:
            url += '&rights={}'.format(self.rights)
        if self.for_channels:
            if isinstance(self.for_channels, types.ChatAdministratorRights):
                for_channels = self.for_channels.get_dict()
            else:
                for_channels = self.for_channels
            url += '&for_channels={}'.format(for_channels)
        r = requests_session.get(self.bot.bot_url + url, params=self.extra)
        if r.status_code != 200:
            self.bot.check(r.json(), url)
        else:
            self.result = r.json().get('result')
            return self.result

    def __repr__(self):
        msg = self.result
        return str(msg)

class getMyDefaultAdministratorRights:
    def __init__(self, bot, for_channels=None, **kwargs):
        self.bot = bot
        self.for_channels = for_channels
        self.extra = kwargs

    def get_my_default_administrator_rights(self):
        url = '/getMyDefaultAdministratorRights'
        if self.for_channels:
            url += '&for_channels={}'.format(self.for_channels)
        r = requests_session.get(self.bot.bot_url + url, params=self.extra)
        if r.status_code != 200:
            self.bot.check(r.json(), url)
        else:
            self.result = r.json().get('result')
            return self.result

    def __repr__(self):
        msg = self.result
        return str(msg)

class editMessageText:
    def __init__(self, bot, text, chat_id=None, message_id=None, inline_message_id=None, parse_mode=None, entities=None, disable_web_page_preview=None, reply_markup=None, **kwargs):
        self.bot = bot
        self.chat_id = chat_id
        self.message_id = message_id
        self.inline_message_id = inline_message_id
        self.text = text
        self.parse_mode = parse_mode
        self.entities = entities
        self.disable_web_page_preview = disable_web_page_preview
        self.reply_markup = reply_markup
        self.extra = kwargs

    def edit_message_text(self):
        url = '/editMessageText?text={}'.format(self.text)
        if self.chat_id:
            url += '&chat_id={}'.format(self.chat_id)
        if self.message_id:
            url += '&message_id={}'.format(self.message_id)
        if self.inline_message_id:
            url += '&inline_message_id={}'.format(self.inline_message_id)
        if self.parse_mode:
            url += '&parse_mode={}'.format(self.parse_mode)
        if self.entities:
            url += '&entities={}'.format(self.entities)
        if self.disable_web_page_preview:
            url += '&disable_web_page_preview={}'.format(self.disable_web_page_preview)
        if self.reply_markup:
            btns = parse_buttons(self.reply_markup)
            btns = json.dumps(btns)
            url += '&reply_markup={}'.format(btns)
        r = requests_session.get(self.bot.bot_url + url, params=self.extra)
        if r.status_code != 200:
            self.bot.check(r.json(), url)
        else:
            self.result = r.json().get('result')
            if self.result is True:
                return self.result
            else:
                return types.Message(self.result)

    def __repr__(self):
        msg = self.result
        return str(msg)

class editMessageCaption:
    def __init__(self, bot, chat_id=None, message_id=None, inline_message_id=None, caption=None, parse_mode=None, entities=None, disable_web_page_preview=None, reply_markup=None, **kwargs):
        self.bot = bot
        self.chat_id = chat_id
        self.message_id = message_id
        self.inline_message_id = inline_message_id
        self.caption = caption
        self.parse_mode = parse_mode
        self.caption_entities = caption_entities
        self.reply_markup = reply_markup
        self.extra = kwargs

    def edit_message_caption(self):
        url = '/editMessageCaption?caption={}'.format(self.text)
        if self.chat_id:
            url += '&chat_id={}'.format(self.chat_id)
        if self.message_id:
            url += '&message_id={}'.format(self.message_id)
        if self.inline_message_id:
            url += '&inline_message_id={}'.format(self.inline_message_id)
        if self.parse_mode:
            url += '&parse_mode={}'.format(self.parse_mode)
        if self.caption_entities:
            url += '&caption_entities={}'.format(self.caption_entities)
        if self.reply_markup:
            btns = parse_buttons(self.reply_markup)
            btns = json.dumps(btns)
            url += '&reply_markup={}'.format(btns)
        r = requests_session.get(self.bot.bot_url + url, params=self.extra)
        if r.status_code != 200:
            self.bot.check(r.json(), url)
        else:
            self.result = r.json().get('result')
            if self.result is True:
                return self.result
            else:
                return types.Message(self.result)

    def __repr__(self):
        msg = self.result
        return str(msg)

class editMessageMedia:
    def __init__(self, bot, media, chat_id=None, message_id=None, inline_message_id=None, reply_markup=None, **kwargs):
        self.bot = bot
        self.chat_id = chat_id
        self.message_id = message_id
        self.inline_message_id = inline_message_id
        self.media = media
        self.extra = kwargs

    def edit_message_media(self):
        url = '/editMessageMedia?media={}'.format(self.media)
        if self.chat_id:
            url += '&chat_id={}'.format(self.chat_id)
        if self.message_id:
            url += '&message_id={}'.format(self.message_id)
        if self.inline_message_id:
            url += '&inline_message_id={}'.format(self.inline_message_id)
        if self.reply_markup:
            btns = parse_buttons(self.reply_markup)
            btns = json.dumps(btns)
            url += '&reply_markup={}'.format(btns)
        r = requests_session.get(self.bot.bot_url + url, params=self.extra)
        if r.status_code != 200:
            self.bot.check(r.json(), url)
        else:
            self.result = r.json().get('result')
            if self.result is True:
                return self.result
            else:
                return types.Message(self.result)

    def __repr__(self):
        msg = self.result
        return str(msg)

class editMessageReplyMarkup:
    def __init__(self, bot, media, chat_id=None, message_id=None, inline_message_id=None, reply_markup=None, **kwargs):
        self.bot = bot
        self.chat_id = chat_id
        self.message_id = message_id
        self.inline_message_id = inline_message_id
        self.media = media
        self.extra = kwargs

    def edit_message_reply_markup(self):
        url = '/editMessageReplyMarkup'
        if self.chat_id:
            url += '&chat_id={}'.format(self.chat_id)
        if self.message_id:
            url += '&message_id={}'.format(self.message_id)
        if self.inline_message_id:
            url += '&inline_message_id={}'.format(self.inline_message_id)
        if self.reply_markup:
            btns = parse_buttons(self.reply_markup)
            btns = json.dumps(btns)
            url += '&reply_markup={}'.format(btns)
        r = requests_session.get(self.bot.bot_url + url, params=self.extra)
        if r.status_code != 200:
            self.bot.check(r.json(), url)
        else:
            self.result = r.json().get('result')
            if self.result is True:
                return self.result
            else:
                return types.Message(self.result)

    def __repr__(self):
        msg = self.result
        return str(msg)

class stopPoll:
    def __init__(self, bot, chat_id, message_id, reply_markup=None, **kwargs):
        self.bot = bot
        self.chat_id = chat_id
        self.message_id = message_id
        self.extra = kwargs

    def stop_poll(self):
        url = '/stopPoll&chat_id={}&message_id={}'.format(self.chat_id, self.message_id)
        if self.reply_markup:
            btns = parse_buttons(self.reply_markup)
            btns = json.dumps(btns)
            url += '&reply_markup={}'.format(btns)
        r = requests_session.get(self.bot.bot_url + url, params=self.extra)
        if r.status_code != 200:
            self.bot.check(r.json(), url)
        else:
            self.result = types.Poll(r.json().get('result'))
            return self.result

    def __repr__(self):
        msg = self.result
        return str(msg)

class deleteMessage:
    def __init__(self, bot, chat_id, message_id, **kwargs):
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

class sendSticker:
    def __init__(self, bot, chat_id, sticker, disable_web_page_preview=None, protect_content=None, reply_to_message_id=None, allow_sending_without_reply=None, reply_markup=None, **kwargs):
        self.bot = bot
        self.chat_id = chat_id
        self.sticker = sticker
        self.disable_web_page_preview = disable_web_page_preview
        self.protect_content = protect_content
        self.reply_to_message_id = reply_to_message_id
        self.allow_sending_without_reply = allow_sending_without_reply
        self.reply_markup = reply_markup
        self.extra = kwargs

    def send_sticker(self):
        url = '/sendSticker&chat_id={}&sticker={}'.format(self.chat_id, self.sticker)
        r = requests_session.get(self.bot.bot_url + url, params=self.extra)
        if r.status_code != 200:
            self.bot.check(r.json(), url, params=self.extra)
        else:
            self.result = types.Message(r.json().get('result'))
            return self.result

    def __repr__(self):
        msg = self.result
        return str(msg)

class getStickerSet:
    def __init__(self, bot, name, **kwargs):
        self.bot = bot
        self.name = name
        self.extra = kwargs

    def get_sticker_set(self):
        url = '/getStickerSet?name={}'.format(self.name)
        r = requests_session.get(self.bot.bot_url + url, params=self.extra)
        if r.status_code != 200:
            self.bot.check(r.json(), url, params=self.extra)
        else:
            self.result = types.StickerSet(r.json().get('result'))
            return self.result

    def __repr__(self):
        msg = self.result
        return str(msg)

class getCustomEmojiStickers:
    def __init__(self, bot, custom_emoji_ids, **kwargs):
        self.bot = bot
        self.custom_emoji_ids = custom_emoji_ids
        self.extra = kwargs

    def get_custom_emoji_sticker(self):
        url = '/getCustomEmojiStickers?custom_emoji_ids={}'.format(self.custom_emoji_ids)
        r = requests_session.get(self.bot.bot_url + url, params=self.extra)
        if r.status_code != 200:
            self.bot.check(r.json(), url, params=self.extra)
        else:
            self.result = types.StickerSet(r.json().get('result'))
            return self.result

    def __repr__(self):
        msg = self.result
        return str(msg)

class uploadStickerFile:
    def __init__(self, bot, user_id, png_sticker, **kwargs):
        self.bot = bot
        self.png_sticker = png_sticker
        self.extra = kwargs

    def upload_sticker_file(self):
        url = '/uploadStickerFile?user_id={}&png_sticker={}'.format(self.user_id, self.png_sticker)
        r = requests_session.get(self.bot.bot_url + url, params=self.extra)
        if r.status_code != 200:
            self.bot.check(r.json(), url, params=self.extra)
        else:
            self.result = types.File(r.json().get('result'))
            return self.result

    def __repr__(self):
        msg = self.result
        return str(msg)

class createNewStickerSet:
    def __init__(self, bot, user_id, name, title, emoji, png_sticker=None, tgs_sticker=None, webm_sticker=None, sticker_type=None, mask_position=None, **kwargs):
        self.bot = bot
        self.user_id = user_id
        self.name = name
        self.title = title
        self.emoji = emoji
        self.png_sticker = png_sticker
        self.tgs_sticker = tgs_sticker
        self.webm_sticker = webm_sticker
        self.sticker_type = sticker_type
        self.mask_position = mask_position
        self.extra = kwargs

    def create_new_sticker(self):
        url = '/createNewStickerSet?user_id={}&name={}&title={}&emoji={}'.format(self.user_id, self.name, self.title, self.emoji)
        if self.png_sticker:
            url += '&png_sticker={}'.format(self.png_sticker)
        if self.tgs_sticker:
            url += '&tgs_sticker={}'.format(self.tgs_sticker)
        if self.webm_sticker:
            url += '&webm_sticker={}'.format(self.webm_sticker)
        if self.sticker_type:
            url += '&sticker_type={}'.format(self.sticker_type)
        if self.mask_position:
            url += '&mask_position={}'.format(self.mask_position)
        r = requests_session.get(self.bot.bot_url + url, params=self.extra)
        if r.status_code != 200:
            self.bot.check(r.json(), url, params=self.extra)
        else:
            self.result = r.json().get('result')
            return self.result

    def __repr__(self):
        msg = self.result
        return str(msg)

class addStickerToSet:
    def __init__(self, bot, user_id, name, emoji, png_sticker=None, tgs_sticker=None, webm_sticker=None, mask_position=None, **kwargs):
        self.bot = bot
        self.user_id = user_id
        self.name = name
        self.emoji = emoji
        self.png_sticker = png_sticker
        self.tgs_sticker = tgs_sticker
        self.webm_sticker = webm_sticker
        self.mask_position = mask_position
        self.extra = kwargs

    def add_sticker_to_set(self):
        url = '/addStickerToSet?user_id={}&name={}&emoji={}'.format(self.user_id, self.name, self.emoji)
        if self.png_sticker:
            url += '&png_sticker={}'.format(self.png_sticker)
        if self.tgs_sticker:
            url += '&tgs_sticker={}'.format(self.tgs_sticker)
        if self.webm_sticker:
            url += '&webm_sticker={}'.format(self.webm_sticker)
        if self.mask_position:
            url += '&mask_position={}'.format(self.mask_position)
        r = requests_session.get(self.bot.bot_url + url, params=self.extra)
        if r.status_code != 200:
            self.bot.check(r.json(), url, params=self.extra)
        else:
            self.result = r.json().get('result')
            return self.result

    def __repr__(self):
        msg = self.result
        return str(msg)

class setStickerPositionInSet:
    def __init__(self, bot, sticker, position, **kwargs):
        self.bot = bot
        self.sticker = sticker
        self.position = position
        self.extra = kwargs

    def set_sticker_position_in_set(self):
        url = '/setStickerPositionInSet?sticker={}&position={}'.format(self.sticker, self.position)
        r = requests_session.get(self.bot.bot_url + url, params=self.extra)
        if r.status_code != 200:
            self.bot.check(r.json(), url, params=self.extra)
        else:
            self.result = r.json().get('result')
            return self.result

    def __repr__(self):
        msg = self.result
        return str(msg)

class deleteStickerFromSet:
    def __init__(self, bot, sticker, **kwargs):
        self.bot = bot
        self.sticker = sticker
        self.extra = kwargs

    def delete_sticker_from_set(self):
        url = '/deleteStickerFromSet?sticker={}'.format(self.sticker)
        r = requests_session.get(self.bot.bot_url + url, params=self.extra)
        if r.status_code != 200:
            self.bot.check(r.json(), url, params=self.extra)
        else:
            self.result = r.json().get('result')
            return self.result

    def __repr__(self):
        msg = self.result
        return str(msg)

class setStickerSetThumb:
    def __init__(self, bot, name, user_id, thumb=None, **kwargs):
        self.bot = bot
        self.name = name
        self.user_id = user_id
        self.thumb = thumb
        self.extra = kwargs

    def set_sticker_set_thumb(self):
        url = '/setStickerSetThumb?name={}&user_id={}'.format(self.name, self.user_id)
        if self.thumb:
            url += '&thumb={}'.format(self.thumb)
        r = requests_session.get(self.bot.bot_url + url, params=self.extra)
        if r.status_code != 200:
            self.bot.check(r.json(), url, params=self.extra)
        else:
            self.result = r.json().get('result')
            return self.result

    def __repr__(self):
        msg = self.result
        return str(msg)

# Own created methods.
class getPermissions:
    def __init__(self, bot, chat_id, user_id):
        self.bot = bot
        self.chat_id = chat_id
        self.user_id = user_id

    def get_permissions(self):
        if self.chat_id and not self.user_id:
            chat = getChat(bot=self.bot, chat_id=self.chat_id).get_chat()
            return getattr(chat, 'permissions', None)
        chat_member = getChatMember(bot=self.bot, chat_id=self.chat_id, user_id=self.user_id).get_chat_member()
        self.permissions = types.ChatMember(chat_member.__dict__).do()
        if self.permissions.status == 'member':
            chat = getChat(bot=self.bot, chat_id=self.chat_id).get_chat()
            chat_perms = chat.permissions
            self.permissions.can_manage_chat = chat_perms.can_change_info
            self.permissions.can_invite_users = chat_perms.can_invite_users
            self.permissions.can_send_messages = chat_perms.can_send_messages
            self.permissions.can_pin_messages = chat_perms.can_pin_messages
            self.permissions.can_restrict_members = False
            self.permissions.is_anonymous = False
        try:
            del self.permissions.status
        except:
            pass
        try:
            del self.permissions.user
        except:
            pass
        try:
            del self.permissions.custom_title
        except:
            pass
        self.permissions.can_ban = True if self.permissions.can_restrict_members is True else False
        self.permissions.can_unban = True if self.permissions.can_restrict_members is True else False
        self.permissions.is_admin = True if chat_member.status == 'administrator' else False
        self.permissions.is_creator = True if chat_member.status == 'creator' else False
        if not self.permissions.is_anonymous:
            self.permissions.is_anonymous = getattr(chat_member, 'is_anonymous', None)
        self.permissions.status = chat_member.status
        return self.permissions

    def __repr__(self):
        msg = self.__dict__
        return str(msg)

# Template.
'''
class :
    def __init__(self, bot, **kwargs):
        self.bot = bot
        self. =
        self.extra = kwargs

    def (self):
        url = '/'.format()
        r = requests_session.get(self.bot.bot_url + url, params=self.extra)
        if r.status_code != 200:
            self.bot.check(r.json(), url, params=self.extra)
        else:
            self.result = types.(r.json().get('result'))
            return self.result

    def __repr__(self):
        msg = self.result
        return str(msg)
'''