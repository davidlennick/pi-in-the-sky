import asyncio
import aiohttp
import subprocess
import logging

import Adafruit_GPIO.SPI as SPI
import Adafruit_SSD1306

from PIL import Image
from PIL import ImageDraw
from PIL import ImageFont


class DisplayService:

    def __init__(self, font: ImageFont=None, loop={}, debug=logging.INFO):
        self._log = logging.getLogger('DisplayService')
        self._log.setLevel(debug)
        self._log.info("Init DisplayService")
        
        if loop is {}:
            self.loop = asyncio.get_event_loop()
        else:
            self.loop = loop


        if font == None:
            self.font = ImageFont.load_default()
        else:
            self.font = font

        self.disp = Adafruit_SSD1306.SSD1306_128_64(None)
        self._init_disp()
        self.img, self.draw = self._init_canvas_draw(self.disp.width, self.disp.height)


    async def _draw_img(self):
        self._log.debug("Init draw loop")
        while True:
            self.disp.image(self.img)
            self.disp.display()
            await asyncio.sleep(.1)

    def _init_disp(self):
        self._log.debug("Init display")
    
        # Initialize library.
        self.disp.begin()

        # Clear display.
        self.disp.clear()
        self.disp.display()


    def _init_canvas_draw(self, w, h):
        self._log.debug("Init canvas and draw obj")
        image = Image.new('1', (w, h))
        draw = ImageDraw.Draw(image)
        draw.rectangle((0, 0, w, h), outline=0, fill=0)
        return image, draw


    
    # public stuff 

    async def start(self):
        self._log.debug("Starting DisplayService events")
        asyncio.ensure_future(self._draw_img())  
        #asyncio.ensure_future(self.block_check())       


    def draw_txt_content(self, content=[]):
        self._log.debug("Drawing content {}".format(content))
        # Draw a black filled box to clear the image.
        self.draw.rectangle((0, 0, self.disp.width, self.disp.height), outline=0, fill=0)
        
        offset = 8
        base = -2
        current = 0
        for c in content:
            self.draw.text((0, current + base), str(c), font=self.font, fill=255)
            current += offset


    async def block_check(self):
        while True:
            self._log.debug("not blocked")
            await asyncio.sleep(1)




