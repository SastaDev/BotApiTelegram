import time

class Conversation:
    def __init__(self, bot, chat_id):
        self.bot = bot
        self.chat_id = chat_id
        self.updates = {}
        self.last_update_number = 0

    def append_update(self, update):
        update_number = list(self.updates.keys())[-1] + 1
        data = {
            str(update_number): update
        }
        self.updates.update(data)
        self.last_update_number += 1

    def get_response(self):
        index = list(self.updates.keys())[-1]
        return self.updates[index]