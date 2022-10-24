from BotApiTelegram import TelegramBot
from BotApiTelegram.types import Button

bot_token = '' # Your Bot Token from @BotFather.

bot = TelegramBot('bot_db', bot_token=bot_token)

@bot.on_update(command='start')
def on_start(message):
    buttons = [
        [Button.inline('Orange', 'orange'),
        Button.inline('Apple', 'apple')],
        [Button.url('Google.com', 'https://google.com')]
        ]
    message.reply('Orange or Apple?', buttons=buttons)

print('Bot has been started!')
bot.start_polling()
