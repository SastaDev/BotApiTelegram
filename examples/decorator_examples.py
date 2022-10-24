# hello.py (using decorator)
# Decorators are followed by on_update.

from BotApiTelegram import TelegramBot

bot_token = '' # Your Bot Token from @BotFather.

bot = TelegramBot('bot_db', bot_token=bot_token)

@bot.on_update(command='start')
def on_start(message):
    message.reply('Hello.')

bot.start_polling()
