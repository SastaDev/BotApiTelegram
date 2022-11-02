import datetime

allowed_updates_all_types = [
    'message',
    'edited_message',
    'channel_post',
    'edited_channel_post',
    'inline_query',
    'chosen_inline_result',
    'callback_query',
    'shipping_query',
    'pre_checkout_query',
    'poll',
    'poll_answer',
    'my_chat_member',
    'chat_member',
    'chat_join_request'
    ] # along with chat_member

def Date(seconds):
    if isinstance(seconds, str):
        return seconds
    date = datetime.datetime.fromtimestamp(seconds)
    t = '{}:{}:{} {}/{}/{}'.format(date.hour, date.minute, date.second, date.day, date.month, date.year)
    return t

class DefaultSettings:
    def __init__(self):
        self.link_preview = True

class getMe:
    def __init__(self, get_me):
        try:
            get_me = get_me.__dict__
        except:
            pass
        self.first_name = get_me.get('first_name')
        self.username = get_me.get('username')
        self.bot_id = get_me.get('id')
        self.is_bot = get_me.get('is_bot')
        self.can_join_groups = get_me.get('can_join_groups')
        self.can_read_all_group_messages = get_me.get('can_read_all_group_messages')
        self.supports_inline_queries = get_me.get('supports_inline_queries')

    def get_dict(self):
        return self.__dict__

    def __repr__(self):
        msg = self.__dict__
        return str(msg)

class Updates:
    def __init__(self, update):
        self.original_update = update
        self.update_id = update.get('update_id')
        if update.get('message'):
            self.message = Message(update.get('message'))
        if update.get('edited_message'):
            self.edited_message = Message(update.get('edited_message'))
        if update.get('channel_post'):
            self.channel_post = Message(update.get('channel_post'))
        if update.get('edited_channel_post'):
            self.edited_channel_post = Message(update.get('edited_channel_post'))
        if update.get('inline_query'):
            self.inline_query = InlineQuery(update.get('inline_query'))
        if update.get('chosen_inline_result'):
            self.chosen_inline_result = ChosenInlineResult(update.get('chosen_inline_result'))
        if update.get('callback_query'):
            self.callback_query = CallbackQuery(self.bot, update.get('callback_query'))
        if update.get('shipping_query'):
            self.shipping_query = ShippingQuery(update.get('shipping_query'))
        if update.get('pre_checkout_query'):
            self.pre_checkout_query = PreCheckoutQuery(update.get('pre_checkout_query'))
        if update.get('poll'):
            self.poll = Poll(update.get('poll'))
        if update.get('poll_answer'):
            self.poll_answer = PollAnswer(update.get('poll_answer'))
        if update.get('my_chat_member'):
            self.my_chat_member = ChatMemberUpdated(update.get('my_chat_member'))
        if update.get('chat_member'):
            self.chat_member = ChatMemberUpdated(update.get('chat_member'))
        if update.get('chat_join_request'):
            self.chat_join_request = ChatJoinRequest(update.get('chat_join_request'))

    def get_dict(self):
        return self.__dict__

    def __repr__(self):
        msg = self.__dict__
        return str(msg)

    def __getattr__(self, key):
        return self.__dict__.get(key)

class User:
    def __init__(self, user):
        try:
            user = user.__dict__
        except:
            pass
        self.user_id = user.get('id') or user.get('user_id')
        self.is_bot = user.get('is_bot')
        self.first_name = user.get('first_name')
        self.last_name = user.get('last_name')
        self.username = user.get('username')
        if user.get('language_code'):
            self.language_code = user.get('language_code')
        if user.get('is_premium'):
            self.is_premium = user.get('is_premium')
        if user.get('added_to_attachment_menu'):
            self.added_to_attachment_menu = user.get('added_to_attachment_menu')

    def get_dict(self):
        return self.__dict__

    def __repr__(self):
        msg = self.__dict__
        return str(msg)

class Chat:
    def __init__(self, chat):
        try:
            chat = chat.__dict__
        except:
            pass
        self.chat_id = chat.get('id') or chat.get('chat_id')
        if chat.get('title'):
            self.title = chat.get('title')
            self.all_members_are_administrators = chat.get('all_members_are_administrators')
        else:
            self.first_name = chat.get('first_name')
            self.last_name = chat.get('last_name')
        self.username = chat.get('username')
        self.type = chat.get('type')
        self.is_group = True if chat.get('type') in ['group', 'supergroup'] else False
        self.is_private = True if chat.get('type') == 'private' else False
        if chat.get('photo'):
            self.photo = ChatPhoto(chat.get('photo'))
        if chat.get('bio'):
            self.bio = chat.get('bio')
        if chat.get('has_private_forwards'):
            self.has_private_forwards = chat.get('has_private_forwards')
        if chat.get('has_restricted_voice_and_video_messages'):
            self.has_restricted_voice_and_video_messages = chat.get('has_restricted_voice_and_video_messages')
        if chat.get('join_to_send_messages'):
            self.join_to_send_messages = chat.get('join_to_send_messages')
        if chat.get('join_by_request'):
            self.join_by_request = chat.get('join_by_request')
        if chat.get('description'):
            self.description = chat.get('description')
        if chat.get('invite_link'):
            self.invite_link = chat.get('invite_link')
        if chat.get('pinned_message'):
            self.pinned_message = Message(chat.get('pinned_message'))
        if chat.get('permissions'):
            self.permissions = ChatPermissions(chat.get('permissions'))
        if chat.get('slow_mode_delay'):
            self.slow_mode_delay = chat.get('slow_mode_delay')
        if chat.get('message_auto_delete_time'):
            self.message_auto_delete_time = chat.get('message_auto_delete_time')
        if chat.get('has_protected_content'):
            self.has_protected_content = chat.get('has_protected_content')
        if chat.get('sticker_set_name'):
            self.sticker_set_name = chat.get('sticker_set_name')
        if chat.get('can_set_sticker_set'):
            self.can_set_sticker_set = chat.get('can_set_sticker_set')
        if chat.get('linked_chat_id'):
            self.linked_chat_id = chat.get('linked_chat_id')
        if chat.get('location'):
            self.location = ChatLocation(chat.get('location'))

    def get_dict(self):
        return self.__dict__

    def __repr__(self):
        msg = self.__dict__
        return str(msg)

