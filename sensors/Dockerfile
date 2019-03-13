FROM balenalib/raspberrypi3-debian

RUN apt update && apt install -y build-essential gcc
RUN apt install -y python3 python3-pip python3-dev

RUN python3 -m pip install aiohttp 
RUN python3 -m pip install Adafruit_DHT

ENV PORT=8888
#ENV INITSYSTEM on
#ENV UDEV=1

WORKDIR /app

COPY sensors.py ./

CMD ["python3", "./sensors.py"]

