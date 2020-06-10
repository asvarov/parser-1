import account
import logging

from aiogram import Bot, Dispatcher, executor, types


logging.basicConfig(level=logging.INFO)

bot = Bot(token=account.API_TOKEN)
dp = Dispatcher(bot)


@dp.message_handler()
async def echo(message: types.Message):
    if message.text == 'Hi':
        await message.answer('Hello man!')


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)