class Message:
    def __init__(self, raw_message):
        try:
            raw_message = raw_message.__dict__
        except:
            pass
        if raw_message.get('message_id'):
            self.message_id = raw_message.get('message_id')
        if raw_message.get('from'):
            self.from_user = User(raw_message.get('from'))
        if raw_message.get('sender_chat'):
            self.sender_chat = raw_message.get('sender_chat')
        if raw_message.get('date'):
            self.date = Date(raw_message.get('date'))
        if raw_message.get('chat'):
            self.chat = Chat(raw_message.get('chat'))
        if raw_message.get('my_chat_members'):
            self.my_chat_members = [User(x) for x in raw_message.get('my_chat_members')]
        if raw_message.get('forward_from'):
            self.forward_from = User(raw_message.get('forward_from'))
        if raw_message.get('forward_from_chat'):
            self.forward_from_chat = Chat(raw_message.get('forward_from_chat'))
        if raw_message.get('forward_from_message_id'):
            self.forward_from_message_id = raw_message.get('forward_from_message_id')
        if raw_message.get('forward_signature'):
            self.forward_signature = raw_message.get('forward_signature')
        if raw_message.get('forward_sender_name'):
            self.forward_sender_name = raw_message.get('forward_sender_name')
        if raw_message.get('forward_date'):
            self.forward_date = raw_message.get('forward_date')
        if raw_message.get('is_automatic_forward'):
            self.is_automatic_forward = raw_message.get('is_automatic_forward')
        if raw_message.get('reply_to_message'):
            self.reply_to_message = Message(raw_message.get('reply_to_message'))
            self.is_reply = True
        else:
            self.is_reply = False
        if raw_message.get('via_bot'):
            self.via_bot = User(raw_message.get('via_bot'))
        if raw_message.get('edit_date'):
            self.edit_date = raw_message.get('edit_date')
        if raw_message.get('has_protected_content'):
            self.has_protected_content = raw_message.get('has_protected_content')
        if raw_message.get('media_group_id'):
            self.media_group_id = raw_message.get('media_group_id')
        if raw_message.get('author_signature'):
            self.author_signature = raw_message.get('author_signature')
        if raw_message.get('text'):
            self.text = raw_message.get('text')
        if raw_message.get('entities'):
            self.entities = [MessageEntity(x) for x in raw_message.get('entities')]
        if raw_message.get('animation'):
            self.animation = Animation(raw_message.get('animation'))
        if raw_message.get('audio'):
            self.audio = Audio(raw_message.get('audio'))
        if raw_message.get('document'):
            self.document = Document(raw_message.get('document'))
        if raw_message.get('photo'):
            self.photo = [PhotoSize(x) for x in raw_message.get('photo')]
        '''
        if raw_message.get('sticker'):
            self.sticker = Sticker(raw_message.get('sticker'))
        '''
        if raw_message.get('video'):
            self.video = Video(raw_message.get('video'))
        if raw_message.get('video_note'):
            self.video_note = VideoNote(raw_message.get('video_note'))
        if raw_message.get('voice'):
            self.voice = Voice(raw_message.get('voice'))
        if raw_message.get('caption'):
            self.caption = raw_message.get('caption')
        if raw_message.get('caption_entities'):
            self.caption_entities = [MessageEntity(x) for x in raw_message.get('caption_entities')]
        if raw_message.get('contact'):
            self.contact = Contact(raw_message.get('contact'))
        if raw_message.get('dice'):
            self.dice = Dice(raw_message.get('dice'))
        if raw_message.get('game'):
            self.game = Game(raw_message.get('game'))
        if raw_message.get('poll'):
            self.poll = Poll(raw_message.get('poll'))
        if raw_message.get('venue'):
            self.venue = Venue(raw_message.get('venue'))
        if raw_message.get('location'):
            self.location = Location(raw_message.get('location'))
        if raw_message.get('new_chat_members'):
            self.new_chat_members = [User(x) for x in raw_message.get('new_chat_members')]
        if raw_message.get('left_chat_member'):
            self.left_chat_member = User(raw_message.get('left_chat_member'))
        if raw_message.get('new_chat_title'):
            self.new_chat_title = raw_message.get('new_chat_title')
        if raw_message.get('new_chat_photo'):
            self.new_chat_photo = [PhotoSize(x) for x in raw_message.get('new_chat_photo')]
        if raw_message.get('delete_chat_photo'):
            self.delete_chat_photo = raw_message.get('delete_chat_photo')
        if raw_message.get('group_chat_created'):
            self.group_chat_created = raw_message.get('group_chat_created')
        if raw_message.get('supergroup_chat_created'):
            self.supergroup_chat_created = raw_message.get('supergroup_chat_created')
        if raw_message.get('channel_chat_created'):
            self.channel_chat_created = raw_message.get('channel_chat_created')
        if raw_message.get('message_auto_delete_timer_changed'):
            self.message_auto_delete_timer_changed = MessageAutoDeleteTimerChanged(raw_message.get('message_auto_delete_timer_changed'))
        if raw_message.get('migrate_to_chat_id'):
            self.migrate_to_chat_id = raw_message.get('migrate_to_chat_id')
        if raw_message.get('migrate_from_chat_id'):
            self.migrate_from_chat_id = raw_message.get('migrate_from_chat_id')
        if raw_message.get('pinned_message'):
            self.pinned_message = Message(raw_message.get('pinned_message'))
        '''
        if raw_message.get('invoice'):
            self.invoice = Invoice(raw_message.get('invoice'))
        if raw_message.get('successful_payment'):
            self.successful_payment = SuccessfulPayment(raw_message.get('successful_payment'))
        '''
        if raw_message.get('connected_website'):
            self.connected_website = raw_message.get('connected_website')
        '''
        if raw_message.get('passport_data'):
            self.passport_data = PassportData(raw_message.get('passport_data'))
        '''
        if raw_message.get('proximity_alert_triggered'):
            self.proximity_alert_triggered = ProximityAlertTriggered(raw_message.get('proximity_alert_triggered'))
        if raw_message.get('video_chat_scheduled'):
            self.video_chat_scheduled = VideoChatScheduled(raw_message.get('video_chat_scheduled'))
        if raw_message.get('video_chat_started'):
            self.video_chat_started = VideoChatStarted(raw_message.get('video_chat_started'))
        if raw_message.get('video_chat_ended'):
            self.video_chat_ended = VideoChatEnded(raw_message.get('video_chat_ended'))
        if raw_message.get('video_chat_participants_invited'):
            self.video_chat_participants_invited = VideoChatParticipantsInvited(raw_message.get('video_chat_participants_invited'))
        if raw_message.get('web_app_data'):
            self.web_app_data = WebAppData(raw_message.get('web_app_data'))
        if raw_message.get('reply_markup'):
            self.reply_markup = InlineKeyboardMarkup(raw_message.get('reply_markup'))

    def get_dict(self):
        return self.__dict__

    def __repr__(self):
        msg = self.__dict__
        return str(msg)

class MessageId:
    def __init__(self, message_id):
        self.message_id = message_id

    def get_dict(self):
        return self.__dict__

    def __repr__(self):
        msg = self.__dict__
        return str(msg)

class MessageEntity:
    def __init__(self, message_entity):
        try:
            message_entity = message_entity.__dict__
        except:
            pass
        self.type = message_entity.get('type')
        self.offset = message_entity.get('offset')
        self.length = message_entity.get('length')
        if message_entity.get('url'):
            self.url = message_entity.get('url')
        if message_entity.get('user'):
            self.user = User(message_entity.get('user'))
        if message_entity.get('language'):
            self.language = message_entity.get('language')
        if message_entity.get('custom_emoji_id'):
            self.custom_emoji_id = message_entity.get('custom_emoji_id')

    def get_dict(self):
        return self.__dict__

    def __repr__(self):
        msg = self.__dict__
        return str(msg)

class PhotoSize:
    def __init__(self, photo_size):
        try:
            photo_size = photo_size.__dict__
        except:
            pass
        self.file_id = photo_size.get('file_id')
        self.file_unique_id = photo_size.get('file_unique_id')
        self.width = photo_size.get('width')
        self.height = photo_size.get('height')
        self.file_size = photo_size.get('file_size')

    def get_dict(self):
        return self.__dict__

    def __repr__(self):
        msg = self.__dict__
        return str(msg)

class Animation:
    def __init__(self, animation):
        try:
            animation = animation.__dict__
        except:
            pass
        self.file_id = animation.get('file_id')
        self.file_unique_id = animation.get('file_unique_id')
        self.width = animation.get('width')
        self.height = animation.get('height')
        self.duration = animation.get('duration')
        if animation.get('thumb'):
            self.thumb = PhotoSize(animation.get('thumb'))
        if animation.get('file_name'):
            self.file_name = animation.get('file_name')
        if animation.get('mime_type'):
            self.mime_type = animation.get('mime_type')
        if animation.get('file_size'):
            self.file_size = animation.get('file_size')

    def get_dict(self):
        return self.__dict__

    def __repr__(self):
        msg = self.__dict__
        return str(msg)

class Audio:
    def __init__(self, audio):
        try:
            audio = audio.__dict__
        except:
            pass
        self.file_id = audio.get('file_id')
        self.file_unique_id = audio.get('file_unique_id')
        self.duration = audio.get('duration')
        if audio.get('performer'):
            self.performer = audio.get('performer')
        if audio.get('title'):
            self.title = audio.get('title')
        if audio.get('file_name'):
            self.file_name = audio.get('file_name')
        if audio.get('mime_type'):
            self.mime_type = audio.get('mime_type')
        if audio.get('file_size'):
            self.file_size = audio.get('file_size')
        if audio.get('thumb'):
            self.thumb = PhotoSize(audio.get('thumb'))

    def get_dict(self):
        return self.__dict__

    def __repr__(self):
        msg = self.__dict__
        return str(msg)

class Document:
    def __init__(self, document):
        try:
            document = document.__dict__
        except:
            pass
        self.file_id = document.get('file_id')
        self.file_unique_id = document.get('file_unique_id')
        if document.get('thumb'):
            self.thumb = PhotoSize(document.get('thumb'))
        if document.get('file_name'):
            self.file_name = document.get('file_name')
        if document.get('mime_type'):
            self.mime_type = document.get('mime_type')
        if document.get('file_size'):
            self.file_size = document.get('file_size')

    def get_dict(self):
        return self.__dict__

    def __repr__(self):
        msg = self.__dict__
        return str(msg)

