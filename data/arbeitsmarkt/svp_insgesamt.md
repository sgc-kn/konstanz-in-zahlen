---
title: Sozialvers.-pflichtig Beschäftigte (jeweils Juni)
teaser: Text
source: Bundesagentur für Arbeit (BA)
columns:
- name: jahr
  type: int
  description: Jahr (Stichtag 30. Juni)
  short: Jahr
- name: wohnort
  type: int
  description: am  Wohnort
  short: am  Wohnort
- name: auspendler
  type: int
  description: darunter Berufsauspendler
  short: darunter Berufsauspendler
- name: arbeitsort
  type: int
  description: am Arbeitsort
  short: am Arbeitsort
- name: einpendler
  type: int
  description: darunter Berufseinpendler
  short: darunter Berufseinpendler
- name: produzierend
  type: int
  description: 'nach Wirtschaftsbereichen: Produzierendes Gewerbe'
  short: produzierendes Gewerbe
- name: anteil_produzierend
  type: float
  computed: (self.produzierend / self.arbeitsort) * 100
  description: produzierendes Gewerbe (%)
  unit: Prozent
- name: handel
  type: int
  description: 'nach Wirtschaftsbereichen: Handel, Gastgewerbe und Verkehr'
  short: Handel, Gastgewerbe und Verkehr
- name: anteil_handel
  type: float
  computed: (self.handel / self.arbeitsort) * 100
  description: Handel, Gastgewerbe und Verkehr (%)
  unit: Prozent
- name: sonstige
  type: int
  description: 'nach Wirtschaftsbereichen: Sonstige Dienstleistungen'
  short: sonstige Dienstleistungen
- name: anteil_sonstige
  type: float
  computed: (self.sonstige / self.arbeitsort) * 100
  description: sonstige Dienstleistungen (%)
  unit: Prozent
---
