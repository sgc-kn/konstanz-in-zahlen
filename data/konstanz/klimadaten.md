---
title: Klimadaten
source: Deutscher Wetterdienst (DWD)
columns:
- name: jahr
  type: int
  description: Jahr
  export_id: Jahr
- name: temperatur
  type: float
  description: Lufttemperatur (Jahresmittel) seit 2000
  unit: °C (⌀)
  export_id: Lufttemperatur Jahresmittel (in °C)
- name: niederschlag
  type: float
  description: Niederschlag (Jahressumme) seit 2000
  unit: mm pro Jahr
  export_id: Niederschlag (Jahresmenge in mm)
- name: sonne
  type: Optional[float]
  description: Sonnenscheindauer (Jahressumme) seit 2000
  unit: Stunden pro Jahr
  export_id: Sonnenscheindauer (Stunden im Jahr)
---
Anmerkungen: Der Deutsche Wetterdienst stellt Klimadaten mit den jährlichen Stationswerten für die Station Konstanz (ID: 2712) im „Climate Data Center“ (https://cdc.dwd.de/portal) zur Verfügung.

- Jahresmittel der Stationsmessungen der Lufttemperatur in 2 m Höhe in °C
- Jahressumme der Stationsmessungen der Niederschlagshöhe in mm
- Jahressumme der Stationsmessungen der Sonnenscheindauer in Stunden