class Video:
    def __init__(self, video):
        try:
            video = video.__dict__
        except:
            pass
        self.file_id = video.get('file_id')
        self.file_unique_id = video.get('file_unique_id')
        self.width = video.get('width')
        self.height = video.get('height')
        self.duration = video.get('duration')
        if video.get('thumb'):
            self.thumb = PhotoSize(video.get('thumb'))
        if video.get('file_name'):
            self.file_name = video.get('file_name')
        if video.get('mime_type'):
            self.mime_type = video.get('mime_type')
        if video.get('file_size'):
            self.file_size = video.get('file_size')

    def get_dict(self):
        return self.__dict__

    def __repr__(self):
        msg = self.__dict__
        return str(msg)

class VideoNote:
    def __init__(self, video_note):
        try:
            video_note = video_note.__dict__
        except:
            pass
        self.file_id = video_note.get('file_id')
        self.file_unique_id = video_note.get('file_unique_id')
        self.length = video_note.get('length')
        self.duration = video_note.get('duration')
        if video_note.get('thumb'):
            self.thumb = PhotoSize(video_note.get('thumb'))
        if video_note.get('file_size'):
            self.file_size = video_note.get('file_size')

    def get_dict(self):
        return self.__dict__

    def __repr__(self):
        msg = self.__dict__
        return str(msg)

class Voice:
    def __init__(self, voice):
        try:
            voice = voice.__dict__
        except:
            pass
        self.file_id = voice.get('file_id')
        self.file_unique_id = voice.get('file_unique_id')
        self.duration = voice.get('duration')
        if voice.get('mime_type'):
            self.thumb = voice.get('mime_type')
        if voice.get('file_size'):
            self.file_size = voice.get('file_size')

    def get_dict(self):
        return self.__dict__

    def __repr__(self):
        msg = self.__dict__
        return str(msg)

class Contact:
    def __init__(self, contact):
        try:
            contact = contact.__dict__
        except:
            pass
        self.phone_number = contact.get('phone_number')
        self.first_name = contact.get('first_name')
        if contact.get('last_name'):
            self.last_name = contact.get('last_name')
        if contact.get('user_id'):
            self.user_id = contact.get('user_id')
        if contact.get('vcard'):
            self.vcard = contact.get('vcard')

    def get_dict(self):
        return self.__dict__

    def __repr__(self):
        msg = self.__dict__
        return str(msg)

class Dice:
    def __init__(self, dice):
        try:
            dice = dice.__dict__
        except:
            pass
        self.emoji = dice.get('emoji')
        self.value = dice.get('value')

    def get_dict(self):
        return self.__dict__

    def __repr__(self):
        msg = self.__dict__
        return str(msg)

class PollOption:
    def __init__(self, poll_option):
        try:
            poll_option = poll_option.__dict__
        except:
            pass
        self.text = poll_option.get('text')
        self.voter_count = poll_option.get('voter_count')

    def get_dict(self):
        return self.__dict__

    def __repr__(self):
        msg = self.__dict__
        return str(msg)

class PollAnswer:
    def __init__(self, poll_answer):
        try:
            poll_answer = poll_answer.__dict__
        except:
            pass
        self.poll_id = poll_answer.get('poll_id')
        self.user = User(poll_answer.get('user'))
        self.option_ids = poll_answer.get('option_ids')

    def get_dict(self):
        return self.__dict__

    def __repr__(self):
        msg = self.__dict__
        return str(msg)

class Poll:
    def __init__(self, poll):
        try:
            poll = poll.__dict__
        except:
            pass
        self.id = poll.get('id')
        self.question = poll.get('question')
        self.options = [PollOption(x) for x in poll.get('options')]
        self.total_voter_count = poll.get('total_voter_count')
        self.is_closed = poll.get('is_closed')
        self.is_anonymous = poll.get('is_anonymous')
        self.type = poll.get('type')
        self.allows_multiple_answers = poll.get('allows_multiple_answers')
        if poll.get('correct_option_id'):
            self.correct_option_id = poll.get('correct_option_id')
        if poll.get('explanation'):
            self.explanation = poll.get('explanation')
        if poll.get('explanation_entities'):
            self.explanation_entities = [MessageEntity(x) for x in poll.get('explanation_entities')]
        if poll.get('open_period'):
            self.open_period = poll.get('open_period')
        if poll.get('close_date'):
            self.close_date = poll.get('close_date')

    def get_dict(self):
        return self.__dict__

    def __repr__(self):
        msg = self.__dict__
        return str(msg)

class Location:
    def __init__(self, location):
        try:
            location = message.__dict__
        except:
            pass
        self.longitude = location.get('longitude')
        self.latitude = location.get('latitude')
        self.horizontal_accuracy = location.get('horizontal_accuracy')
        self.live_period = location.get('live_period')
        self.heading = location.get('heading')
        self.proximity_alert_radius = location.get('proximity_alert_radius')

    def get_dict(self):
        return self.__dict__

    def __repr__(self):
        msg = self.__dict__
        return str(msg)

class Venue:
    def __init__(self, venue):
        try:
            venue = venue.__dict__
        except:
            pass
        self.location = Location(venue.get('location'))
        self.title = venue.get('title')
        self.address = venue.get('address')
        if venue.get('foursquare_id'):
            self.foursquare_id = venue.get('foursquare_id')
        if venue.get('foursquare_type'):
            self.foursquare_type = venue.get('foursquare_type')
        if venue.get('google_place_id'):
            self.google_place_id = venue.get('google_place_id')
        if venue.get('google_place_type'):
            self.google_place_type = venue.get('google_place_type')

    def get_dict(self):
        return self.__dict__

    def __repr__(self):
        msg = self.__dict__
        return str(msg)

class WebAppData:
    def __init__(self, web_app_data):
        try:
            web_app_data = web_app_data.__dict__
        except:
            pass
        self.data = web_app_data.get('data')
        self.button_text = web_app_data.get('button_text')

    def get_dict(self):
        return self.__dict__

    def __repr__(self):
        msg = self.__dict__
        return str(msg)

class ProximityAlertTriggered:
    def __init__(self, proximity_alert_triggered):
        try:
            proximity_alert_triggered = proximity_alert_triggered.__dict__
        except:
            pass
        self.traveler = User(proximity_alert_triggered.get('traveler'))
        self.watcher = User(proximity_alert_triggered.get('watcher'))
        self.distance = proximity_alert_triggered.get('distance')

    def get_dict(self):
        return self.__dict__

    def __repr__(self):
        msg = self.__dict__
        return str(msg)

class MessageAutoDeleteTimerChanged:
    def __init__(self, message_auto_delete_timer_changed):
        try:
            message_auto_delete_timer_changed = message_auto_delete_timer_changed.__dict__
        except:
            pass
        self.message_auto_delete_time = message_auto_delete_timer_changed.get('message_auto_delete_time')

    def get_dict(self):
        return self.__dict__

    def __repr__(self):
        msg = self.__dict__
        return str(msg)

class VideoChatScheduled:
    def __init__(self, video_chat_scheduled):
        try:
            video_chat_scheduled = video_chat_scheduled.__dict__
        except:
            pass
        self.start_date = video_chat_scheduled.get('start_date')

    def get_dict(self):
        return self.__dict__

    def __repr__(self):
        msg = self.__dict__
        return str(msg)

class VideoChatStarted:
    def __init__(self, video_chat_started):
        pass

    def get_dict(self):
        return self.__dict__

    def __repr__(self):
        msg = self.__dict__
        return str(msg)

class VideoChatEnded:
    def __init__(self, video_chat_ended):
        try:
            video_chat_ended = video_chat_ended.__dict__
        except:
            pass
        self.duration = video_chat_ended.get('duration')

    def get_dict(self):
        return self.__dict__

    def __repr__(self):
        msg = self.__dict__
        return str(msg)

