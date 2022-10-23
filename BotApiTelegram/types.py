import datetime

def Date(seconds):
    date = datetime.datetime.fromtimestamp(seconds)
    t = '{}:{}:{} {}/{}/{}'.format(date.hour, date.minute, date.second, date.day, date.month, date.year)
    return t

class Message_:
    def __init__(self, bot, msg):
        self.bot = bot
        self.msg = msg

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
        d = self.bot.delete_message(self.chat.chat_id, self.message_id)
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
        d = self.bot.delete_message(self.chat.chat_id, self.message_id)
        return d

    def answer(self, text, show_alert=False, url=None, cache_time=0):
        ans = self.bot.answer_callback_query(
            callback_query_id=self.callback_query.callback_query_id,
            text=text,
            show_alert=show_alert,
            url=url,
            cache_time=cache_time
            )
        return ans

    def __repr__(self):
        msg = self.callback_query.__dict__
        return str(msg)

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

    def __repr__(self):
        msg = self.__dict__
        return str(msg)

class Updates:
    def __init__(self, bot, update):
        self.bot = bot
        self.original_update = update
        self.update_id = update.get('update_id')
        if update.get('message'):
            self.message = Message(bot, update.get('message'))
        '''
        self.edited_message = EditedMessage(update.get('edited_message'))
        self.channel_post = ChannelPost(update.get('channel_post'))
        self.edited_channel_post = EditedChannelPost(update.get('edited_channel_post'))
        self.inline_query = InlineQuery(update.get('inline_query'))
        self.chosen_inline_result = ChosenInlineResult(update.get('chosen_inline_result'))
        '''
        if update.get('callback_query'):
            self.callback_query = CallbackQuery(bot, update.get('callback_query'))
        '''
        self.shipping_query = ShippingQuery(update.get('shipping_query'))
        self.pre_checkout_query = PreCheckoutQuery(update.get('pre_checkout_query'))
        self.poll = Poll(update.get('poll'))
        self.poll_answer = PollAnswer(update.get('poll_answer'))
        '''
        if update.get('my_chat_member'):
            self.my_chat_member = ChatMemberUpdated(update.get('my_chat_member'))
        '''
        self.chat_member = ChatMember(update.get('chat_member'))
        self.chat_join_request = ChatJoinRequest(update.get('chat_join_request'))
        '''

    def __repr__(self):
        msg = self.__dict__
        return str(msg)

    def __getattr__(self, key):
        return self.__dict__.get(key)

# Available Types:
# User, Chat, Message, ChatPhoto.

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
        self.language_code = user.get('language_code')
        self.is_premium = user.get('is_premium')
        self.added_to_attachment_menu = user.get('added_to_attachment_menu')

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

    def __repr__(self):
        msg = self.__dict__
        return str(msg)

class Message:
    def __init__(self, bot, raw_message):
        self.bot = bot
        if raw_message.get('message_id'):
            self.message_id = raw_message.get('message_id')
        if raw_message.get('text'):
            self.text = raw_message.get('text')
        if raw_message.get('from'):
            self.from_user = User(raw_message.get('from'))
        if raw_message.get('sender_chat'):
            self.sender_chat = raw_message.get('sender_chat')
        if raw_message.get('date'):
            self.date = Date(raw_message.get('date'))
        if raw_message.get('chat'):
            self.chat = Chat(raw_message.get('chat'))
        if raw_message.get('forward_from'):
            self.forward_from = User(raw_message.get('forward_from'))
        if raw_message.get('forward_from_chat'):
            self.forward_from_chat = Chat(raw_message.get('forward_from_chat'))
        if raw_message.get('entities'):
            self.entities = raw_message.get('entities')
        if raw_message.get('forward_from_message_id'):
            self.forward_from_message_id = raw_message.get('forward_from_message_id')

    def reply(self, text, reply_to=None, link_preview=True, parse_mode='markdown', **kwargs):
        chat_id = self.chat.chat_id
        r = self.bot.send_message(chat_id=chat_id, text=text, reply_to=self.message_id, link_preview=link_preview, parse_mode=parse_mode, **kwargs)
        return r

    def edit(self, text, link_preview=True, parse_mode='markdown', **kwargs):
        chat_id = self.chat.chat_id
        e = self.bot.edit_message(chat_id=chat_id, message_id=self.message_id, text=text, link_preview=link_preview, parse_mode=parse_mode, **kwargs)
        return e

    def __repr__(self):
        msg = self.__dict__
        return str(msg)

class EditedMessage:
    pass

class ChannelPost:
    pass

class EditedChannelPost:
    pass

class ChannelPost:
    pass

class EditedChannelPost:
    pass

class InlineQuery:
    pass

class ChosenInlineResult:
    pass

class CallbackQuery:
    def __init__(self, bot, callback_query):
        try:
            callback_query = callback_query.__dict__
        except:
            pass
        self.callback_query_id = callback_query.get('id')
        self.from_user = User(callback_query.get('from'))
        if callback_query.get('message'):
            self.message = Message(bot, callback_query.get('message'))
        if callback_query.get('inline_message_id'):
            self.inline_message_id = callback_query.get('inline_message_id')
        self.chat_instance = callback_query.get('chat_instance')
        if callback_query.get('data'):
            self.data = callback_query.get('data')
        if callback_query.get('game_short_name'):
            self.game_short_name = callback_query.get('game_short_name')

    def __repr__(self):
        msg = self.__dict__
        return str(msg)

