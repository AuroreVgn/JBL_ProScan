# JBL ProScan for Home Assistant

Unofficial Home Assistant integration and Lovelace card for measurements saved by the JBL ProScan application.

> This project is not affiliated with or endorsed by JBL GmbH & Co. KG. JBL and ProScan are trademarks of their respective owner.

## Version

- Integration: **1.0.0**
- Lovelace card: **1.0.0**

## Features

- Login to myJBL with a standard Home Assistant config flow.
- Automatic discovery and selection of a pond or aquarium.
- pH, KH, GH, NO₂, NO₃, CO₂ and chlorine sensors.
- Preservation of comparison signs such as `>7` and `<0.5`.
- Full analysis history exposed by `sensor.<name>_historique`.
- Multilingual integration and card: French, English, German, Spanish, Italian, Dutch and Portuguese.
- Responsive Lovelace card with visual editor, quality indicators and interactive history graph.

## Repository structure

```text
custom_components/jbl_proscan/    Home Assistant integration
dist/jbl-proscan-card.js          Lovelace card release file
www/jbl-proscan-card.js           Copy for manual installation
brands/custom_integrations/       Files prepared for home-assistant/brands
```

## Manual installation

### Integration

Copy:

```text
custom_components/jbl_proscan
```

to:

```text
/config/custom_components/jbl_proscan
```

Restart Home Assistant, then add **JBL ProScan** from **Settings → Devices & services**.

### Lovelace card

Copy:

```text
www/jbl-proscan-card.js
```

to:

```text
/config/www/jbl-proscan-card.js
```

Add this Dashboard resource as a JavaScript module:

```text
/local/jbl-proscan-card.js?v=1.0.0
```

Then add **JBL ProScan** through the visual card picker or use:

```yaml
type: custom:jbl-proscan-card
entity: sensor.bassin_historique
title: Bassin — JBL ProScan
measurements: 100
show_co2: true
stale_warning_days: 14
stale_critical_days: 30
```

## Logo

The folder `brands/custom_integrations/jbl_proscan` is ready to be copied into a fork of the `home-assistant/brands` repository. These files are not read directly from this repository by Home Assistant.

## GitHub graphical upload

Create an empty public repository without generating a README, licence or `.gitignore`. Extract this archive and upload all files and folders from its root using **Add file → Upload files**.

## Important HACS note

HACS treats integrations and dashboard cards as different repository categories. This combined repository is designed for GitHub publication and manual installation. For one-click HACS installation of both parts, publish the integration and card as two separate repositories.
