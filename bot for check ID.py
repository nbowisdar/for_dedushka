from aiogram import Bot,  types
from aiogram.dispatcher import Dispatcher
from aiogram.utils import executor


TOKEN = '5108400714:AAHp6JO9AWKpGnAQeAMMrwuExweKtnm0K9Y'
USER = None


bot = Bot(TOKEN)
dp = Dispatcher(bot)

@dp.message_handler(commands=['check_id'])
async def check_id (message: types.Message, ):
    await message.reply(f'Your id is - {message.from_user.id}')
    global USER
    USER = message.from_user.id

@dp.message_handler(commands=['test'])
async def test (message: types.Message,):
    print(USER)

executor.start_polling(dp, skip_updates=True)