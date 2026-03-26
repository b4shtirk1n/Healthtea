import os
from telegram.ext import Application
from abstractions.baseProvider import BaseProvider

BOT_TOKEN = os.getenv("BOT_TOKEN")
TG_USER_ID = os.getenv("TG_USER_ID")

if not BOT_TOKEN or not TG_USER_ID:
    raise


class TelegramProvider(BaseProvider):
    application = Application.builder().token(BOT_TOKEN).build()  # type: ignore

    async def send_report(self, msg: str):
        await self.application.bot.send_message(TG_USER_ID, msg)
