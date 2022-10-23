class Conversation:
    def __init__(self, bot, chat):
        self.bot = bot
        self.chat = chat
        self.updates = {}

    def append_update(update):
        update_number = list(self.updates.keys())[-1] + 1
        data = {
            str(update_number): update
        }
        self.updates.update(data)

    def wait(self):
        self.do_wait = True
        while self.do_wait is True:
            pass

    def response(self):
        index = list(self.updates.keys())[-1]
        return self.updates[index]