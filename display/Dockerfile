FROM balenalib/raspberrypi3-debian

RUN apt update && apt install -y build-essential gcc
RUN apt install -y python3 python3-pip python3-dev

RUN python3 -m pip install --upgrade pip
RUN python3 -m pip install aiohttp 
RUN python3 -m pip install Adafruit-SSD1306

RUN sudo apt install \
    libjpeg-turbo-progs libopenjp2-7-dev \
    libtiff5-dev libjpeg62-turbo-dev zlib1g-dev \
    libfreetype6-dev liblcms2-dev libwebp-dev \
    tcl8.6-dev tk8.6-dev 

RUN python3 -m pip install Pillow RPi.GPIO

WORKDIR /app

COPY display sysread.py ./

CMD ["python3", "./sysread.py"]