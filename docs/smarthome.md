# My Smart Home

## Introduction

My smart home journey began with an experiment using **OpenHAB** on a **Raspberry Pi 3B+**, paired with a Philips Hue starter kit that included the Hue bridge and two lights. While OpenHAB gave me a good start, I quickly realized it didn’t meet all my needs in terms of ease of use and flexibility. That’s when I made the switch to **Home Assistant**, and I haven’t looked back since.

Over time, I reworked my Home Assistant configuration a few times, eventually settling on the **packages approach** to organize everything in a scalable and maintainable way. This allowed me to simplify the management of my growing smart home system.

My main focus initially was on **automating lighting** with motion sensors. I used **presence detection** to turn my motion sensors into a **security system**, giving my home an added layer of protection. The system evolved, and I added **Shelly** devices to **monitor power consumption** and track the performance of my **solar panels**, which has been both enlightening and rewarding.

Looking ahead, my smart home continues to expand. I plan to **monitor water consumption**, integrate more **security devices** like door and window sensors, and dive deeper into **automation** to make the entire system smarter and more intuitive.

It’s been an exciting journey, and there’s still so much more to explore.

## Hardware
I'm running now running Home Assistant OS on a [Raspberry Pi 4 (4GB)](https://www.raspberrypi.com/products/raspberry-pi-4-model-b/){:target="_blank"} with a MariaDB database powering the system, hosted on my [Synology NAS](http://synology.com/){:target="_blank"} ([DS224+](https://www.synology.com/nl-nl/products/DS224+){:target="_blank"}). I use an **external SSD** for faster performance and increased realiability.

### Protocols & hubs
* Zigbee: [Philips HUE bridge](https://www.philips-hue.com/en-us/p/hue-bridge/046677458478){:target="_blank"}, [Niko Home Control hub](https://www.niko.eu/en/products/niko-home-control/products-for-traditional-wiring/wireless-smart-hub-for-niko-home-control-productmodel-niko-b442b6fb-5274-5114-bc4f-79477a804541){:target="_blank"}, [Conbee II](https://phoscon.de/en/conbee2){:target="_blank"} (deprecated)
* Z-wave: [Aeon Labs Z Wave Stick (GEN 5)](https://aeotec.com/products/aeotec-z-stick-gen5/){:target="_blank"} (deprecated)

##### Future
* [RFXtrx433E](http://www.rfxcom.com/RFXtrx433E-USB-43392MHz-Transceiver/en){:target="_blank"} (433 mhz): to control our Somfy window covers

### Lights
* [Niko connected dimmer](https://www.niko.eu/en/products/niko-home-control/products-for-traditional-wiring/connected-dimmer-3-200-w-2-wire-zigbee-productmodel-niko-e61c5693-2d0c-5be5-8544-461983048049){:target="_blank"}
* [HUE ambiance light bulbs](https://www.philips-hue.com/en-us/p/hue-white-ambiance-a19-e26-smart-bulb-60-w-2-pack/046677548568){:target="_blank"}
* [HUE Centris ceiling](https://www.philips-hue.com/en-us/p/hue-white-and-color-ambiance-centris-2-spot-ceiling-light/046677589493){:target="_blank"}

### Plugs
* [Niko connected switching socket](https://www.niko.eu/en/products/niko-home-control/products-for-traditional-wiring/connected-switching-socket-outlet-with-pin-earthing-and-shutters-zigbee-productmodel-niko-aa84a653-36c4-55de-b6d1-d2ddfc6326dc){:target="_blank"}
* [IKEA Tretakt smart plugs](https://www.ikea.com/us/en/p/tretakt-plug-smart-40556511/){:target="_blank"}

### Media
* [Marantz AV7701](https://www.marantz.com/en-us/product/archive-av-separates/av7701/810003.html){:target="_blank"}
* [IKEA Symfonisk](https://www.sonos.com/en-us/symfonisk-by-sonos-and-ikea){:target="_blank"}
* [Samsung The Frame TVs](https://www.samsung.com/us/tvs/the-frame/highlights/){:target="_blank"}

### Security
* [HUE motion sensors](https://www.philips-hue.com/en-us/p/hue-motion-sensor/046677570972#overview){:target="_blank"}
* [Ubiquiti G4 doorbell](https://techspecs.ui.com/unifi/cameras-nvrs/uvc-g4-doorbell){:target="_blank"}

##### Future
* Ubiquiti cameras
* Door & window sensors

### Remotes
* [Niko dimmer switch for HUE](https://www.niko.eu/en/article/122-91004){:target="_blank"}
* [HUE dimmer switches](https://www.philips-hue.com/en-us/p/hue-dimmer-switch-latest-model/046677562779){:target="_blank"}

### Climate
* [Aqara Temperature and Humidity Sensor](https://www.aqara.com/en/product/temperature-humidity-sensor/){:target="_blank"}

##### Future
* Smart thermostat

### Voice assistants
* Siri