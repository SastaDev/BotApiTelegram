import pickle
import os

class BotDB:
    def __init__(self, bot, db_path):
        self.bot = bot
        self.db_path = '{}.dat'.format(db_path)

    def dat_file(self):
        if os.path.exists(self.db_path) is False:
            file = open(self.db_path, 'wb')
            db_data = {
                'bot_token': self.bot.bot_token,
                'stats': {
                    'total_users': 0,
                    'total_groups': 0
                }
            }
            pickle.dump(db_data, file)
            file.close()
            return db_data
        else:
            file = open(self.db_path, 'rb')
            db_data = pickle.load(file)
            file.close()
            try:
                db_data.get('bot_token')
            except KeyError:
                raise ValueError('Invalid/Corrupted "{}" file.'.format(self.db_path))
            return db_data

    def save(self, **kwargs):
        file = open(self.db_path, 'rb')
        db_data = pickle.load(file)
        file.close()
        db_data.update(kwargs)
        file = open(self.db_path, 'wb')
        pickle.dump(db_data, file)
        file.close()