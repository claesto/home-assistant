# [Home Assistant](https://home-assistant.io) configuration

![Home Assistant version](https://img.shields.io/badge/Home%20Assistant-2020.12.5-blue.svg) 
![Commits this year](https://img.shields.io/github/commit-activity/y/tomclaessens/home-assistant.svg)

[@tomclaessens](https://www.github.com/tomclaessens) - also visit my [website](https://tomclaessens.be) for more information. Don't forget to :star: if this configuration helped you.

## Table of contents
- [Equipment](#equipment)
- [Devices](#devices)
- [Integrations](#integrations)
- [Add-ons](#add-ons)
- [Automations](#automations)
- [Dashboards](#dashboards)
- [TODO list](#todo)
- [Future](#future)
- [License](#license)

## Equipment

Home Assistant is running on a [Raspberry Pi 4](https://www.raspberrypi.com/products/raspberry-pi-4-model-b/) with an [60GB Kingston SSD](https://www.amazon.com/Kingston-Digital-SSDNow-SV300S37A-60G/dp/B00A35X6GM). I used [this guide](https://community.home-assistant.io/t/installing-home-assistant-on-a-rpi-4b-with-ssd-boot/230948) by *Jörg Wagner* to migrate my setup from an SD card to the SSD.

I used the Hassio installation method. Plans exist to migrate to a more powerful setup, because as of right now I have the Pi 4 running Home Assistant and a separate Pi 3b+ running docker containers. Migrating both Pi's to a single machine with docker might make things *easier*.

## Devices

### Hubs

| Device | Connection | Integration | Notes |
| ------ | ---------- | ----------- | ----- |
| Phillips HUE Hub v2 | Ethernet | [Phillips Hue](https://www.home-assistant.io/integrations/hue/) | Control Phillips Hue lights and devices. |
| Aeotec Z-stick Gen5 | USB | [Z-Wave](https://www.home-assistant.io/integrations/zwave_js/) | Control z-wave devices. |
| Conbee II | USB | [ZigBee](https://www.home-assistant.io/integrations/zha/) |Control Zigbee devices, non Phillips Hue |
| Niko Home Control Hub | Ethernet | [Niko Home Control II](https://github.com/filipvh/hass-nhc2) | Control connected light switches and power sockets. |

### Lighting

| Device | Quantity | Connection | Component | Notes |
| ------ | :------: | ---------- | --------- | ----- |
| HUE White & Color Centris - two | 2 | Hue Bridge | [Phillips Hue](https://www.home-assistant.io/integrations/hue/) | Ceiling light with a single rectangular downlight and two adjustable spotlights. |
| Niko connected dimmer | 4 | Niko Home Control Hub | [Niko Home Control II](https://github.com/filipvh/hass-nhc2) | Dimmer switches that make any light source "smart". Used in the bedroom, office, dining area and living room. |
| Niko connected switch | 2 | Niko Home Control Hub | [Niko Home Control II](https://github.com/filipvh/hass-nhc2) | Connected light switches without dimmer functionality. Used to control lights in the garden and at the entrance of the house. |

### HUE specific devices

| Device | Quantity | Connection | Component | Notes |
| ------ | :------: | ---------- | --------- | ----- |
| Niko - friends of Hue wall switch | 2 | Hue Bridge | [Phillips Hue](https://www.home-assistant.io/integrations/hue/) | Niko switch, to match the other switches, specifically designed for use with Phillips Hue. |
| Motion sensor | 6 | Hue Bridge | [Phillips Hue](https://www.home-assistant.io/integrations/hue/) | Motion sensor used to control lights, and as *security* system. Also includes temperature and lux sensors. |

### Sensors

| Device | Quantity | Connection | Component | Notes |
| ------ | :------: | ---------- | --------- | ----- |
| Aqara temperature & humidity sensor | 6 | Conbee II | [ZigBee](https://www.home-assistant.io/integrations/zha/) | Reporting indoor climate (temperature & humidity) for most rooms (living room, bedroom, offices, bathroom and attic. |
| Aqara door/window sensor | 15 | Conbee II | [ZigBee](https://www.home-assistant.io/integrations/zha/) | Door & window sensor on every door/window of the house, including garage door |

### Media

| Device | Quantity | Connection | Component | Notes |
| ------ | :------: | ---------- | --------- | ----- |
| Marantz AVR7701 | 1 | Ethernet | [DenonAVR](https://www.home-assistant.io/integrations/denonavr/) | AVR receiver, paired with the Marantz MM7055 amplifier |
| Samsung The Frame 65" | 1 | Ethernet | [DenonAVR](https://www.home-assistant.io/integrations/denonavr/) | Thin profile 65" TV from Samsung with a wooden frame and a permanent image on display when not in use. Doesn't look like a TV when it's off. |

### Energy monitoring
| Device | Quantity | Connection | Component | Notes |
| ------ | :------: | ---------- | --------- | ----- |
| Shelly EM | 1 | WiFi | [Shelly](https://www.home-assistant.io/integrations/shelly/) | Shelly energy meter, reporting electric consumption and solar panel generation. |

### Switches
| Device | Quantity | Connection | Component | Notes |
| ------ | :------: | ---------- | --------- | ----- |
| Shelly | 1 | WiFi | [Shelly](https://www.home-assistant.io/integrations/shelly/) | Shelly switch to control the garage door. |

## Integrations

- [Spotify](https://www.home-assistant.io/integrations/spotify/)
- [Brother](https://www.home-assistant.io/integrations/brother/)
- [Denon AVR Network receivers](https://www.home-assistant.io/integrations/denonavr/)
- [Forecast.Solar](https://www.home-assistant.io/integrations/forecast_solar/)
- [Homekit](https://www.home-assistant.io/integrations/homekit/)
- [Meteorologisk institutt (Met.no)](https://www.home-assistant.io/integrations/met/)
- [Mobile App](https://www.home-assistant.io/integrations/mobile_app/)
- [Philips Hue](https://www.home-assistant.io/integrations/hue/)
- [Raspberry Pi Power Supply Checker](https://www.home-assistant.io/integrations/rpi_power/)
- [Shelly](https://www.home-assistant.io/integrations/shelly/)
- [Synology DSM](https://www.home-assistant.io/integrations/synology_dsm/)
- [UniFi Network](https://www.home-assistant.io/integrations/unifi/)
- [Waze](https://www.home-assistant.io/integrations/waze_travel_time/)
- [Zigbee Home Automation](https://www.home-assistant.io/integrations/zha/)
- [Meteo Alarm](https://www.home-assistant.io/integrations/meteoalarm/)
- [HACS](https://hacs.xyz/)
  - [Niko Home Control II](https://github.com/filipvh/hass-nhc2)
  - [Afvalbeheer](https://github.com/pippyn/Home-Assistant-Sensor-Afvalbeheer) (sensors for waste collectors in Belgium)

## Add-ons

- [Duck DNS](https://github.com/home-assistant/addons/tree/master/duckdns)
- [InfluxDB](https://github.com/hassio-addons/addon-influxdb)
- [Grafana](https://github.com/hassio-addons/addon-grafana)
- [Samba Share](https://github.com/home-assistant/hassio-addons/tree/master/samba)

## Automations

1. Notify me when to take out the trash, before the collection of the day after
2. Notify me whenever [Meteo Alarm](https://www.home-assistant.io/integrations/meteoalarm/) issues a warning for Antwerp (Belgium)
3. Turn on lights in storage room, or toilet, after motion is detected and lux < 60; turn off lights after 20 seconds, toilet after 120 seconds
4. Fade-in bedside lights in the morning as a more *natural* wake up process instead of an alarm
5. Turn on floor lamp in the living room at sunset
6. Turn on outside lights 20 minutes after sunset; turn off at 10PM, and activate them on based on motion

Besides these, there are also *security-based* notifications, related to motion detections when no one is in the house. I can't list all automations, as they frequently change, are removed or new ones are added.

## Dashboards

Work in progress. I currently use the [Kibibit theme](https://github.com/Kibibit/hass-kibibit-theme) with additionally [Hass Hue Icons](https://github.com/arallsopp/hass-hue-icons), [mini-graph-card](https://github.com/kalkih/mini-graph-card), [auto-entities](https://github.com/thomasloven/lovelace-auto-entities) and [animated weather card theme](https://github.com/wowgamr/animated-weather-card).

I have *divided* Home Assistant into two *views*: an overview of devices, sensors, metrics per room. On the second dashboard, everything is grouped by *type*.

#### Overview Dashboard
![Overview Home Assistant dashboard](https://i.imgur.com/oTCxnQ8.jpg)

#### Bedroom dashboard
![Bedroom Home Assistant dashboard](https://i.imgur.com/lK854Uq.jpg)

#### Outside dashboard
![Outside Home Assistant dashboard](https://i.imgur.com/uHLNI1f.jpg)

#### Lighting dashboard
![Lighting Home Assistant dashboard](https://i.imgur.com/giIm0JX.jpg)

#### Sensors dashboard
![Sensors Home Assistant dashboard](https://i.imgur.com/GZUavvX.jpg)

#### Energy dashboard
![Energy Home Assistant dashboard](https://i.imgur.com/dznxWYW.jpg)

## TODO

I use [Github issues](https://github.com/tomclaessens/home-assistant/issues) as a TODO tracker.

## Future

- Smart thermostat
- Node-RED for automations

## License

[MIT](https://choosealicense.com/licenses/mit/)