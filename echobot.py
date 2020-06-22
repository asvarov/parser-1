import logging
import hvac
from aiogram import Bot, Dispatcher, executor, types

with open('root_token_vault.json', mode='r') as f:
    root_token = f.read()

client = hvac.Client(url='http://192.168.10.10:8200', token=root_token)

logging.basicConfig(level=logging.INFO)

read_response = client.secrets.kv.read_secret_version(path='telegram_bot')
API_TOKEN = read_response['data']['data']['API_TOKEN']
bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)


@dp.message_handler()
async def echo(message: types.Message):
    await message.answer(message.text)


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)