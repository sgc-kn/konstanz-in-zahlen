---
title: Wohnbevölkerung nach Staatsangehörigkeit
source: Stadt Konstanz, Amt für Digitalisierung und IT (eigene Einwohnerfortschreibung)
columns:
- name: jahr
  type: int
  description: Jahr der Erhebung
  short: Jahr
- name: gesamt
  type: int
  description: insgesamt
  short: insgesamt
- name: deutsch
  type: int
  description: Deutsche
  short: Deutsche
- name: nichtdeutsch
  type: int
  description: Nichtdeutsche
  short: Nichtdeutsche
- name: in_prozent
  type: float
  computed: (self.nichtdeutsch / self.gesamt) * 100
  description: in %
  unit: Prozent
- name: eu
  type: int
  description: darunter EU Staaten (ohne Dtl.)
  short: darunter EU Staaten (ohne D)
- name: nichteu
  type: int
  description: darunter Europa (Ohne EU)
  short: darunter Europa (Ohne EU)
- name: asien
  type: int
  description: darunter Asien
  short: darunter Asien
- name: afrika
  type: int
  description: darunter Afrika
  short: darunter Afrika
- name: amerika
  type: int
  description: darunter Amerika
  short: darunter Amerika
---
Anmerkungen: Wohnbevölkerung (Einwohner mit Hauptwohnsitz) nach erster Staatsangehörigkeit nach Deutsch / Nichtdeutsch sowie Nichtdeutsche nach Kontinent (Europa - EU-Staaten, Europa - ohne EU-Staaten; Asien, Afrika, Amerika).
