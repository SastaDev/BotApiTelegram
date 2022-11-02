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

class CallbackQuery:
    def __init__(self, data):
        self.data = [data] if not isinstance(data, list) else data

class chat:
    def __init__(self, chat=None, joined=None, left=None, added=None):
        self.chat = [chat] if not isinstance(chat, list) else chat
        self.joined = [joined] if not isinstance(joined, list) else joined
        self.left = [left] if not isinstance(left, list) else left
        self.added = [added] if not isinstance(added, list) else added

class user:
    def __init__(self):
        pass # Implimentation Soon!