class ShippingQuery:
    pass

class PreCheckoutQuery:
    pass

class Poll:
    pass

class PollAnswer:
    pass

class ChatMemberUpdated:
    def __init__(self, chat_member_updated):
        try:
            chat_member_updated = chat_member_updated.__dict__
        except:
            pass
        self.chat = Chat(chat_member_updated.get('chat'))
        self.from_user = User(chat_member_updated.get('from'))
        self.date = Date(chat_member_updated.get('date'))
        self.old_chat_member = ChatMember(chat_member_updated.get('old_chat_member'))
        self.new_chat_member = ChatMember(chat_member_updated.get('new_chat_member'))
        if chat_member_updated.get('invite_link'):
            self.invite_link = ChatInviteLink(chat_member_updated.get('invite_link'))

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
        self.do()

    def do(self):
        if isinstance(self.chat_member, list):
            j = []
            for i in self.chat_member:
                j.append(ChatMemberAdministrator(i))
            return j
        status = self.chat_member.get('status')
        print(status)
        if status == 'left':
            return ChatMemberLeft(self.chat_member)

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
        self.can_be_edited = getattr(chat_member_administrator, 'can_be_edited', None)
        self.is_anonymous = getattr(chat_member_administrator, 'is_anonymous', None)
        self.can_manage_chat = getattr(chat_member_administrator, 'can_manage_chat', None)
        self.can_delete_messages = getattr(chat_member_administrator, 'can_delete_messages', None)
        self.can_manage_video_chats = getattr(chat_member_administrator, 'can_manage_video_chats', None)
        self.can_restrict_members = getattr(chat_member_administrator, 'can_restrict_members', None)
        self.can_promote_members = getattr(chat_member_administrator, 'can_promote_members', None)
        self.can_change_info = getattr(chat_member_administrator, 'can_change_info', None)
        self.can_invite_users = getattr(chat_member_administrator, 'can_invite_users', None)
        self.can_post_messages = getattr(chat_member_administrator, 'can_post_messages', None)
        self.can_edit_messages = getattr(chat_member_administrator, 'can_edit_messages', None)
        self.can_pin_messages = getattr(chat_member_administrator, 'can_pin_messages', None)
        self.custom_title = getattr(chat_member_administrator, 'custom_title', None)

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

    def __repr__(self):
        msg = self.__dict__
        return str(msg)

class ChatMemberRestricted:
    def __init__(self, chat_member_restricted):
        try:
            chat_member_restricted = chat_member_restricted.__dict__
        except:
            pass
        self.status = getattr(chat_member_restricted, 'status', None)
        self.user = User(getattr(chat_member_restricted, '', None))
        self.is_member = getattr(chat_member_restricted, 'is_member', None)
        self.can_change_info = getattr(chat_member_restricted, 'can_change_info', None)
        self.can_invite_users = getattr(chat_member_restricted, 'can_invite_users', None)
        self.can_pin_messages = getattr(chat_member_restricted, 'can_pin_messages', None)
        self.can_send_messages = getattr(chat_member_restricted, 'can_send_messages', None)
        self.can_send_media_messages = getattr(chat_member_restricted, 'can_send_media_messages', None)
        self.can_send_polls = getattr(chat_member_restricted, 'can_send_polls', None)
        self.can_send_other_messages = getattr(chat_member_restricted, 'can_send_other_messages', None)
        self.can_add_web_page_previews = getattr(chat_member_restricted, 'can_add_web_page_previews', None)
        self.until_date = getattr(chat_member_restricted, 'until_date', None)

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
        self.creator = User(chat_invite_link.get('user'))
        self.creates_join_request = chat_invite_link.get('creates_join_request')
        self.is_primary = chat_invite_link.get('is_primary')
        self.is_revoked = chat_invite_link.get('is_revoked')
        self.name = chat_invite_link.get('name')
        self.expire_date = chat_invite_link.get('expire_date')
        self.member_limit = chat_invite_link.get('member_limit')
        self.pending_join_request_count = chat_invite_link.get('pending_join_request_count')

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

    def __repr__(self):
        msg = self.__dict__
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

    def __repr__(self):
        msg = self.__dict__
        return str(msg)

class ChatJoined:
    def __init__(self, chat_joined):
        try:
            message = message.__dict__
        except:
            pass
        self.chat = Chat(message.get('chat'))
        self.added = User(message.get('new_chat_member'))
        self.added_by = User(message.get('from_user'))
        self.date = Date(message.get('date'))
        self.old_status = message.get('old_chat_member')

    def __repr__(self):
        msg = self.__dict__
        return str(msg)

class Button:
    def inline(text, callback_query):
        data = {
            'text': text,
            'callback_data': callback_query
        }
        return data

    def url(text, url):
        data = {
            'text': text,
            'url': url
        }
        return data