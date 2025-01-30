# Integrations
## Introduction
Integrations within Home Assistant are _software components_ that enable Home Assistant to communicate with and control external services, devices, or platforms. They act as the bridge between Home Assistant and your smart home ecosystem, allowing you to seamlessly integrate various technologies under one centralized platform.

## Integrations versus add-ons
In Home Assistant, **integrations** and **add-ons** serve distinct purposes and operate in different parts of the system. See my [add-ons](addons.md).

### Key differences
| **Feature**      | **Integration**              | **Add-ons**                      |
| ---------------- | ---------------------------- | -------------------------------- |
| **Purpose**      | connect to external services | extend Home Assistant services   |
| **Location**     | within Home Assistant        | side-by-side with Home Assistant |
| **Installation** | from UI (devices & services) | from Add-ons menu                |
| **Examples**     | Philips Hue, Spotify, ...    | Node-RED, MariaDB, ...           |

!!! note

    If you're using Home Assistant Core without the Supervisor, only **integrations** are available; **add-ons** require the Supervisor for management or you'd have to manage them yourself within Docker containers for instance. See my [add-ons information](addons.md).

## Integrations list

I use the [`default_config:`](https://www.home-assistant.io/integrations/default_config){:target="_blank"} integration, which is a meta component that loads & configures a default set of integrations.

!!! info
    
    This list does not change frequently; however, it may still be outdated compared to my current installation.

* [Brother Printer][brotherprinter-url]{:target="_blank"}  
Read data from a local Brother printer.
* [Buienradar][buienradar-url]{:target="_blank"}  
Use [Buienradar.nl](https://www.buienradar.nl) as a source for meteorological data.
* [Denon AVR][denonavr-url]{:target="_blank"}  
Allows control of [Denon network receivers](https://www.denon.com/){:target="_blank"}. Also works with some [Marantz](https://www.marantz.com/){:target="_blank"} receivers as well!
* [Electricity Maps][electricitymaps-url]{:target="_blank"}  
A sensor that queries the [Electricity Maps](https://www.electricitymaps.com/){:target="_blank"} API for the CO2 intensity of a specific region.
* [ESPHome][esphome-url]{:target="_blank"}  
Integrate [ESPHome](https://esphome.io/){:target="_blank"} devices directly to Home Assistant.
* [Forecast.Solar][forecastsolar-url]{:target="_blank"}  
Solar production forecasting for a solar panel system. Uses historic averages combined with weather forecasts.
* [Home Assistant Supervisor][hassio-url]{:target="_blank"}  
Monitor & control [add-ons](addons.md) and the operating system from Home Assistant.
* [Home Connect][homeconnect-url]{:target="_blank"}  
Integrates Home Connect appliances within Home Assistant (Bosch & Siemens)
* [HomeKit Bridge][homekit-url]{:target="_blank"}  
Makes Home Assistant entities available in Apple HomeKit for control with Apple's Home app or Siri.
* [InfluxDB][influxdb-url]{:target="_blank"}  
Transfer state changes to an external [InfluxDB](https://influxdb.com/){:target="_blank"} database. Also see [add-ons](addons.md)
* [Internet Printing Protocol [IPP]][ipp-url]{:target="_blank"}  
Allows you to read data from a networked printer that supports the [IPP](https://www.pwg.org/ipp/everywhere.html){:target="_blank"}
* [Local Calendar][localcalendar-url]{:target="_blank"}  
Create a calender of events for powering automations.
* [MeteoAlarm][meteoalarm-url]{:target="_blank"}  
Watch weather alerts in Europe (EUMETNET) - [MeteoAlarm](https://www.meteoalarm.org/){:target="_blank"}
* [Meteorologisk institutt [met.no]][metno-url]{:target="_blank"}  
Uses the [Met.no](https://met.no/){:target="_blank"} web service as a source for meteorological data.
* [Mobile App][mobileapp-url]{:target="_blank"}  
Allows the Home Assistant mobile app to easily integrate with your Home Assistant installation.
* [Moon][moon-url]{:target="_blank"}  
Tracks the phases of the moon.
* [Philips Hue][philipshue-url]{:target="_blank"}  
Control & monitor lights, power plugs and sensors as part of Philips HUE.
* [Raspberry Pi Power Supply Checker][rpipsc-url]{:target="_blank"}  
Allows the detection of a bad power supply on the Raspberry Pi.
* [RESTful][restful-url]{:target="_blank"}  
The `rest` sensor consumes a given endpoint. I use it to scrape [Vlinder weather station](https://vlinder.ugent.be/en/index.html){:target="_blank"} data.
* [Samsung Smart TV][samsungsmarttv-url]{:target="_blank"}  
Allows you to control a Samsung Smart TV.
* [Season][season-url]{:target="_blank"}  
Provides current astronomical or meteorological season as a sensor.
* [Shelly][shelly-url]{:target="_blank"}  
Integrates [Shelly](https://shelly.com){:target="_blank"} devices within Home Assistant.
* [Shopping List][shoppinglist-url]{:target="_blank"}  
Keep track of shopping list items.
* [Sonos][sonos-url]{:target="_blank"}  
Control [Sonos](https://www.sonos.com){:target="_blank"} speakers from Home Assistant.
* [Sun][sun-url]{:target="_blank"}  
Track whether the sun is above or below the horizon for your location.
* [System Monitor][systemmonitor-url]{:target="_blank"}  
Monitor disk usage, memory usage, network usage, CPU usage & running processes.
* [Waze Travel Time][waze-url]{:target="_blank"}  
Travel time from [Waze](https://www.waze.com){:target="_blank"}, used to display my commute travel time.
* [Workday][workday-url]{:target="_blank"}  
Indicates wheher the current day is a workday or not.

### HACS

!!! warning "HACS"

    **HACS (Home Assistant Community Store)** is a third-party extension for Home Assistant that provides access to custom integrations, themes, and frontend elements developed by the Home Assistant community. It's **not officially supported** by Home Assistant, use with caution.

* [Afvalbeheer][afvalbeheer-url]{:target="_blank"}  
Provides sensors for various waste collectors in Belgium and the Netherlands via a REST API.
* [FontAwesome][fontawesome-url]{:target="_blank"}  
Allows the use of FontAwesome icons within Home Assistant.
* [HACS][hacs-url]{:target="_blank"}  
The HACS component itself which allows you to install community store integrations.
* [Niko Home Control II][nikohc-url]{:target="_blank"}  
Integration with the [Niko Connected Controller (version II)](https://www.niko.eu/en/products/niko-home-control/products-on-bus-wiring/connected-controller-for-niko-home-control-ii-productmodel-niko-beec7a08-371c-5472-9dfd-d79a8d63dc3a){:target="_blank"} and its connected devices. Also works with the [Niko Smart Hub](https://www.niko.eu/en/products/niko-home-control/products-for-traditional-wiring/wireless-smart-hub-for-niko-home-control-productmodel-niko-b442b6fb-5274-5114-bc4f-79477a804541){:target="_blank"} for Niko Home Control for traditionally wired houses.
* [Presence Simulation][presencesimulation-url]{:target="_blank"}  
Component that provides presence simulation by turning on/off lights, switches, covers, etc. based on your history.

[afvalbeheer-url]: https://github.com/pippyn/Home-Assistant-Sensor-Afvalbeheer
[brotherprinter-url]: https://www.home-assistant.io/integrations/brother
[buienradar-url]: https://www.home-assistant.io/integrations/buienradar
[denonavr-url]: https://www.home-assistant.io/integrations/denonavr
[electricitymaps-url]: https://www.home-assistant.io/integrations/co2signal
[esphome-url]: https://www.home-assistant.io/integrations/esphome
[fontawesome-url]: https://github.com/thomasloven/hass-fontawesome
[forecastsolar-url]: https://www.home-assistant.io/integrations/forecast_solar
[hacs-url]: https://hacs.xyz/docs/use/
[hassio-url]: https://www.home-assistant.io/integrations/hassio
[homeconnect-url]: https://www.home-assistant.io/integrations/home_connect
[homekit-url]: https://www.home-assistant.io/integrations/homekit
[influxdb-url]: https://www.home-assistant.io/integrations/influxdb
[ipp-url]: https://www.home-assistant.io/integrations/ipp
[localcalendar-url]: https://www.home-assistant.io/integrations/local_calendar
[meteoalarm-url]: https://www.home-assistant.io/integrations/meteoalarm
[metno-url]: https://www.home-assistant.io/integrations/met
[mobileapp-url]: https://www.home-assistant.io/integrations/mobile_app
[moon-url]: https://www.home-assistant.io/integrations/moon
[nikohc-url]: https://github.com/joleys/niko-home-control-II/blob/master/README.md
[philipshue-url]: https://www.home-assistant.io/integrations/hue
[presencesimulation-url]: https://github.com/slashback100/presence_simulation
[restful-url]: https://www.home-assistant.io/integrations/rest
[rpipsc-url]: https://www.home-assistant.io/integrations/rpi_power
[samsungsmarttv-url]: https://www.home-assistant.io/integrations/samsungtv
[season-url]: https://www.home-assistant.io/integrations/season
[shelly-url]: https://www.home-assistant.io/integrations/shelly
[shoppinglist-url]: https://www.home-assistant.io/integrations/shopping_list
[sonos-url]: https://www.home-assistant.io/integrations/sonos
[sun-url]: https://www.home-assistant.io/integrations/sun
[systemmonitor-url]: https://www.home-assistant.io/integrations/systemmonitor
[waze-url]: https://www.home-assistant.io/integrations/waze_travel_time
[workday-url]: https://www.home-assistant.io/integrations/workday