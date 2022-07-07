from aiogram import Bot, Dispatcher, executor, md, types
from babel.core import Locale

from settings import API_TOKEN
from static.lang import transalate


class DemBot:
    bot = Bot(token=API_TOKEN)
    dp = Dispatcher(bot)

    @dp.message_handler(commands=["start", "help"])
    async def send_welcome(message: types.Message):
        """
        This handler will be called when user sends `/start` or `/help` command
        """
        text = transalate(message.from_user.locale, "greeting")
        await message.reply(text)

    def start(self):
        executor.start_polling(self.dp, skip_updates=True)
