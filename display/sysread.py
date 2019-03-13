import asyncio
import logging 
import json

import aiohttp

from display import DisplayService


async def simple_run(cmd):
    proc = await asyncio.create_subprocess_shell(
        cmd,
        stdout=asyncio.subprocess.PIPE,
        stderr=asyncio.subprocess.PIPE)

    stdout, stderr = await proc.communicate()
    if proc.returncode != 0:
        raise Exception("proc returned with non-zero")

    if stdout:
        stdout = stdout.decode('utf-8')
    if stderr:
        stderr = stderr.decode('utf-8')
    return stdout, stderr


async def system_read():  
    cmds = [
        "hostname -I | cut -d\' \' -f1",
        "top -bn1 | grep load | awk '{printf \"CPU Load: %.2f\", $(NF-2)}'",
        "free -m | awk 'NR==2{printf \"Mem: %s/%sMB %.2f%%\", $3,$2,$3*100/$2 }'",
        "df -h | awk '$NF==\"/\"{printf \"Disk: %d/%dGB %s\", $3,$2,$5}'"
    ]

    out = await asyncio.gather(*map(lambda c: simple_run(c), cmds))
    return list(map(lambda x: x[0], out))


async def get_res(session, url):
  
    async with session.get(url) as response:
        assert response.status == 200
        return await response.json()


async def full_readout(queue):
    while True:
        async with aiohttp.ClientSession() as session:
            res = []

            [sys_out, json_res] = await asyncio.gather(
                system_read(),
                get_res(session, 'http://sensors:8888/dht11')
            )
            
            res.append("pihost")
            res.append("======")
            
            for i in sys_out:
                res.append(i)
            for k, v in json_res.items():
                res.append("{0}: {1: .3g}".format(k, v))

            await queue.put(res)
           
        asyncio.sleep(.3)


# producer consumer example
async def system_read_producer(queue: asyncio.Queue):
    while True:
        await asyncio.sleep(.1)
        res = await system_read()
        await queue.put(res)


async def draw_consumer(queue: asyncio.Queue, ds: DisplayService):
    while True:
        content = await queue.get()
        ds.draw_txt_content(content=content)


# basic system out
async def show_system_read(ds: DisplayService):
    while True:
        ip, cpu, mem, disk = await system_read()
        ds.draw_txt_content(content=[ip, cpu, mem, disk])
        await asyncio.sleep(.1)


def main():
    logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
    logging.getLogger('asyncio').setLevel(logging.INFO)
    logging.getLogger('Adafruit_I2C').setLevel(logging.INFO)
    log = logging.getLogger('test')
    log.setLevel(logging.DEBUG)

    log.debug("Init event loop")
    loop = asyncio.get_event_loop()
    q = asyncio.Queue()

    log.debug("Init display service")
    ds = DisplayService(loop=loop, debug=logging.DEBUG)
    
    asyncio.ensure_future(ds.start())
    asyncio.ensure_future(full_readout(q))
    asyncio.ensure_future(draw_consumer(q, ds))

    log.debug("Starting loop")
    loop.run_forever()


if __name__ == '__main__':
    main()