class VideoChatParticipantsInvited:
    def __init__(self, video_chat_participants_invited):
        try:
            video_chat_participants_invited = video_chat_participants_invited.__dict__
        except:
            pass
        self.users = [User(x) for x in video_chat_participants_invited.get('users')]

    def get_dict(self):
        return self.__dict__

    def __repr__(self):
        msg = self.__dict__
        return str(msg)

class UserProfilePhotos:
    def __init__(self, user_profile_photos):
        try:
            user_profile_photos = user_profile_photos.__dict__
        except:
            pass
        self.total_count = user_profile_photos.get('total_count')
        self.photos = [PhotoSize(x) for x in user_profile_photos.get('photos')]

    def get_dict(self):
        return self.__dict__

    def __repr__(self):
        msg = self.__dict__
        return str(msg)

class File:
    def __init__(self, file):
        try:
            file = file.__dict__
        except:
            pass
        self.file_id = file.get('file_id')
        self.file_unique_id = file.get('file_unique_id')
        if file.get('file_size'):
            self.file_size = file.get('file_size')
        if file.get('file_path'):
            self.file_path = file.get('file_path')

    def get_dict(self):
        return self.__dict__

    def __repr__(self):
        msg = self.__dict__
        return str(msg)

class WebAppInfo:
    def __init__(self, web_app_info):
        try:
            web_app_info = web_app_info.__dict__
        except:
            pass
        self.url = web_app_info.url

    def get_dict(self):
        return self.__dict__

    def __repr__(self):
        msg = self.__dict__
        return str(msg)

class ReplyKeyboardMarkup:
    def __init__(self, reply_keyboard_markup):
        try:
            reply_keyboard_markup = reply_keyboard_markup.__dict__
        except:
            pass
        self.keyboard = [[reply_keyboard_markup.get('keyboard')]]
        self.resize_keyboard = reply_keyboard_markup.get('resize_keyboard')
        self.one_time_keyboard = reply_keyboard_markup.get('one_time_keyboard')
        self.placeholder = reply_keyboard_markup.get('input_field_placeholder')
        self.selective = reply_keyboard_markup.get('selective')

    def get_dict(self):
        return self.__dict__

    def __repr__(self):
        msg = self.__dict__
        return str(msg)

class KeyboardButton:
    def __init__(self, keyboard_button):
        try:
            keyboard_button = keyboard_button.__dict__
        except:
            pass
        self.text = keyboard_button.get('text')
        if keyboard_button.get('request_contact'):
            self.request_contact = keyboard_button.get('request_contact')
        if keyboard_button.get('request_location'):
            self.request_location = keyboard_button.get('request_location')
        if keyboard_button.get('request_poll'):
            self.request_poll = KeyboardButtonPollType(keyboard_button.get('request_poll'))
        if keyboard_button.get('web_app'):
            self.web_app = WebAppInfo(keyboard_button.get('web_app'))

    def get_dict(self):
        return self.__dict__

    def __repr__(self):
        msg = self.__dict__
        return str(msg)

class KeyboardButtonPollType:
    def __init__(self, keyboard_button_poll_type):
        try:
            keyboard_button_poll_type = keyboard_button_poll_type.__dict__
        except:
            pass
        if keyboard_button_poll_type.get('type'):
            self.type = keyboard_button_poll_type.get('type')

    def get_dict(self):
        return self.__dict__

    def __repr__(self):
        msg = self.__dict__
        return str(msg)

class ReplyKeyboardRemove:
    def __init__(self, reply_keyboard_remove):
        try:
            reply_keyboard_remove = reply_keyboard_remove.__dict__
        except:
            pass
        self.remove_keyboard = reply_keyboard_remove.get('remove_keyboard')
        if reply_keyboard_remove.get('selective'):
            self.selective = keyboard_button_poll_type.get('selective')

    def get_dict(self):
        return self.__dict__

    def __repr__(self):
        msg = self.__dict__
        return str(msg)

class InlineKeyboardMarkup:
    def __init__(self, inline_keyboard_markup):
        self.inline_keyboard = inline_keyboard_markup

class InlineKeyboardButton:
    def __init__(self, inline_keyboard_button):
        try:
            inline_keyboard_button = inline_keyboard_button.__dict__
        except:
            pass
        self.text = inline_keyboard_button.get('text')
        if inline_keyboard_button.get('url'):
            self.url = inline_keyboard_button.get('url')
        if inline_keyboard_button.get('callback_data'):
            self.callback_data = inline_keyboard_button.get('callback_data')
        if inline_keyboard_button.get('web_app'):
            self.web_app = WebAppInfo(inline_keyboard_button.get('web_app'))
        if inline_keyboard_button.get('login_url'):
            self.login_url = LoginUrl(inline_keyboard_button.get('login_url'))
        if inline_keyboard_button.get('switch_inline_query'):
            self.switch_inline_query = inline_keyboard_button.get('switch_inline_query')
        if inline_keyboard_button.get('switch_inline_query_current_chat'):
            self.switch_inline_query_current_chat = inline_keyboard_button.get('switch_inline_query_current_chat')
        if inline_keyboard_button.get('callback_game'):
            self.callback_game = CallbackGame(inline_keyboard_button.get('callback_game'))
        if inline_keyboard_button.get('pay'):
            self.pay = inline_keyboard_button.get('pay')

    def get_dict(self):
        return self.__dict__

    def __repr__(self):
        msg = self.__dict__
        return str(msg)

class LoginUrl:
    def __init__(self, login_url):
        try:
            login_url = login_url.__dict__
        except:
            pass
        self.url = login_url.get('url')
        self.forward_text = login_url.get('forward_text')
        self.bot_username = login_url.get('bot_username')
        self.request_write_access = login_url.get('request_write_access')

    def get_dict(self):
        return self.__dict__

    def __repr__(self):
        msg = self.__dict__
        return str(msg)

class CallbackGame:
    def __init__(self, callback_game):
        try:
            callback_game = callback_game.__dict__
        except:
            pass

    def get_dict(self):
        return self.__dict__

    def __repr__(self):
        msg = self.__dict__
        return str(msg)

class ForceReply:
    def __init__(self, force_reply):
        try:
            force_reply = force_reply.__dict__
        except:
            pass
        self.force_reply = force_reply.get('force_reply')
        self.input_field_placeholder = force_reply.get('input_field_placeholder')

    def get_dict(self):
        return self.__dict__

    def __repr__(self):
        msg = self.__dict__
        return str(msg)

class ChatPhoto:
    def __init__(self, chat_photo):
        try:
            chat_photo = chat_photo.__dict__
        except:
            pass
        self.small_file_id = chat_photo.get('small_file_id')
        self.small_file_unique_id = chat_photo.get('small_file_unique_id')
        self.big_file_id = chat_photo.get('big_file_id')
        self.big_file_unique_id = chat_photo.get('big_file_unique_id')

    def get_dict(self):
        return self.__dict__

    def __repr__(self):
        msg = self.__dict__
        return str(msg)

class ChatInviteLink:
    def __init__(self, chat_invite_link):
        try:
            chat_invite_link = chat_invite_link.__dict__
        except:
            pass
        self.invite_link = chat_invite_link.get('invite_link')
        if chat_invite_link.get('creator'):
            self.creator = User(chat_invite_link.get('creator'))
        if chat_invite_link.get('creates_join_request'):
            self.creates_join_request = chat_invite_link.get('creates_join_request')
        if chat_invite_link.get('is_primary'):
            self.is_primary = chat_invite_link.get('is_primary')
        if chat_invite_link.get('is_revoked'):
            self.is_revoked = chat_invite_link.get('is_revoked')
        if chat_invite_link.get('name'):
            self.name = chat_invite_link.get('name')
        if chat_invite_link.get('expire_date'):
            self.expire_date = chat_invite_link.get('expire_date')
        if chat_invite_link.get('member_limit'):
            self.member_limit = chat_invite_link.get('member_limit')
        if chat_invite_link.get('pending_join_request_count'):
            self.pending_join_request_count = chat_invite_link.get('pending_join_request_count')

    def get_dict(self):
        return self.__dict__

    def __repr__(self):
        msg = self.__dict__
        return str(msg)
