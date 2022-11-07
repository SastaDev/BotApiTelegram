from . import types

def parse_entities(message):
    if isinstance(message, types.Message):
        entities = message.entities
    else:
        entities = message
    commands = []
    for command in entities:
        if command.type == 'bot_command':
            commands.append(message.text[command.offset - 1 + command.length:])
    users = []
    for user in entities:
        if user.type == 'text_mention':
            users.append(user.user)
    return [commands, users]