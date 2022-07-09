from os import makedirs, remove
from os.path import exists, join
from uuid import uuid4

from aiogram.types import Message

from settings import DELETE_TEMP


class TempTelegramImage:
    temp_dir: str = "temp"

    def __init__(self, message: Message):
        self.message: Message = message
        self.path: str = join(self.temp_dir, f"{str(uuid4())}.jpg")

    def read(self):
        with open(self.path, "rb") as file:
            return file.read()

    async def __aenter__(self):
        if not exists(self.temp_dir):
            makedirs(self.temp_dir)
        await self.message.photo[-1].download(self.path)
        return self

    async def __aexit__(self, exc_type, exc_value, exc_traceback):
        if DELETE_TEMP:
            remove(self.path)
