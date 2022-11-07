class NewMessage:
    def __init__(self, user, chat):
        self.user = [user] if not isinstance(user, list) else user
        self.chat = [chat] if not isinstance(chat, list) else chat

class text:
    def __init__(self, text):
        self.text = [text] if not isinstance(text, list) else text

class command:
    def __init__(self, command, starts_with=None):
        self.command = [command] if not isinstance(command, list) else command
        self.starts_with = [starts_with] if not isinstance(starts_with, list) else starts_with

class regex:
    def __init__(self, regex):
        self.regex = [regex] if not isinstance(regex, list) else regex

class CallbackQuery:
    def __init__(self, data):
        self.data = [data] if not isinstance(data, list) else data

class chat:
    def __init__(self, chat=None, users=None, joined=None, left=None, added=None):
        self.chat = [chat] if not isinstance(chat, list) else chat
        self.users = [users] if not isinstance(users, list) else users
        self.joined = [joined] if not isinstance(joined, list) else joined
        self.left = [left] if not isinstance(left, list) else left
        self.added = [added] if not isinstance(added, list) else added

class user:
    def __init__(self, users=None, from_private=None, from_groups=None, from_channels=None):
        pass # Implimentation Soon!

class animation:
    def __init__(self, only_mime_type=None):
        self.only_mime_type = ([only_mime_type] if isinstance(only_mime_type, list) else only_mime_type) if only_mime_type is not None else []

class audio:
    def __init__(self, only_mime_type=None):
        self.only_mime_type = ([only_mime_type] if isinstance(only_mime_type, list) else only_mime_type) if only_mime_type is not None else []

class document:
    def __init__(self, only_mime_type=None):
        self.only_mime_type = ([only_mime_type] if isinstance(only_mime_type, list) else only_mime_type) if only_mime_type is not None else []

class photo:
    def __init__(self):
        pass

class sticker:
    def __init__(self, only_type=None, only_animated=None, only_video=None, only_premium_animation=None, only_custom_emoji=None):
        self.only_type = ([only_type] if not isinstance(only_type, list) else only_type) if only_type is not None else []
        self.only_animated = only_animated
        self.only_video = only_video
        self.only_premium_animation = only_premium_animation
        self.only_custom_emoji = only_custom_emoji

class video:
    def __init__(self, only_mime_type=None):
        self.only_mime_type = ([only_mime_type] if isinstance(only_mime_type, list) else only_mime_type) if only_mime_type is not None else []

class video_note:
    def __init__(self):
        pass

class voice:
    def __init__(self, only_mime_type=None):
        self.only_mime_type = ([only_mime_type] if isinstance(only_mime_type, list) else only_mime_type) if only_mime_type is not None else []

class contact:
    def __init__(self, only_phone_number=None, users=None, only_vcard=None):
        self.only_phone_number = only_phone_number
        self.users = [users] if not isinstance(users, list) else users
        self.only_vcard = only_vcard

class dice:
    def __init__(self):
        pass

class game:
    def __init__(self):
        pass

class poll:
    def __init__(self, only_closed=None, only_anonymous=None, poll_type=None):
        self.only_closed = only_closed
        self.only_anonymous = only_anonymous
        self.poll_type = [poll_type] if not isinstance(poll_type, list) else poll_type

class venue:
    def __init__(self):
        pass

class location:
    def __init__(self):
        pass

class pinned_message:
    def __init__(self):
        pass

class invoice:
    def __init__(self):
        pass

# Template.
'''
class :
    def __init__(self):
        self. = [.] if not isinstance(., list) else .
'''