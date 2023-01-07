import logging
import config as cf
import aiogram as aio
token = cf.token
tgbot = aio.Bot(token)
dp = aio.Dispatcher(tgbot)


@dp.message_handler(commands = ['start'])
async def send_welcome(message: aio.types.Message):
    await message.reply("Привет!")

@dp.message_handler(commands=['BB'])
async def send_welcome(message: aio.types.Message):
     await message.reply("Пока((")

@dp.message_handler(commands=['lox'])
async def send_welcome(message: aio.types.Message):
    await message.reply("Ты лох))")

@dp.message_handler(commands=['NG'])
async def send_welcome(message: aio.types.Message):
    await message.reply("__/|\__   \n"
                        "/ | \  \n")

if __name__ == '__main__':
    aio.executor.start_polling(dp, skip_updates = True)

