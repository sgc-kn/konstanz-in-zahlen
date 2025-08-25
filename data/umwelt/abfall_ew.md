---
title: Abfall- und Wertstoffmenge je Einw. in kg
teaser: Text
source: Entsorgungsbetriebe Konstanz
columns:
- name: jahr
  type: int
  description: Jahr der Erhebung
  short: Jahr
- name: rest
  type: int
  description: Restmüll
  unit: kg pro Einwohner
  short: Restmüll
- name: bio
  type: int
  description: Biomüll
  unit: kg pro Einwohner
  short: Biomüll
- name: glas
  type: Optional[int]
  description: Glas
  unit: kg pro Einwohner
  short: Glas
- name: papier
  type: int
  description: Papier
  unit: kg pro Einwohner
  short: Papier
- name: gruen
  type: int
  description: Grünabfall
  unit: kg pro Einwohner
  short: Grünabfall
- name: gelb
  type: int
  description: Gelber Sack
  unit: kg pro Einwohner
  short: Gelber Sack
- name: sperr
  type: Optional[int]
  description: Sperrmüll
  unit: kg pro Einwohner
  short: Sperrmüll
- name: sonstige
  type: Optional[int]
  description: sonstige Wertstoffe (Holz, Metall, E-Schrott)
  unit: kg pro Einwohner
  short: sonstige Wertstoffe (Holz, Metall, E-Schrott)
---
Anmerkungen:

- amtliche Einwohnerzahl des Vorjahres
