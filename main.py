import os
import logging
import asyncio
import requests
from datetime import timedelta
from providers.telegramProvider import TelegramProvider


logger = logging.getLogger(__name__)
logging.basicConfig(
    handlers=[logging.StreamHandler()],
    level=logging.INFO,
    format="%(asctime)s %(levelname)s %(message)s",
)

UPDATE_CHECK_SECONDS = os.getenv("UPDATE_CHECK_SECONDS")
CHECK_URL = os.getenv("CHECK_URL")
TG_PROVIDER = os.getenv("TG_PROVIDER")

services = {CHECK_URL}


async def health_check():
    if 200 < requests.get(CHECK_URL).status_code >= 400:
        msg = f"{CHECK_URL} is down!"
        if CHECK_URL not in services:
            services.add(CHECK_URL)
    elif CHECK_URL in services:
        msg = f"{CHECK_URL} is alive!"
        services.remove(CHECK_URL)
    else:
        return
    await provider.send_report(msg)


async def scheduler():
    while True:
        await asyncio.sleep(
            timedelta(seconds=float(UPDATE_CHECK_SECONDS)).total_seconds()
        )
        asyncio.create_task(health_check())


if __name__ == "__main__":
    if TG_PROVIDER:
        provider = TelegramProvider()

    asyncio.run(scheduler())

    if TG_PROVIDER:
        provider.application.run_polling()
