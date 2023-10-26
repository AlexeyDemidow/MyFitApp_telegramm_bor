import aiohttp
from bot_settings import config


async def bot_exit(auth_token: str):
    headers = {'Authorization': f'Token {auth_token}'}
    async with aiohttp.ClientSession() as session:
        async with session.post(config.unauth_api_url, headers=headers):
            return 'Вы вышли из профиля.'
