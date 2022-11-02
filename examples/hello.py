from BotApiTelegram import TelegramBot, filters

bot_token = '' # Your Bot Token from @BotFather.

bot = TelegramBot('bot_db', bot_token=bot_token)

@bot.on_update(filters.command('start'))
def on_start(message):
    message.reply('Hello.')

bot.start_polling()
