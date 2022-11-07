class UnAuthorizedBotToken(Exception):
    def __init__(self, bot_token):
        msg = 'Un-Authorized Bot Token.'
        super().__init__(msg)

class UnKnownError(Exception):
    def __init__(self, error):
        msg = 'UnKnow Error Occured: {}.'.format(error)
        super().__init__(msg)

class ChatNotFound(Exception):
    def __init__(self):
        msg = 'Chat was not found.'
        super().__init__(msg)

class NoAdministratorsInPrivateChat(Exception):
    def __init__(self):
        msg = 'Administrators are not available in private chat.'
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

class UserBlockedBot(Exception):
    def __init__(self):
        msg = 'Bot was blocked by the user.'
        super().__init__(msg)

class ConversationTimeOut(Exception):
    def __init__(self, timeout):
        msg = 'The conversation response timeout of {} seconds was timed out.'.format(timeout)
        super().__init__(msg)

class UnSupportedParseMode(Exception):
    def __init__(self):
        msg = 'An UnSupported parse_mode.'
        super().__init__(msg)

class QueryError(Exception):
    def __init__(self):
        msg = 'Query is too old and response timeouted or Query ID is invalid.'
        super().__init__(msg)

# Template.
'''
class (Exception):
    def __init__(self):
        msg = ''
        super().__init__(msg)
'''