class ChatAdministratorRights:
    def __init__(self, chat_administrator_rights):
        try:
            chat_administrator_rights = chat_administrator_rights.__dict__
        except:
            pass
        self.is_anonymous = chat_administrator_rights.get('is_anonymous')
        self.can_manage_chat = chat_administrator_rights.get('can_manage_chat')
        self.can_delete_messages = chat_administrator_rights.get('can_delete_messages')
        self.can_manage_video_chats = chat_administrator_rights.get('can_manage_video_chats')
        self.can_restrict_members = chat_administrator_rights.get('can_restrict_members')
        self.can_promote_members = chat_administrator_rights.get('can_promote_members')
        self.can_change_info = chat_administrator_rights.get('can_change_info')
        self.can_invite_users = chat_administrator_rights.get('can_invite_users')
        self.can_post_messages = chat_administrator_rights.get('can_post_messages')
        self.can_edit_messages = chat_administrator_rights.get('can_edit_messages')
        self.can_pin_messages = chat_administrator_rights.get('can_pin_messages')

    def get_dict(self):
        return self.__dict__

    def __repr__(self):
        msg = self.__dict__
        return str(msg)

class ChatMember:
    def __init__(self, chat_member):
        try:
            chat_member = chat_member.__dict__
        except:
            pass
        self.chat_member = chat_member

    def do(self):
        if isinstance(self.chat_member, list):
            j = []
            for i in self.chat_member:
                j.append(ChatMemberAdministrator(i))
            return j
        status = self.chat_member.get('status')
        if status == 'member':
            return ChatMemberMember(self.chat_member)
        elif status == 'administrator':
            return ChatMemberAdministrator(self.chat_member)
        elif status == 'creator':
            return ChatMemberOwner(self.chat_member)
        elif status == 'left':
            return ChatMemberLeft(self.chat_member)
        elif status == 'kicked':
            return ChatMemberRestricted(self.chat_member)
        elif status == 'restricted':
            return ChatMemberRestricted(self.chat_member)

    def get_dict(self):
        return self.__dict__

    def __repr__(self):
        msg = self.__dict__
        return str(msg)

class ChatMemberOwner:
    def __init__(self, chat_member_owner):
        try:
            chat_member_owner = chat_member_owner.__dict__
        except:
            pass
        self.status = chat_member_owner.get('status')
        self.user = User(chat_member_owner.get('user'))
        self.is_anonymous = chat_member_owner.get('is_anonymous')
        self.custom_title = chat_member_owner.get('custom_title')
        self.can_be_edited = True
        self.can_manage_chat = True
        self.can_delete_messages = True
        self.can_manage_video_chats = True
        self.can_restrict_members = True
        self.can_promote_members = True
        self.can_change_info = True
        self.can_invite_users = True
        self.can_post_messages = True
        self.can_edit_messages = True
        self.can_pin_messages = True

    def get_dict(self):
        return self.__dict__

    def __repr__(self):
        msg = self.__dict__
        return str(msg)

class ChatMemberAdministrator:
    def __init__(self, chat_member_administrator):
        try:
            chat_member_administrator = chat_member_administrator.__dict__
        except:
            pass
        self.status = chat_member_administrator.get('status')
        self.user = User(chat_member_administrator.get('user'))
        self.can_be_edited = chat_member_administrator.get('can_be_edited')
        self.is_anonymous = chat_member_administrator.get('is_anonymous')
        self.can_manage_chat = chat_member_administrator.get('can_manage_chat')
        self.can_delete_messages = chat_member_administrator.get('can_delete_messages')
        self.can_manage_video_chats = chat_member_administrator.get('can_manage_video_chats')
        self.can_restrict_members = chat_member_administrator.get('can_restrict_members')
        self.can_promote_members = chat_member_administrator.get('can_promote_members')
        self.can_change_info = chat_member_administrator.get('can_change_info')
        self.can_invite_users = chat_member_administrator.get('can_invite_users')
        self.can_post_messages = chat_member_administrator.get('can_post_messages')
        self.can_edit_messages = chat_member_administrator.get('can_edit_messages')
        self.can_pin_messages = chat_member_administrator.get('can_pin_messages')
        self.custom_title = chat_member_administrator.get('custom_title')

    def get_dict(self):
        return self.__dict__

    def __repr__(self):
        msg = self.__dict__
        return str(msg)

class ChatMemberMember:
    def __init__(self, chat_member_member):
        try:
            chat_member_member = chat_member_member.__dict__
        except:
            pass
        self.status = chat_member_member.get('status')
        self.user = User(chat_member_member.get('user'))

    def get_dict(self):
        return self.__dict__

    def __repr__(self):
        msg = self.__dict__
        return str(msg)

class ChatMemberRestricted:
    def __init__(self, chat_member_restricted):
        try:
            chat_member_restricted = chat_member_restricted.__dict__
        except:
            pass
        self.status = chat_member_restricted.get('status')
        self.user = User(chat_member_restricted.get('user'))
        self.is_member = chat_member_restricted.get('is_member')
        self.can_change_info = chat_member_restricted.get('can_change_info')
        self.can_invite_users = chat_member_restricted.get('can_invite_users')
        self.can_pin_messages = chat_member_restricted.get('can_pin_messages')
        self.can_send_messages = chat_member_restricted.get('can_send_messages')
        self.can_send_media_messages = chat_member_restricted.get('can_send_media_messages')
        self.can_send_polls = chat_member_restricted.get('can_send_polls')
        self.can_send_other_messages = chat_member_restricted.get('can_send_other_messages')
        self.can_add_web_page_previews = chat_member_restricted.get('can_add_web_page_previews')
        self.until_date = chat_member_restricted.get('until_date')

    def get_dict(self):
        return self.__dict__

    def __repr__(self):
        msg = self.__dict__
        return str(msg)

class ChatMemberLeft:
    def __init__(self, chat_member_left):
        try:
            chat_member_left = chat_member_left.__dict__
        except:
            pass
        self.status = chat_member_left.get('status')
        self.user = User(chat_member_left.get('user'))

    def get_dict(self):
        return self.__dict__

    def __repr__(self):
        msg = self.__dict__
        return str(msg)

class ChatMemberBanned:
    def __init__(self, chat_member_banned):
        try:
            chat_member_banned = chat_member_banned.__dict__
        except:
            pass
        self.status = chat_member_banned.get('status')
        self.user = User(chat_member_banned.get('user'))
        self.until_date = chat_member_banned.get('until_date')

    def get_dict(self):
        return self.__dict__

    def __repr__(self):
        msg = self.__dict__
        return str(msg)

class ChatMemberUpdated:
    def __init__(self, chat_member_updated):
        try:
            chat_member_updated = chat_member_updated.__dict__
        except:
            pass
        self.chat = Chat(chat_member_updated.get('chat'))
        self.from_user = User(chat_member_updated.get('from'))
        self.date = Date(chat_member_updated.get('date'))
        self.old_chat_member = ChatMember(chat_member_updated.get('old_chat_member')).do()
        self.new_chat_member = ChatMember(chat_member_updated.get('new_chat_member')).do()
        if chat_member_updated.get('invite_link'):
            self.invite_link = ChatInviteLink(chat_member_updated.get('invite_link'))

    def get_dict(self):
        return self.__dict__

    def __repr__(self):
        msg = self.__dict__
        return str(msg)

class ChatJoinRequest:
    def __init__(self, chat_join_request):
        try:
            chat_join_request = chat_join_request.__dict__
        except:
            pass
        self.chat = Chat(chat_join_request.get('status'))
        self.user = User(chat_join_request.get('user'))
        self.date = chat_join_request.get('date')
        self.bio = chat_join_request.get('bio')
        self.invite_link = ChatInviteLink(chat_join_request.get('invite_link'))

    def get_dict(self):
        return self.__dict__

    def __repr__(self):
        msg = self.__dict__
        return str(msg)

class ChatPermissions:
    def __init__(self, chat_permissions):
        try:
            chat_permissions = chat_permissions.__dict__
        except:
            pass
        self.can_send_messages = chat_permissions.get('can_send_messages')
        self.can_send_media_messages = chat_permissions.get('can_send_media_messages')
        self.can_send_polls = chat_permissions.get('can_send_polls')
        self.can_send_other_messages = chat_permissions.get('can_send_other_messages')
        self.can_add_web_page_previews = chat_permissions.get('can_add_web_page_previews')
        self.can_change_info = chat_permissions.get('can_change_info')
        self.can_invite_users = chat_permissions.get('can_invite_users')
        self.can_pin_messages = chat_permissions.get('can_pin_messages')

    def get_json(self):
        return self.__dict__

    def __repr__(self):
        msg = self.__dict__
        return str(msg)

