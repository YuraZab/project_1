from aiogram import Bot, Dispatcher
from aiogram.filters import Command
from aiogram.types import Message
from aiogram.types import ContentType
from aiogram import F

BOT_TOKEN = '6407812037:AAHIjdQDfRW4JwyldWtwTN9ApORUEKG4XHk'

bot = Bot(token=BOT_TOKEN)
dp = Dispatcher()



if __name__ == '__main__':
    dp.run_polling(bot)