# JBL ProScan

[![GitHub Release][releases-shield]][releases]
[![License][license-shield]](LICENSE)
[![Home Assistant](https://img.shields.io/badge/Home%20Assistant-2026.3%2B-41BDF5.svg?style=flat-square&logo=homeassistant)](https://www.home-assistant.io/)
[![HACS Custom](https://img.shields.io/badge/HACS-Custom-41BDF5.svg?style=flat-square)](https://hacs.xyz/)
[![Maintainer](https://img.shields.io/badge/Maintainer-AuroreVgn-blue.svg?style=flat-square)](https://github.com/AuroreVgn)

## 🏠 Mes projets Home Assistant

Retrouvez l'ensemble de mes intégrations et projets Home Assistant sur ma page dédiée : [**🏠 Découvrir mes projets Home Assistant**](https://gentle-suggestion-7c3.notion.site/Mes-projets-Home-Assistant-3eda02eefa8f81a48621c3caeef7fa8e)

## ☕ Soutenir le projet

Si cette intégration vous est utile et que vous souhaitez soutenir son développement et sa maintenance :

<p>
  <a href="https://ko-fi.com/aurorevgn">
    <img src="https://storage.ko-fi.com/cdn/kofi4.png?v=3" alt="Soutenir sur Ko-fi" height="45">
  </a>
</p>

## 🌍 Other languages

[English](README.en.md)

## ⚠️ Important

Intégration personnalisée Home Assistant pour **JBL ProScan**, permettant de récupérer les analyses d'eau de votre **bassin** ou **aquarium** directement depuis votre compte **myJBL**.

## ✨ Fonctionnalités

- 🔐 Authentification sécurisée à **myJBL**
- 🌊 Sélection automatique des bassins et aquariums
- 📊 Historique complet des analyses
- 🔄 Service d'actualisation manuelle
- 📈 Compatibilité avec les statistiques longue durée
- 🤖 Capteurs binaires pour les automatisations
- 🌍 Prise en charge de plusieurs langues
- ⚡ Configuration native via l'interface Home Assistant

## 📸 Captures d'écran

### Configuration
<img width="450" src="https://github.com/user-attachments/assets/09e357ca-72af-489c-bd66-f16c78006d31"/>

### Entités
<img width="250" alt="Entités JBL ProScan" src="https://github.com/user-attachments/assets/04da4e02-f774-4e2f-98c3-c452e3ff5f17" />

## 📦 Installation

### HACS (recommandé)

#### Ajouter le dépôt

Automatiquement :

[![Ouvrir ce dépôt dans HACS](https://my.home-assistant.io/badges/hacs_repository.svg)](https://my.home-assistant.io/redirect/hacs_repository/?owner=AuroreVgn&repository=JBL_ProScan&category=integration)

Ou manuellement :

```text
HACS
 └── Intégrations
      └── ⋮
           └── Dépôts personnalisés

Dépôt :
https://github.com/AuroreVgn/JBL_ProScan

Catégorie :
Integration
```

#### Installer

```text
HACS
 └── JBL ProScan
      └── Télécharger
```

Redémarrez Home Assistant.

## ⚙️ Configuration

Accédez à :

```text
Paramètres
→ Appareils et services
→ Ajouter une intégration
→ JBL ProScan
```

Renseignez votre adresse e-mail et votre mot de passe **myJBL**, puis sélectionnez le bassin ou l'aquarium à importer.

## 📊 Capteurs

### Paramètres de l'eau
- pH
- KH
- GH
- NO₂
- NO₃
- CO₂
- Chlore

### Capteurs supplémentaires
- Historique
- Dernière analyse
- Nombre de jours depuis la dernière analyse

### Capteurs binaires
- pH OK
- KH OK
- GH OK
- Nitrites élevés
- Nitrates élevés
- Chlore élevé
- Analyse en retard

## 📊 Entités créées

### Capteurs

| Entité | Unité |
|---|---|
| pH | — |
| KH | °dKH |
| GH | °dGH |
| NO₂ | mg/L |
| NO₃ | mg/L |
| CO₂ | mg/L |
| Chlore | mg/L |
| Historique | analyses |
| Dernière analyse | Date |
| Jours depuis la dernière analyse | jour |

Tous les capteurs de mesure sont compatibles avec les **statistiques longue durée de Home Assistant**.

### Capteurs binaires

L'intégration crée également des capteurs binaires destinés aux automatisations :
- pH OK
- KH OK
- GH OK
- Nitrites élevés
- Nitrates élevés
- Chlore élevé
- Analyse en retard

### Services

L'intégration fournit le service suivant :

#### Actualiser les données

```text
jbl_proscan.refresh
```

Actualise immédiatement les données du bassin sélectionné, sans attendre la prochaine mise à jour programmée.

Ce service peut être utilisé dans les tableaux de bord et les automatisations.

### Automatisations

Les capteurs binaires permettent notamment de créer un rappel lorsqu'aucune analyse n'a été réalisée depuis un certain nombre de jours.

### Tableau de bord

➡️ https://github.com/AuroreVgn/JBL_ProScan_card

## 🧩 Carte Lovelace associée

Une carte Lovelace dédiée est disponible : https://github.com/AuroreVgn/JBL_ProScan_card

Ses fonctionnalités comprennent :
- 📈 Graphiques interactifs
- 🎨 Couleurs personnalisées
- 🎭 Icônes personnalisées
- 🌍 Plusieurs langues
- 🔄 Actualisation manuelle
- 📅 Sélection de période
- 📊 Comparaison avec l'analyse précédente
- 📉 Plages recommandées JBL
- 🖱 Infobulles interactives
- 🧩 Éditeur visuel

## 🙏 Remerciements

Développé par **AuroreVgn**.

Merci à la communauté Home Assistant.

Ce projet **n'est pas affilié à JBL GmbH & Co. KG**.

## 📄 Licence

Distribué sous licence MIT.

[releases-shield]: https://img.shields.io/github/v/release/AuroreVgn/JBL_ProScan?style=flat-square
[releases]: https://github.com/AuroreVgn/JBL_ProScan/releases
[license-shield]: https://img.shields.io/github/license/AuroreVgn/JBL_ProScan?style=flat-square