class ChatLocation:
    def __init__(self, chat_location):
        try:
            chat_location = chat_location.__dict__
        except:
            pass
        self.location = Location(chat_location.get('location'))
        self.address = chat_location.get('address')

    def get_dict(self):
        return self.__dict__

    def __repr__(self):
        msg = self.__dict__
        return str(msg)

class BotCommand:
    def __init__(self, bot_command):
        try:
            bot_command = bot_command.__dict__
        except:
            pass
        self.command = command(chat_location.get('command'))
        self.description = bot_command.get('description')

    def get_dict(self):
        return self.__dict__

    def __repr__(self):
        msg = self.__dict__
        return str(msg)

class BotCommandScope:
    def __init__(self, bot_command_scope):
        try:
            bot_command_scope = bot_command_scope.__dict__
        except:
            pass
        self.bot_command_scope = bot_command_scope

    def do(self):
        if isinstance(self.bot_command_scope, BotCommandScopeDefault):
            return BotCommandScopeDefault(self.bot_command_scope)
        elif isinstance(self.bot_command_scope, BotCommandScopeAllPrivateChats):
            return BotCommandScopeAllPrivateChats(self.bot_command_scope)
        elif isinstance(self.bot_command_scope, BotCommandScopeAllGroupChats):
            return BotCommandScopeAllGroupChats(self.bot_command_scope)
        elif isinstance(self.bot_command_scope, BotCommandScopeChatAdministrators):
            return BotCommandScopeChatAdministrators(self.bot_command_scope)
        elif isinstance(self.bot_command_scope, BotCommandScopeChat):
            return BotCommandScopeChat(self.bot_command_scope)
        elif isinstance(self.bot_command_scope, BotCommandScopeChatAdministrators):
            return BotCommandScopeChatAdministrators(self.bot_command_scope)
        elif isinstance(self.bot_command_scope, BotCommandScopeChatMember):
            return BotCommandScopeChatMember(self.bot_command_scope)

    def get_dict(self):
        return self.__dict__

    def __repr__(self):
        msg = self.__dict__
        return str(msg)

class BotCommandScopeDefault:
    def __init__(self, bot_command_scope_default):
        try:
            bot_command_scope_default = bot_command_scope_default.__dict__
        except:
            pass
        self.type = bot_command_scope_default.get('type')

    def get_dict(self):
        return self.__dict__

    def __repr__(self):
        msg = self.__dict__
        return str(msg)

class BotCommandScopeAllPrivateChats:
    def __init__(self, bot_command_scope_all_private_chats):
        try:
            bot_command_scope_all_private_chats = bot_command_scope_all_private_chats.__dict__
        except:
            pass
        self.type = bot_command_scope_all_private_chats.get('type')

    def get_dict(self):
        return self.__dict__

    def __repr__(self):
        msg = self.__dict__
        return str(msg)

class BotCommandScopeAllGroupChats:
    def __init__(self, bot_command_scope_all_group_chats):
        try:
            bot_command_scope_all_group_chats = bot_command_scope_all_group_chats.__dict__
        except:
            pass
        self.type = bot_command_scope_all_group_chats.get('type')

    def get_dict(self):
        return self.__dict__

    def __repr__(self):
        msg = self.__dict__
        return str(msg)

class BotCommandScopeAllChatAdministrators:
    def __init__(self, bot_command_scope_all_chat_administrators):
        try:
            bot_command_scope_all_chat_administrators = bot_command_scope_all_chat_administrators.__dict__
        except:
            pass
        self.type = bot_command_scope_all_chat_administrators.get('type')

    def get_dict(self):
        return self.__dict__

    def __repr__(self):
        msg = self.__dict__
        return str(msg)

class BotCommandScopeChat:
    def __init__(self, bot_command_scope_chat):
        try:
            bot_command_scope_chat = bot_command_scope_chat.__dict__
        except:
            pass
        self.type = bot_command_scope_chat.get('type')
        self.chat_id = bot_command_scope_chat.get('chat_id')

    def get_dict(self):
        return self.__dict__

    def __repr__(self):
        msg = self.__dict__
        return str(msg)

class BotCommandScopeChatAdministrators:
    def __init__(self, bot_command_scope_chat_administrators):
        try:
            bot_command_scope_chat_administrators = bot_command_scope_chat_administrators.__dict__
        except:
            pass
        self.type = bot_command_scope_chat_administrators.get('type')
        self.chat_id = bot_command_scope_chat_administrators.get('chat_id')

    def get_dict(self):
        return self.__dict__

    def __repr__(self):
        msg = self.__dict__
        return str(msg)

class BotCommandScopeChatMember:
    def __init__(self, bot_command_scope_chat_members):
        try:
            bot_command_scope_chat_members = bot_command_scope_chat_members.__dict__
        except:
            pass
        self.type = bot_command_scope_chat_members.get('type')
        self.chat_id = bot_command_scope_chat_members.get('chat_id')
        self.user_id = bot_command_scope_chat_members.get('user_id')

    def get_dict(self):
        return self.__dict__

    def __repr__(self):
        msg = self.__dict__
        return str(msg)

class MenuButton:
    def __init__(self, menu_button):
        try:
            menu_button = menu_button.__dict__
        except:
            pass
        self.menu_button = menu_button

    def do(self):
        if isinstance(self.menu_button, MenuButtonCommands):
            return MenuButtonCommands(self.menu_button)
        elif isinstance(self.menu_button, MenuButtonWebApp):
            return MenuButtonWebApp(self.menu_button)
        elif isinstance(self.menu_button, MenuButtonDefault):
            return MenuButtonDefault(self.menu_button)

    def get_dict(self):
        return self.__dict__

    def __repr__(self):
        msg = self.__dict__
        return str(msg)

class MenuButtonCommands:
    def __init__(self, menu_button_commands):
        try:
            menu_button_commands = menu_button_commands.__dict__
        except:
            pass
        self.type = menu_button_commands.get('type')

    def get_dict(self):
        return self.__dict__

    def __repr__(self):
        msg = self.__dict__
        return str(msg)

class MenuButtonWebApp:
    def __init__(self, menu_button_web_app):
        try:
            menu_button_web_app = menu_button_web_app.__dict__
        except:
            pass
        self.type = menu_button_web_app.get('type')
        self.text = menu_button_web_app.get('text')
        self.web_app = WebAppInfo(menu_button_web_app.get('web_app'))

    def get_dict(self):
        return self.__dict__

    def __repr__(self):
        msg = self.__dict__
        return str(msg)

class MenuButtonDefault:
    def __init__(self, menu_button_default):
        try:
            menu_button_default = menu_button_default.__dict__
        except:
            pass
        self.type = menu_button_default.get('type')

    def get_dict(self):
        return self.__dict__

    def __repr__(self):
        msg = self.__dict__
        return str(msg)

class ResponseParameters:
    def __init__(self, response_parameters):
        try:
            response_parameters = response_parameters.__dict__
        except:
            pass
        if response_parameters.get('migrate_to_chat_id'):
            self.migrate_to_chat_id = response_parameters.get('migrate_to_chat_id')
        if response_parameters.get('retry_after'):
            self.retry_after = response_parameters.get('retry_after')

    def get_dict(self):
        return self.__dict__

    def __repr__(self):
        msg = self.__dict__
        return str(msg)

class InputMedia:
    def __init__(self, input_media):
        try:
            input_media = input_media.__dict__
        except:
            pass
        self.input_media = input_media

    def do(self):
        if isinstance(self.input_media, InputMediaPhoto):
            return InputMediaPhoto(self.input_media)
        elif isinstance(self.input_media, InputMediaVideo):
            return InputMediaVideo(self.input_media)
        elif isinstance(self.input_media, InputMediaAnimation):
            return InputMediaAnimation(self.input_media)
        elif isinstance(self.input_media, InputMediaAudio):
            return InputMediaAudio(self.input_media)
        elif isinstance(self.input_media, InputMediaDocument):
            return InputMediaDocument(self.input_media)

    def get_dict(self):
        return self.__dict__

    def __repr__(self):
        msg = self.__dict__
        return str(msg)

