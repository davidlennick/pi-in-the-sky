FROM balenalib/raspberrypi3-python:3.7-latest
ENV PORT=8888
ENV INITSYSTEM on
ENV UDEV=1

WORKDIR /app

RUN apt update && apt install -y build-essential gcc
RUN python3 -m pip install aiohttp Adafruit_DHT
COPY sensors.py ./

RUN ["python3", "./sensors.py"]

