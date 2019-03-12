import asyncio
import aiohttp
import aiohttp.web
import os
import json
import logging
import functools

#import RPi.GPIO as GPIO
import Adafruit_DHT


class DHT11SensorServer:

    def __init__(self, port=8888, loop={}, debug=logging.INFO):
        self._log = logging.getLogger('DHT11SensorServer')
        self._log.setLevel(debug)
        self._log.info("Init DHT11SensorServer")
        self.port = port 

        if loop is {}:
            self.loop = asyncio.get_event_loop()
        else:
            self.loop = loop

        # this is a view that will be updated by the async method
        self.dht11_reading = {
            "humidity": 0,
            "temperature": 0
        }

        self.app = aiohttp.web.Application()  
        self.app.add_routes([aiohttp.web.get('/dht11', self.handle)])

  
    async def handle(self, request):
        self._log.debug("Returning {}".format(self.dht11_reading))         
        return aiohttp.web.json_response(self.dht11_reading)


    async def read_sensor(self):
        while True:
            self._log.debug("Reading DHT11")  
            await asyncio.sleep(2)
            humidity = 0
            temperature = 0
            try:
                humidity, temperature = Adafruit_DHT.read_retry(Adafruit_DHT.DHT11, 17)
            except Exception as e:
                 self._log.debug(e)
                 pass                 

            if humidity is not None and temperature is not None:
                self.dht11_reading = {
                    "humidity": humidity,
                    "temperature": temperature
                }               
            else:
                print('Failed to get reading. Try again!')


    async def start(self):        
        runner = aiohttp.web.AppRunner(self.app)
        await runner.setup()

        site = aiohttp.web.TCPSite(runner, port=self.port)
        await site.start()

        asyncio.ensure_future(self.read_sensor()) 


if __name__ == '__main__':

    logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
    logging.getLogger('asyncio').setLevel(logging.INFO)

    if os.environ.get("PORT") != None:        
        port = os.environ["PORT"]
    else:
        logging.debug("port not set, using default 8888")
        port = 8888

    
    server = DHT11SensorServer(port=port, debug=logging.DEBUG)
    
    loop = asyncio.get_event_loop()
    asyncio.ensure_future(server.start())
    loop.run_forever()
