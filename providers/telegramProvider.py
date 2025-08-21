import os
from telegram.ext import Application
from abstractions.baseProvider import BaseProvider


BOT_TOKEN = os.getenv("BOT_TOKEN")
TG_USER_ID = os.getenv("TG_USER_ID")


class TelegramProvider(BaseProvider):
    application = Application.builder().token(BOT_TOKEN).build()

    async def send_report(self, msg: str):
        await self.application.bot.send_message(TG_USER_ID, msg)
