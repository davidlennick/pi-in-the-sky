import asyncio
import random
import logging


# really wuick overview of asyncio

async def block_check():
    while True:
        _log.debug("not blocked")
        await asyncio.sleep(.5)


async def a_long_function():
    length = random.randint(0, 3)
    await asyncio.sleep(length)
    _log.debug("Done after {}".format(length))
    return length



logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
logging.getLogger('asyncio').setLevel(logging.INFO)
_log = logging.getLogger("another")

loop = asyncio.get_event_loop()


asyncio.ensure_future(block_check())

asyncio.ensure_future(a_long_function(), loop=loop)
asyncio.ensure_future(a_long_function(), loop=loop)
asyncio.ensure_future(a_long_function(), loop=loop)
asyncio.ensure_future(a_long_function(), loop=loop)
asyncio.ensure_future(a_long_function(), loop=loop)
asyncio.ensure_future(a_long_function(), loop=loop)


loop.run_forever()



