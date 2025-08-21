import os
from abc import ABC, abstractmethod
from dotenv import load_dotenv
from telegram.ext import Application


if os.path.exists(".env"):
    load_dotenv(".env")


class BaseProvider(ABC):
    @property
    @abstractmethod
    def application(self) -> Application:
        pass

    @abstractmethod
    async def send_report(self, msg: str):
        pass
