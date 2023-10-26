import aiohttp
from bot_settings import config


async def profile(auth_token: str):
    headers = {'Authorization': f'Token {auth_token}'}
    async with aiohttp.ClientSession() as session:
        async with session.get(config.profile_api_url, headers=headers) as response:
            return await response.json()
