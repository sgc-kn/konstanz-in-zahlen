---
title: Klimadaten
teaser: Text
source: Deutscher Wetterdienst (DWD)
columns:
- name: jahr
  type: int
  description: Jahr der Erhebung
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
