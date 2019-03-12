# pi-in-the-sky

a quick demo project for a presentation


## get started

```
- set up a local network (ie., use a phone wifi hotspot)
- install balenaOS on pi
- install balena-cli on local machine
- build and push :)
```


install balenaOS on pi: https://www.balena.io/os/


https://www.balena.io/os/docs/raspberrypi3/getting-started/

https://www.balena.io/docs/learn/develop/hardware/gpio/


http://www.circuitbasics.com/how-to-set-up-the-dht11-humidity-sensor-on-the-raspberry-pi/




## stuff
```

sudo balena local flash ./balena.img

sudo balena local scan
ssh root@pihost.local -p22222

balena push 192.168.43.126 -s .


balena run -it --privileged -p 8888:8888 52a35e9b48f3 "/bin/bash"

http://192.168.43.126:8888/dht11

while true; do curl http://192.168.43.126:8888/dht11; sleep .5; printf "\n"; done

```


- for some reason, compose file isn't working as expected... can't access GPIO pins? works when running the container directly