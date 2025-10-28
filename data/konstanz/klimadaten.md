---
title: Klimadaten
teaser: Text
source: Deutscher Wetterdienst (DWD)
columns:
- name: jahr
  type: int
  description: Jahr 
  short: Jahr
- name: temperatur
  type: float
  description: Lufttemperatur Jahresmittel (in °C)
  unit: °C
  short: Lufttemperatur Jahresmittel (in °C)
- name: niederschlag
  type: float
  description: Niederschlag (Jahresmenge in mm)
  unit: mm pro Jahr
  short: Niederschlag (Jahresmenge in mm)
- name: sonne
  type: Optional[float]
  description: Sonnenscheindauer (Stunden im Jahr)
  unit: Stunden pro Jahr
  short: Sonnenscheindauer (Stunden im Jahr)
---
Anmerkung: Der Deutsche Wetterdienst stellt Klimadaten im „Climate Data Center“ (https://cdc.dwd.de/portal) zur Verfügung mit den jährlichen Stationswerten für die Station Konstanz (ID: 2712): 
- „Jahresmittel der Stationsmessungen der Lufttemperatur in 2 m Höhe in °C“
- „Jahressumme der Stationsmessungen der Niederschlagshöhe in mm“ 
- „Jahressumme der Stationsmessungen der Sonnenscheindauer in Stunden“.
