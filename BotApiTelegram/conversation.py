from . import exceptions
import threading

class Conversation:
    def __init__(self, bot, chat_id, global_timeout=60):
        self.bot = bot
        self.chat_id = chat_id
        self.updates = {}
        self.last_update_number = 0
        self.global_timeout = global_timeout

    def append_update(self, update):
        update_number = list(self.updates.keys())[-1] + 1
        data = {
            str(update_number): update
        }
        self.updates.update(data)
        self.last_update_number += 1

    def wait(self, timeout=None):
        if timeout is None:
            timeout = self.global_timeout
        t = threading.Thread(target=self._wait, args=(timeout,))
        t.start()
        t.join(timeout=timeout)
        raise exceptions.ConversationTimeOut(timeout=timeout)

    def _wait(self):
        while self.last_update_number != self.last_update_number + 1:
            pass
        else:
            return 'hehelmao'

    def get_response(self):
        index = list(self.updates.keys())[-1]
        return self.updates[index]