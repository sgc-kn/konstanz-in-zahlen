---
title: Sozialvers.-pflichtig Beschäftigte (jeweils Juni)
source: Bundesagentur für Arbeit (BA)
columns:
- name: jahr
  type: int
  description: Jahr (Stichtag 30. Juni)
  short: Sozialvers.-pflichtig Beschäftigte nach Wirtschaftsbereich und Arbeitsort seit 2000
  export_id: Jahr (Stichtag 30. Juni)
- name: wohnort
  type: int
  description: am Wohnort
  unit: Anzahl Beschäftigte
  export_id: am Wohnort
- name: auspendler
  type: int
  description: darunter Berufsauspendler
  unit: Anzahl Beschäftigte
  export_id: darunter Berufsauspendler
- name: arbeitsort
  type: int
  description: am Arbeitsort
  unit: Anzahl Beschäftigte
  export_id: am Arbeitsort
- name: einpendler
  type: int
  description: darunter Berufseinpendler
  unit: Anzahl Beschäftigte
  export_id: darunter Berufseinpendler
- name: produzierend
  type: int
  description: 'nach Wirtschaftsbereichen: Produzierendes Gewerbe'
  unit: Anzahl Beschäftigte
  short: produzierendes Gewerbe
  export_id: 'nach Wirtschaftsbereichen: Produzierendes Gewerbe'
- name: anteil_produzierend
  type: float
  description: produzierendes Gewerbe (%)
  unit: "%"
  computed: (self.produzierend / self.arbeitsort) * 100
  export_id: produzierendes Gewerbe (%)
- name: handel
  type: int
  description: 'nach Wirtschaftsbereichen: Handel, Gastgewerbe und Verkehr'
  unit: Anzahl Beschäftigte
  short: Handel, Gastgewerbe und Verkehr
  export_id: 'nach Wirtschaftsbereichen: Handel, Gastgewerbe und Verkehr'
- name: anteil_handel
  type: float
  description: Handel, Gastgewerbe und Verkehr (%)
  export_id: Handel, Gastgewerbe und Verkehr (%)
  unit: "%"
  computed: (handel / arbeitsort) * 100
- name: sonstige
  type: int
  description: 'nach Wirtschaftsbereichen: Sonstige Dienstleistungen'
  unit: Anzahl Beschäftigte
  short: sonstige Dienstleistungen
  export_id: 'nach Wirtschaftsbereichen: Sonstige Dienstleistungen'
- name: anteil_sonstige
  type: float
  export_id: sonstige Dienstleistungen (%)
  description: sonstige Dienstleistungen (%)
  unit: "%"
  computed: (sonstige / arbeitsort) * 100
---
Anmerkungen: 

- Sozialversicherungspflichtig Beschäftigte am Wohnort zum 30.06., wobei die Beschäftigten in der Stadt Konstanz wohnen, unabhängig davon wo sie arbeiten.
- Sozialversicherungspflichtig Beschäftigte am Arbeitsort, wobei die Betriebe der Beschäftigten ihren Sitz in der Stadt Konstanz haben. 
- Berufspendler sind alle sozialversicherungspflichtig Beschäftigten, deren Arbeitsort sich vom Wohnort unterscheidet. Berufseinpendler wohnen nicht an ihrem Arbeitsort, Berufsauspendler arbeiten nicht an ihrem Wohnort. Ob und wie häufig gependelt wird, ist unerheblich. Der Wohnort kann auch im Ausland liegen, der Arbeitsort - wegen des Inlandskonzepts der Beschäftigungsstatistik - jedoch nicht.
- Wirtschaftsbereich nach Klassifikation der Wirtschaftszweige, Ausgabe 2008 (WZ 2008).
