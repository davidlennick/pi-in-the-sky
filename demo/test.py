import asyncio
import aiohttp
import random

from aiohttp import web

async def handle(request):

    time_to_wait = random.randint(0, 5)
    await asyncio.sleep(time_to_wait)

    name = request.match_info.get('name', "Anonymous")
    text = "Hello, " + name + "\nYou waited " + str(time_to_wait) + " s"
    return web.Response(text=text)

app = web.Application()
app.add_routes([web.get('/', handle),
                web.get('/{name}', handle)])

web.run_app(app)