from aiogram import Bot, Dispatcher
from aiogram.filters import Command
from aiogram.types import Message

BOT_TOKEN = '6407812037:AAHIjdQDfRW4JwyldWtwTN9ApORUEKG4XHk'

bot = Bot(token=BOT_TOKEN)
dp = Dispatcher()

@dp.message(Command(commands=["start"]))
async def process_start_command(message: Message):
    await message.answer('Привет!\nМеня зовут Эхо-бот!')

@dp.message(Command(commands=["help"]))
async def process_help_command(message: Message):
    await message.answer(
        'тееесть'
        'тут тоже что то должно быть'
        "текст 3"
    )

@dp.message()
async def send_echo(message: Message):
    await message.reply(text=message.text)
    print(message.text)

if __name__ == '__main__':
    dp.run_polling(bot)