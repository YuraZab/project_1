from aiogram import Bot, Dispatcher
from aiogram.filters import Command
from aiogram.types import Message
from aiogram.types import ContentType
from aiogram import F

BOT_TOKEN = '6407812037:AAHIjdQDfRW4JwyldWtwTN9ApORUEKG4XHk'

bot = Bot(token=BOT_TOKEN)
dp = Dispatcher()

@dp.message(Command(commands='start'))
async def process_start_command(message: Message):
    print(message.model_dump_json(indent=4, exclude_none=True))
    await message.answer('Привет! Я бот напиши мне что-нибудь.')

@dp.message(Command(commands='help'))
async def process_help_command(message: Message):
    await message.answer('на данный момент в боте прописаны функции:')


async def send_echo(message: Message):
    print(message.model_dump_json(indent=7, exclude_none=True))
    try:
        await message.send_copy(chat_id=message.chat.id)
    except TypeError:
        await message.reply(
            text='функция не поддерживается'
        )


dp.message.register(send_echo)

if __name__ == '__main__':
    dp.run_polling(bot)