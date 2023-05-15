import asyncio
from src.barbot_go import BarbotGo

bar_bot = BarbotGo(mode="CONSOLE")

while(True):
    asyncio.run(bar_bot.main_menu())
