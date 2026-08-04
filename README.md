# JBL ProScan

[![GitHub Release][releases-shield]][releases]
[![License][license-shield]](LICENSE)
[![Home Assistant](https://img.shields.io/badge/Home%20Assistant-2026.3%2B-41BDF5.svg?style=flat-square&logo=homeassistant)](https://www.home-assistant.io/)
[![HACS Custom](https://img.shields.io/badge/HACS-Custom-41BDF5.svg?style=flat-square)](https://hacs.xyz/)
[![Maintainer](https://img.shields.io/badge/Maintainer-AuroreVgn-blue.svg?style=flat-square)](https://github.com/AuroreVgn)

A Home Assistant custom integration for **JBL ProScan** allowing you to retrieve your **pond** or **aquarium** water analyses directly from your **myJBL** account.

## ✨ Features

- 🔐 Secure authentication to **myJBL**
- 🌊 Automatic pond / aquarium selection
- 📊 Complete analysis history
- 🔄 Manual refresh service
- 📈 Long-Term Statistics compatible
- 🤖 Binary sensors for automations
- 🌍 Multi-language support
- ⚡ Native Home Assistant Config Flow

## Sensors
### Water parameters
- pH
- KH
- GH
- NO₂
- NO₃
- CO₂
- Chlorine

### Additional sensors
- History
- Last analysis
- Days since last analysis

### Binary sensors
- pH OK
- KH OK
- GH OK
- Nitrite High
- Nitrate High
- Chlorine High
- Analysis overdue

## Screenshots

### Setup
<img width="285" src="https://github.com/user-attachments/assets/09e357ca-72af-489c-bd66-f16c78006d31"/>

### Entities
<img width="150" height="407" alt="image" src="https://github.com/user-attachments/assets/04da4e02-f774-4e2f-98c3-c452e3ff5f17" />


### Dashboard
➡️ https://github.com/AuroreVgn/JBL_ProScan_card


## Installation
### HACS (recommended)
#### Add the repository

Automatically
[![Open your Home Assistant instance and open this repository inside HACS.](https://my.home-assistant.io/badges/hacs_repository.svg)](https://my.home-assistant.io/redirect/hacs_repository/?owner=AuroreVgn&repository=JBL_ProScan&category=integration)

Or manually

```
HACS
 └── Integrations
      └── ⋮
           └── Custom repositories

Repository:
https://github.com/AuroreVgn/JBL_ProScan

Category:
Integration
```

#### Install
```
HACS
 └── JBL ProScan
      └── Download
```

Restart Home Assistant.

## Configuration
Go to

```
Settings
→ Devices & Services
→ Add Integration
→ JBL ProScan
```

Enter
- myJBL email
- myJBL password

Then simply choose the pond (or aquarium) to import.

## Created entities
### Sensors

| Entity | Unit |
|---------|------|
| pH | — |
| KH | °dKH |
| GH | °dGH |
| NO₂ | mg/L |
| NO₃ | mg/L |
| CO₂ | mg/L |
| Chlorine | mg/L |
| History | analyses |
| Last analysis | Date |
| Days since last analysis | day |

All measurement sensors are compatible with **Home Assistant Long-Term Statistics**.

### Binary sensors
The integration also creates binary sensors designed for automations.
- pH OK
- KH OK
- GH OK
- Nitrite High
- Nitrate High
- Chlorine High
- Analysis overdue

### Services

The integration provides the following service:

#### Refresh data

```
jbl_proscan.refresh
```

Refreshes the selected pond immediately without waiting for the next scheduled update.

Perfect for dashboards and automations.

### Automations
Thanks to the binary sensors you can easily create automations such as:
- Remind you when no analysis has been performed for X days.

## Companion Lovelace Card
A dedicated Lovelace card is available ➡️ https://github.com/AuroreVgn/JBL_ProScan_card

Features include:
- 📈 Interactive graphs
- 🎨 Custom colors
- 🎭 Custom icons
- 🌍 Multi-language
- 🔄 Manual refresh
- 📅 Period selector
- 📊 Previous analysis comparison
- 📉 Recommended JBL ranges
- 🖱 Interactive tooltips
- 🧩 Visual editor


## Credits
Developed by **AuroreVgn**
Special thanks to the Home Assistant community.
This project is **not affiliated with JBL GmbH & Co. KG**.


## License
Distributed under the MIT License.


[releases-shield]: https://img.shields.io/github/v/release/AuroreVgn/JBL_ProScan?style=flat-square
[releases]: https://github.com/AuroreVgn/JBL_ProScan/releases
[license-shield]: https://img.shields.io/github/license/AuroreVgn/JBL_ProScan?style=flat-square
