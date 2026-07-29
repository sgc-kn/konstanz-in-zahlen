---
title: Sozialversicherungspflichtig Beschäftigte nach Alter (jeweils Juni)
source: Bundesagentur für Arbeit (BA)
columns:
- name: jahr
  type: int
  description: Jahr (Stichtag 30. Juni)
  short: Sozialvers.-pflichtig Beschäftigte gruppiert nach Alter seit 2000
  export_id: Jahr (Stichtag 30. Juni)
- name: gesamt
  type: int
  description: am Arbeitsort gesamt
  unit: Anzahl Beschäftigte
  export_id: am Arbeitsort gesamt
- name: unter25
  type: int
  description: unter 25 Jahre
  unit: Anzahl Beschäftigte
  export_id: unter 25 Jahre
- name: ueber55
  type: Optional[int]
  description: 55 Jahre und älter
  unit: Anzahl Beschäftigte
  export_id: 55 Jahre und älter
---
Anmerkungen: Sozialversicherungspflichtig Beschäftigte am Arbeitsort, wobei die Betriebe der Beschäftigten ihren Sitz in der Stadt Konstanz haben, zum Stichtag 30.06.

Durch eine Umstellung bei der Ausgabe der Merkmale, liegen die Daten für die 55 Jahre und älteren sozialversicherungspflichtig Beschäftigten erst ab 2007 vor.
