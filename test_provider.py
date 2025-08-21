import pytest
from providers.telegramProvider import TelegramProvider


@pytest.mark.asyncio
async def test_tg_provider():
    provider = TelegramProvider()
    async with provider.application:
        await provider.application.start()
        await provider.application.stop()
