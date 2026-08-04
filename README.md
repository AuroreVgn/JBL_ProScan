# JBL ProScan

[![GitHub Release][releases-shield]][releases]
[![License][license-shield]](LICENSE)
[![Home Assistant](https://img.shields.io/badge/Home%20Assistant-2026.3%2B-41BDF5.svg?style=flat-square&logo=homeassistant)](https://www.home-assistant.io/)
[![HACS Custom](https://img.shields.io/badge/HACS-Custom-41BDF5.svg?style=flat-square)](https://hacs.xyz/)
[![Maintainers](https://img.shields.io/badge/maintainers-@AuroreVgn%20-blue.svg?style=flat-square)](https://github.com/AuroreVgn)

A Home Assistant custom integration for **JBL ProScan** allowing you to retrieve your **pond** or **aquarium** water analyses directly from your myJBL account.

## Features

- Secure login to **myJBL**
- Automatic pond selection
- Retrieve the latest analysis
- Retrieve the complete analysis history
- Sensors for:
  - pH
  - KH
  - GH
  - NO₂
  - NO₃
  - CO₂
  - Chlorine

- Number of recorded analyses
- Last analysis date
- Days since the last analysis
- Multi-language support : 🇫🇷 🇬🇧 🇩🇪 🇪🇸 🇮🇹 🇳🇱 🇵🇹

## Screenshots

### Integration
<img width="285" height="211,5" alt="image" src="https://github.com/user-attachments/assets/09e357ca-72af-489c-bd66-f16c78006d31" />

### Entities
<img width="151" height="264" alt="image" src="https://github.com/user-attachments/assets/216a5961-32bb-49de-a12e-7988123f3f2e" />

### Dashboard
<img width="242" height="291" alt="image" src="https://github.com/user-attachments/assets/6cddf462-4f09-4289-af0e-04f7684302eb" />

Lovelace card available **[here](https://github.com/AuroreVgn/JBL_ProScan_card/)**.

## Installation

### HACS (recommended)

1. Add to HACS
   - automatically [![Ouvrir ce dépôt dans HACS](https://my.home-assistant.io/badges/hacs_repository.svg)](https://my.home-assistant.io/redirect/hacs_repository/?owner=AuroreVgn&repository=JBL_ProScan&category=integration) <br />
   - manually
      - HACS :arrow_right: Intégrations :arrow_right: Menu '...' :arrow_right: Dépôts personnalisés
      - Repo: `https://github.com/AuroreVgn/JBL_ProScan`
      - Category: `Integration`
3. Download
   - HACS :arrow_right: Integration :arrow_right: JBL_ProScan :arrow_right: Download
4. Restart Home Assistant

### Configuration

Go to

```
Settings
→ Devices & Services
→ Add Integration
→ JBL ProScan
```

Enter:

- myJBL email
- myJBL password

Then choose the pond (or aquarium) to import.


## Entities

The integration creates the following sensors.

| Sensor | Unit |
|---------|------|
| pH | - |
| KH | °dKH |
| GH | °dGH |
| NO₂ | mg/L |
| NO₃ | mg/L |
| CO₂ | mg/L |
| Chlorine | mg/L |
| Last analysis | Date |
| Days since last analysis | day |
| Number of analyses | - |

## Credits

Developed by **AuroreVgn**
Special thanks to the Home Assistant community.
This project is **not affiliated with JBL GmbH & Co. KG**.


## License
This project is distributed under the MIT License.

[releases-shield]: https://img.shields.io/github/v/release/AuroreVgn/JBL_ProScan?style=flat-square
[releases]: https://github.com/AuroreVgn/JBL_ProScan/releases
[license-shield]: https://img.shields.io/github/license/AuroreVgn/JBL_ProScan?style=flat-square