class InputMediaPhoto:
    def __init__(self, input_media_photo):
        try:
            input_media_photo = input_media_photo.__dict__
        except:
            pass
        self.type = input_media_photo.get('type')
        self.media = input_media_photo.get('media')
        self.caption = input_media_photo.get('caption')
        self.parse_mode = input_media_photo.get('parse_mode')
        self.caption_entities = [MessageEntity(x) for x in input_media_photo.get('caption_entities')]

    def get_dict(self):
        return self.__dict__

    def __repr__(self):
        msg = self.__dict__
        return str(msg)

class InputMediaVideo:
    def __init__(self, input_media_video):
        try:
            input_media_video = input_media_video.__dict__
        except:
            pass
        self.type = input_media_video.get('type')
        self.media = input_media_video.get('media')
        self.thumb = input_media_video.get('thumb')
        self.caption = input_media_video.get('caption')
        self.parse_mode = input_media_video.get('parse_mode')
        self.caption_entities = [MessageEntity(x) for x in input_media_video.get('caption_entities')]
        self.width = input_media_video.get('width')
        self.height = input_media_video.get('height')
        self.duration = input_media_video.get('duration')
        self.supports_streaming = input_media_video.get('supports_streaming')

    def get_dict(self):
        return self.__dict__

    def __repr__(self):
        msg = self.__dict__
        return str(msg)

class InputMediaAnimation:
    def __init__(self, input_media_animation):
        try:
            input_media_animation = input_media_animation.__dict__
        except:
            pass
        self.type = input_media_animation.get('type')
        self.media = input_media_animation.get('media')
        self.thumb = input_media_animation.get('thumb')
        self.caption = input_media_animation.get('caption')
        self.parse_mode = input_media_animation.get('parse_mode')
        self.caption_entities = input_media_animation.get('caption_entities')
        self.width = input_media_animation.get('width')
        self.height = input_media_animation.get('height')
        self.duration = input_media_animation.get('duration')

    def get_dict(self):
        return self.__dict__

    def __repr__(self):
        msg = self.__dict__
        return str(msg)

class InputMediaAudio:
    def __init__(self, input_media_audio):
        try:
            input_media_audio = input_media_audio.__dict__
        except:
            pass
        self.type = input_media_audio.get('type')
        self.media = input_media_audio.get('media')
        self.thumb = input_media_audio.get('thumb')
        self.caption = input_media_audio.get('caption')
        self.parse_mode = input_media_audio.get('parse_mode')
        self.caption_entities = [MessageEntity(x) for x in input_media_audio.get('caption_entities')]
        self.duration = input_media_audio.get('duration')
        self.performer = input_media_audio.get('performer')
        self.title = input_media_audio.get('title')

    def get_dict(self):
        return self.__dict__

    def __repr__(self):
        msg = self.__dict__
        return str(msg)

class InputMediaDocument:
    def __init__(self, input_media_document):
        try:
            input_media_document = input_media_document.__dict__
        except:
            pass
        self.type = input_media_document.get('type')
        self.media = input_media_document.get('media')
        self.thumb = input_media_document.get('thumb')
        self.caption = input_media_document.get('caption')
        self.parse_mode = input_media_document.get('parse_mode')
        self.caption_entities = [MessageEntity(x) for x in input_media_document.get('caption_entities')]
        self.disable_content_type_detection = input_media_document.get('disable_content_type_detection')

    def get_dict(self):
        return self.__dict__

    def __repr__(self):
        msg = self.__dict__
        return str(msg)
















































class InlineQuery:
    def __init__(self, inline_query):
        try:
            inline_query = inline_query.__dict__
        except:
            pass
        self.id = inline_query.get('id')
        self.from_user = inline_query.get('from')
        self.offset = inline_query.get('offset')
        if inline_query.get('chat_type'):
            self.chat_type = inline_query.get('chat_type')
        if inline_query.get('location'):
            self.location = Location(inline_query.get('location'))

    def get_dict(self):
        return self.__dict__

    def __repr__(self):
        msg = self.__dict__
        return str(msg)

class ChosenInlineResult:
    def __init__(self, chosen_inline_result):
        try:
            chosen_inline_result = chosen_inline_result.__dict__
        except:
            pass
        self.result_id = chosen_inline_result.get('result_id')
        self.from_user = chosen_inline_result.get('from')
        if chosen_inline_result.get('location'):
            self.location = Location(chosen_inline_result.get('location'))
        if chosen_inline_result.get('inline_message_id'):
            self.inline_message_id = chosen_inline_result.get('inline_message_id')
        self.query = chosen_inline_result.get('query')

    def get_dict(self):
        return self.__dict__

    def __repr__(self):
        msg = self.__dict__
        return str(msg)

class ShippingQuery:
    def __init__(self, shipping_query):
        try:
            shipping_query = shipping_query.__dict__
        except:
            pass
        self.id = shipping_query.get('id')
        self.from_user = User(shipping_query.get('from'))
        self.invoice_payload = shipping_query.get('invoice_payload')
        self.shipping_address = ShippingAddress(shipping_query.get('shipping_address'))

    def get_dict(self):
        return self.__dict__

    def __repr__(self):
        msg = self.__dict__
        return str(msg)

class ShippingAddress:
    def __init__(self, shipping_address):
        try:
            shipping_address = shipping_address.__dict__
        except:
            pass
        self.country_code = shipping_address.get('country_code')
        self.state = shipping_address.get('state')
        self.city = shipping_address.get('city')
        self.street_line1 = shipping_address.get('street_line1')
        self.street_line2 = shipping_address.get('street_line2')
        self.post_code = shipping_address.get('post_code')

    def get_dict(self):
        return self.__dict__

    def __repr__(self):
        msg = self.__dict__
        return str(msg)

class CallbackQuery:
    def __init__(self, callback_query):
        try:
            callback_query = callback_query.__dict__
        except:
            pass
        self.callback_query_id = callback_query.get('id')
        self.from_user = User(callback_query.get('from'))
        if callback_query.get('message'):
            self.message = Message(callback_query.get('message'))
        if callback_query.get('inline_message_id'):
            self.inline_message_id = callback_query.get('inline_message_id')
        self.chat_instance = callback_query.get('chat_instance')
        if callback_query.get('data'):
            self.data = callback_query.get('data')
        if callback_query.get('game_short_name'):
            self.game_short_name = callback_query.get('game_short_name')

    def get_dict(self):
        return self.__dict__

    def __repr__(self):
        msg = self.__dict__
        return str(msg)

# Own created types.
class Message_:
    def __init__(self, bot, msg):
        self.bot = bot
        self.msg = msg
        self.chat_type = getattr(msg.chat, 'type', None)
        self.is_private = True if self.chat_type == 'private' else False
        self.is_channel = True if self.chat_type == 'channel' else False
        self.is_group = True if self.chat_type == 'group' else False
        self.is_forward = True if getattr(msg, 'forward_from', None) else False

    def reply(self, text, reply_to=None, link_preview=True, parse_mode='markdown', **kwargs):
        if not getattr(self, 'message_id', None):
            self.message_id = None
        chat_id = self.chat.chat_id
        r = self.bot.send_message(chat_id=chat_id, text=text, reply_to=self.message_id, link_preview=link_preview, parse_mode=parse_mode, **kwargs)
        return r

    def edit(self, text, link_preview=True, parse_mode='markdown', **kwargs):
        chat_id = self.chat.chat_id
        e = self.bot.edit_message(chat_id=chat_id, message_id=self.message_id, text=text, link_preview=link_preview, parse_mode=parse_mode, **kwargs)
        return e

    def delete(self):
        d = self.bot.delete_message(chat_id=self.chat.chat_id, message_id=self.message_id)
        return d

    def __getattr__(self, a):
        return getattr(self.msg, a)

    def __repr__(self):
        msg = self.msg.__dict__
        return str(msg)

