from BotApiTelegram import TelegramBot

bot_token = '' # Your Bot Token from @BotFather.

bot = TelegramBot('bot_db', bot_token=bot_token)

def on_start(message):
    message.reply('Hello.')

bot.add_command('start', on_start)
bot.start_polling()
