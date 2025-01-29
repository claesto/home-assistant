[![Unlicense License][license-shield]][license-url]
[![Commits][commits-shield]][commits-url]

# Home Assistant configuration

## About The Project
This project is my personal Home Assistant configuration, designed to automate and simplify everyday tasks while enhancing the functionality of my smart home. It integrates a wide range of devices and platforms, providing centralized control over lighting, climate, security, and other connected systems.

With custom automations, scripts, and dashboards, this configuration is tailored to meet the specific needs of my household.

This repository serves as a hub for sharing, improving, and evolving my smart home setup while inspiring others to create their own personalized automation systems.

Don't forget to :star: if this configuration helped you or [buy me a coffee](https://paypal.me/tomclaessens).

## Structure
To maintain an organized and manageable configuration, I have chosen to use [Home Assistant's Packages](https://www.home-assistant.io/docs/configuration/packages/) functionality. This approach enables me to keep all related code consolidated in one place.

_Some information is stored in `secrets.yml`, which is not uploaded for obvious reasons._

## Architecture

### Core system
- Raspberry Pi 4 (4GB)
- Backups to Synology NAS
- MariaDB as database (on Synology NAS)

### Smart home integration
- HUE bridge for several lights & Zigbee power plugs
- Niko home control for non-HUE lights
- Shelly for power monitoring
- Sonos / Marantz integrations to control audio
- HomeKit bridge for use within the iOS ecosystem

## License

Distributed under the Unlicense License. See `LICENSE.txt` for more information.

## Contact

Tom Claessens - [@claesto](https://twitter.com/claesto) - [Buy me a coffee](https://paypal.me/tomclaessens)

Project Link: [https://github.com/claesto/home-assistant](https://github.com/claesto/home-assistant)

[license-shield]: https://img.shields.io/github/license/claesto/home-assistant.svg?style=for-the-badge
[license-url]: https://github.com/claesto/home-assistant/blob/master/LICENSE.txt

[commits-shield]: https://img.shields.io/github/commit-activity/y/claesto/home-assistant.svg?style=for-the-badge
[commits-url]: https://github.com/claesto/home-assistant/commits/master/