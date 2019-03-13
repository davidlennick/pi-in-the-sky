# pi-in-the-sky

a quick demo project for a presentation


## get started

```
- set up a local network (ie., use a phone wifi hotspot)
- install balenaOS on pi
- install balena-cli on local machine
- build and push :)
```

Uses a DHT11 (GPIO pin 17) and SSD1306 128x64 (I2C)
http://www.circuitbasics.com/how-to-set-up-the-dht11-humidity-sensor-on-the-raspberry-pi/
https://www.raspberrypi-spy.co.uk/2018/04/i2c-oled-display-module-with-raspberry-pi/


install balenaOS on pi: https://www.balena.io/os/

https://www.balena.io/os/docs/raspberrypi3/getting-started/

https://www.balena.io/docs/learn/develop/hardware/gpio/


## stuff
```

sudo balena local flash ./balena.img

sudo balena local scan
ssh root@pihost.local -p22222

balena push 192.168.43.126 -s .


balena run -it --privileged -p 8888:8888 52a35e9b48f3 "/bin/bash"

http://192.168.43.126:8888/dht11

while true; do curl http://192.168.43.126:8888/dht11; sleep .5; printf "\n"; done

balena ps
balena inspect --format='{{.HostConfig.Privileged}}' c4709f5f1b6e

```
