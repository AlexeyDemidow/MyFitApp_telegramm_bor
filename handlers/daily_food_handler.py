import aiohttp
from datetime import date

from bot_settings import config


async def daily_food(auth_token: str):
    headers = {'Authorization': f'Token {auth_token}'}
    today_date = str(date.today())
    async with aiohttp.ClientSession() as session:
        async with session.get(
            f'{config.user_foodlist_api_url}{today_date}/',
            headers=headers,
        ) as response:
            return await response.json()