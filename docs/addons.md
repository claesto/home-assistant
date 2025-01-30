# Add-ons
## Introduction
Add-ons enhance Home Assistant’s functionality by enabling the installation of additional applications. These applications may integrate with Home Assistant, or facilitate tasks like sharing configurations via Samba for seamless editing from other devices.

Add-ons are in fact [Docker containers](https://www.docker.com/resources/what-container/) managed from within Home Assistant. If you've installed "Home Assistant" as the OS,the add-on store allows you to install these. If you've installed Home Assistant within Docker, you're supposed to setup & manage these containers yourself.

## Integrations versus add-ons
In Home Assistant, **integrations** and **add-ons** serve distinct purposes and operate in different parts of the system. See [my integrations](integrations.md).

### Key differences
| **Feature**      | **Integration**              | **Add-ons**                      |
| ---------------- | ---------------------------- | -------------------------------- |
| **Purpose**      | connect to external services | extend Home Assistant services   |
| **Location**     | within Home Assistant        | side-by-side with Home Assistant |
| **Installation** | from UI (devices & services) | from Add-ons menu                |
| **Examples**     | Philips Hue, Spotify, ...    | Node-RED, MariaDB, ...           |

## Add-ons list
!!! info
    
    This list does not change frequently; however, it may still be outdated compared to my current installation.

| Add-on                 | Description                                                          |
| ---------------------- | -------------------------------------------------------------------- | 
| Adguard Home           | Network-wide ads & trackers blocking DNS server                      |
| Duck DNS               | Free dynamic DNS (DynDNS or DDNS) service with Let's Encrypt support |
| ESPHome device builder | building your own smart home devices using ESPHome                   |
| File editor            | browser based file editor for Home Assistant                         |
| Grafana                | open platform for analytics and monitoring                           |
| InfluxDB               | scalable datastore for metrics, events and real-time analytics       |
| Samba share            | explore Home Assistant folders with SMB/CIFS                         |
| Terminal & SSH         | allow remote logins                                                  |