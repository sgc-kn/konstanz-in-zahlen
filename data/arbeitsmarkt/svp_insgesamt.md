---
title: Sozialvers.-pflichtig Beschäftigte (jeweils Juni)
source: Bundesagentur für Arbeit (BA)
columns:
- name: jahr
  type: int
  description: Jahr (Stichtag 30. Juni)
  short: Jahr
- name: wohnort
  type: int
  description: am  Wohnort
- name: auspendler
  type: int
  description: darunter Berufsauspendler
- name: arbeitsort
  type: int
  description: am Arbeitsort
- name: einpendler
  type: int
  description: darunter Berufseinpendler
- name: produzierend
  type: int
  description: 'nach Wirtschaftsbereichen: Produzierendes Gewerbe'
  short: produzierendes Gewerbe
- name: anteil_produzierend
  type: float
  description: produzierendes Gewerbe (%)
  unit: Prozent
  computed: (self.produzierend / self.arbeitsort) * 100
- name: handel
  type: int
  description: 'nach Wirtschaftsbereichen: Handel, Gastgewerbe und Verkehr'
  short: Handel, Gastgewerbe und Verkehr
- name: anteil_handel
  type: float
  description: Handel, Gastgewerbe und Verkehr (%)
  unit: Prozent
  computed: (self.handel / self.arbeitsort) * 100
- name: sonstige
  type: int
  description: 'nach Wirtschaftsbereichen: Sonstige Dienstleistungen'
  short: sonstige Dienstleistungen
- name: anteil_sonstige
  type: float
  description: sonstige Dienstleistungen (%)
  unit: Prozent
  computed: (self.sonstige / self.arbeitsort) * 100
---
Anmerkung: Sozialversicherungspflichtig Beschäftigte am Wohnort, wobei die Beschäftigten in der Stadt Konstanz wohnen, unabhängig davon wo sie arbeiten.
Sozialversicherungspflichtig Beschäftigte am Arbeitsort, wobei die Betriebe der Beschäftigten ihren Sitz in der Stadt Konstanz haben. 
Berufspendler sind alle sozialversicherungspflichtig Beschäftigten, deren Arbeitsort sich vom Wohnort unterscheidet. Berufseinpendler wohnen nicht an ihrem Arbeitsort, Berufsauspendler arbeiten nicht an ihrem Wohnort. Ob und wie häufig gependelt wird, ist unerheblich. Der Wohnort kann auch im Ausland liegen, der Arbeitsort - wegen des Inlandskonzepts der Beschäftigungsstatistik - jedoch nicht.
Wirtschaftsbereich nach Klassifikation der Wirtschaftszweige, Ausgabe 2008 (WZ 2008).
Alle Daten zum Sichtag 30.06.
