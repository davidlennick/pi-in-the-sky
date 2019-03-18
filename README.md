# pi-in-the-sky

- a demo project originally used for a presentation
- target platfrom is a raspberry pi 3 b+, running [balenaOS](https://www.balena.io/os/)
    - you could probably use docker + docker-compose if I2C, etc., are enabled in the base OS
- creates a few services
    - `sensors`, which collects temperature and humidity readings from a DHT11 (GPIO pin 17) and serves them at `http://sensors:8888/dht11` as json
    - `display`, which draws to a SSD1306 128x64 (I2C)



## prereqs


`node` and `npm`


## set up

```
# setup a local network (ie., use a phone wifi hotspot)

# install balena-cli on local machine
sudo npm i -g balena-cli

# insert a microSD card, download the balenaOS image, configure to use wifi
sudo balena local configure ./balena.img
sudo balena local flash ./balena.img

# build and push :)
cd pi-in-the-sky
balena push <PI_IP> -s .
```


## wiring diagram links

http://www.circuitbasics.com/how-to-set-up-the-dht11-humidity-sensor-on-the-raspberry-pi/

https://www.raspberrypi-spy.co.uk/2018/04/i2c-oled-display-module-with-raspberry-pi/



## other links

https://www.balena.io/os/docs/raspberrypi3/getting-started/

https://www.balena.io/docs/learn/develop/hardware/gpio/


## helpful commands
```
sudo balena local flash ./balena.img

sudo balena local scan
ssh root@pihost.local -p22222

balena push 192.168.43.126 -s .

balena run -it --privileged -p 8888:8888 52a35e9b48f3 "/bin/bash"

http://192.168.43.126:8888/dht11

while true; do curl http://192.168.43.126:8888/dht11; sleep .5; printf "\n"; done

balena inspect --format='{{.HostConfig.Privileged}}' c4709f5f1b6e
```