class CallbackQuery_:
    def __init__(self, bot, callback_query):
        self.bot = bot
        self.callback_query = callback_query
        self.message = callback_query.message
        self.message_id = callback_query.message.message_id
        self.chat = callback_query.message.chat

    def reply(self, text, reply_to=None, link_preview=True, parse_mode='markdown', **kwargs):
        if not getattr(self, 'message_id', None):
            self.message_id = None
        chat_id = self.chat.chat_id
        r = self.bot.send_message(chat_id=chat_id, text=text, reply_to=self.message_id, link_preview=link_preview, parse_mode=parse_mode, **kwargs)
        return r

    def edit(self, text, link_preview=True, parse_mode='markdown', **kwargs):
        chat_id = self.chat.chat_id
        e = self.bot.edit_message(chat_id=chat_id, message_id=self.message_id, text=text, link_preview=link_preview, parse_mode=parse_mode, **kwargs)
        return e

    def delete(self):
        d = self.bot.delete_message(chat_id=self.chat.chat_id, message_id=self.message_id)
        return d

    def answer(self, text=None, show_alert=False, url=None, cache_time=0, **kwargs):
        ans = self.bot.answer_callback_query(
            callback_query_id=self.callback_query.callback_query_id,
            text=text,
            show_alert=show_alert,
            url=url,
            cache_time=cache_time,
            **kwargs
            )
        return ans

    def __repr__(self):
        msg = self.callback_query.__dict__
        return str(msg)

class BotAdded:
    def __init__(self, message):
        try:
            message = message.__dict__
        except:
            pass
        self.chat = Chat(message.get('chat'))
        self.added = User(message.get('new_chat_member'))
        self.added_by = User(message.get('from_user'))
        self.date = Date(message.get('date'))
        self.old_status = message.get('old_chat_member')

    def get_dict(self):
        return self.__dict__

    def __repr__(self):
        msg = self.__dict__
        return str(msg)

class ChatJoined:
    def __init__(self, chat_joined):
        try:
            chat_joined = chat_joined.__dict__
        except:
            pass
        self.chat = Chat(chat_joined.get('chat'))
        self.joined_by = User(chat_joined.get('from_user'))
        self.date = Date(chat_joined.get('date'))
        self.old_status = chat_joined.get('old_chat_member')
        self.permissions = chat_joined.get('new_chat_member')
        self.invite_link = chat_joined.get('invite_link')

    def get_dict(self):
        return self.__dict__

    def __repr__(self):
        msg = self.__dict__
        return str(msg)

class ChatLeft:
    def __init__(self, chat_left):
        try:
            chat_left = chat_left.__dict__
        except:
            pass
        self.chat = Chat(chat_left.get('chat'))
        self.left_by = User(chat_left.get('from_user'))
        self.date = Date(chat_left.get('date'))
        self.old_status = chat_left.get('old_chat_member')
        self.permissions = chat_left.get('new_chat_member')
        self.invite_link = chat_left.get('invite_link')

    def get_dict(self):
        return self.__dict__

    def __repr__(self):
        msg = self.__dict__
        return str(msg)

class ChatAdded:
    def __init__(self, chat_added):
        try:
            chat_added = chat_added.__dict__
        except:
            pass
        self.chat = Chat(chat_added.get('chat'))
        self.added = User(chat_added.get('new_chat_member'))
        self.added_by = User(chat_added.get('from_user'))
        self.date = Date(chat_added.get('date'))
        self.old_status = chat_added.get('old_chat_member')

    def get_dict(self):
        return self.__dict__

    def __repr__(self):
        msg = self.__dict__
        return str(msg)

class Button:
    def inline(text, callback_data, web_app=None, login_url=None, switch_inline_query=None, switch_inline_query_current_chat=None, callback_game=None, pay=None):
        if web_app:
            if isinstance(web_app, WebAppInfo):
                web_app = web_app.get_dict()
        if login_url:
            if isinstance(login_url, LoginUrl):
                login_url = login_url.get_dict()
        if callback_game:
            callback_game = callback_game.get_dict()
        data = {
            '_': 'inline_keyboard',
            'text': text,
            'callback_data': callback_data,
            'web_app': web_app,
            'login_url': login_url,
            'switch_inline_query': switch_inline_query,
            'switch_inline_query_current_chat': switch_inline_query_current_chat,
            'callback_game': callback_game,
            'pay': pay
        }
        return data

    def url(text, url):
        data = {
            '_': 'inline_keyboard',
            'text': text,
            'url': url
        }
        return data

    def ForceReply(force_reply=True, placeholder=None, selective=False):
        data = {
            'force_reply': force_reply,
            'input_field_placeholder': placeholder,
            'selective': selective
        }
        return data

    def keyboard(text, callback_data, resize_keyboard=None, one_time_keyboard=None, placeholder=None, selective=None):
        data = {
            '_': 'keyboard',
            'text': text,
            'callback_data': callback_data,
            'resize_keyboard': resize_keyboard,
            'one_time_keyboard': one_time_keyboard,
            'input_field_placeholder': placeholder,
            'selective': selective
        }
        return data

    def remove(remove_keyboard=True, selective=None):
        data = {
            'remove_keyboard': remove_keyboard,
            'selective': selective
        }
        return data

class Stickers:
    def __init__(self, stickers):
        try:
            stickers = stickers.__dict__
        except:
            pass
        self.stickers = stickers

    def do(self):
        if isinstance(self.stickers, Sticker):
            return Sticker(self.input_media)
        elif isinstance(self.stickers, StickerSet):
            return StickerSet(self.stickers)

    def get_dict(self):
        return self.__dict__

    def __repr__(self):
        msg = self.__dict__
        return str(msg)

class Sticker:
    def __init__(self, sticker):
        try:
            sticker = sticker.__dict__
        except:
            pass
        self.file_id = sticker.get('file_id')
        self.file_unique_id = sticker.get('file_unique_id')
        self.type = sticker.get('type')
        self.width = sticker.get('width')
        self.height = sticker.get('height')
        self.is_animated = sticker.get('is_animated')
        self.is_video = sticker.get('is_video')
        if sticker.get('thumb'):
            self.thumb = PhotoSize(sticker.get('thumb'))
        if sticker.get('emoji'):
            self.emoji = sticker.get('emoji')
        if sticker.get('set_name'):
            self.set_name = sticker.get('set_name')
        if sticker.get('premium_animation'):
            self.premium_animation = File(sticker.get('premium_animation'))
        if sticker.get('mask_position'):
            self.mask_position = MaskPosition(sticker.get('mask_position'))
        if sticker.get('custom_emoji_id'):
            self.custom_emoji_id = sticker.get('custom_emoji_id')
        self.file_size = sticker.get('file_size')

    def get_dict(self):
        return self.__dict__

    def __repr__(self):
        msg = self.__dict__
        return str(msg)

class StickerSet:
    def __init__(self, sticker_set):
        try:
            sticker_set = sticker_set.__dict__
        except:
            pass
        self.name = sticker_set.get('name')
        self.title = sticker_set.get('title')
        self.sticker_type = sticker_set.get('sticker_type')
        self.is_animated = sticker_set.get('is_animated')
        self.is_video = sticker_set.get('is_video')
        self.stickers = [Sticker(x) for x in sticker_set.get('stickers')]
        if sticker_set.get('thumb'):
            self.thumb = PhotoSize(sticker_set.get('thumb'))

    def get_dict(self):
        return self.__dict__

    def __repr__(self):
        msg = self.__dict__
        return str(msg)

class MaskPosition:
    def __init__(self, mask_position):
        try:
            mask_position = mask_position.__dict__
        except:
            pass
        self.point = mask_position.get('point')
        self.x_shift = mask_position.get('x_shift')
        self.y_shift = mask_position.get('y_shift')
        self.scale = mask_position.get('scale')

    def get_dict(self):
        return self.__dict__

    def __repr__(self):
        msg = self.__dict__
        return str(msg)

# Template.
'''
class :
    def __init__(self, ):
        try:
            . = .__dict__
        except:
            pass
        self. = .get('')

    def get_dict(self):
        return self.__dict__

    def __repr__(self):
        msg = self.__dict__
        return str(msg)
'''
'''
class :
    def __init__(self, ):
        try:
            . = .__dict__
        except:
            pass
        self. = .

    def do(self):
        if isinstance(self., ):
            return (self.)

    def get_dict(self):
        return self.__dict__

    def __repr__(self):
        msg = self.__dict__
        return str(msg)
'''