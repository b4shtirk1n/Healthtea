import os
from telegram.ext import Application
from abstractions.baseProvider import BaseProvider

BOT_TOKEN = os.getenv("BOT_TOKEN")
TG_USER_ID = os.getenv("TG_USER_ID")


class TelegramProvider(BaseProvider):
    def __init__(self):
        super().__init__()
        self.application = Application.builder().token(BOT_TOKEN).build().run_polling()

    async def send_report(self, msg: str):
        await self.application.bot.send_message(TG_USER_ID, msg)
