import aiohttp
from bot_settings import config


async def authorisation(username: str, password: str):
    async with aiohttp.ClientSession() as session:
        async with session.post(config.bot_auth_api_url, json={'username': username, 'password': password}) as response:
            return await response.json()
