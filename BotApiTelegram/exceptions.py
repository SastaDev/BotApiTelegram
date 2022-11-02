class UnAuthorizedBotToken(Exception):
    def __init__(self, bot_token):
        msg = 'Un-Authorized Bot Token: {}'.format(bot_token)
        super().__init__(msg)

class UnKnownError(Exception):
    def __init__(self, error):
        msg = 'UnKnow Error Occured: {}'.format(error)
        super().__init__(msg)

class ChatNotFound(Exception):
    def __init__(self, chat_id):
        msg = 'Chat was not found: {}'.format(chat_id)
        super().__init__(msg)

class NoAdministratorsInPrivateChat(Exception):
    def __init__(self, chat_id):
        msg = 'Administrators are not available in private chat: {}'.format(chat_id)
        super().__init__(msg)

class MessageTextIsEmpty(Exception):
    def __init__(self):
        msg = 'The Message was not having any text. A message must have a text.'
        super().__init__(msg)

class InvalidKeyboardMarkup(Exception):
    def __init__(self, array_of_array=False):
        msg = None
        if array_of_array:
            msg = 'The KeyboardMarkup should be Array of Array!'
        super().__init__(msg)

# Template.
'''
class (Exception):
    def __init__(self):
        msg = ''
        super().__init__(msg)
'''