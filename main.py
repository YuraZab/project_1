from aiogram import Bot, Dispatcher
from aiogram.filters import Command
from aiogram.types import Message
from aiogram.types import ContentType
from aiogram import F

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

async def send_photo_echo(message: Message):
    print(message)
    await message.reply_photo(message.photo[0].file_id)

async  def send_sticker_echo(message: Message):
    print(message)
    await message.reply_sticker(message.sticker.file_id)

async def send_voice_echo(messagge: Message):
    await messagge.answer_voice(messagge.voice.file_id)

async def send_echo(message: Message):
    await message.reply(text=message.text)

dp.message.register(send_photo_echo, F.content_type == ContentType.PHOTO)
dp.message.register(send_sticker_echo, F.sticker)
dp.message.register(send_voice_echo, F.voice)
dp.message.register(send_echo)

if __name__ == '__main__':
    dp.run_polling(bot)