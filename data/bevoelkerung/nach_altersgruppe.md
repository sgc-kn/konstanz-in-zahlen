---
title: Wohnbevölkerung nach Altersgruppen
source: Stadt Konstanz, Amt für Digitalisierung und IT (eigene Einwohnerfortschreibung)
order: 3
columns:
- name: jahr
  type: int
  description: Jahr
  short: Wohnbevölkerung der Stadt Konstanz nach Altersgruppen seit 2000
  export_id: Jahr
- name: bis_18
  type: Optional[int]
  description: 0 bis unter 18 Jahre
  unit: Anzahl Personen
  short: 0 bis unter 18
  export_id: Anzahl Einwohner, 0 bis unter 18 Jahre
- name: bis_30
  type: Optional[int]
  description: 18 bis unter 30 Jahre
  unit: Anzahl Personen
  short: 18 bis unter 30
  export_id: Anzahl Einwohner, 18 bis unter 30 Jahre
- name: bis_40
  type: Optional[int]
  description: 30 bis unter 40 Jahre
  unit: Anzahl Personen
  short: 30 bis unter 40
  export_id: Anzahl Einwohner, 30 bis unter 40 Jahre
- name: bis_50
  type: Optional[int]
  description: 40 bis unter 50 Jahre
  unit: Anzahl Personen
  short: 40 bis unter 50
  export_id: Anzahl Einwohner, 40 bis unter 50 Jahre
- name: bis_60
  type: Optional[int]
  description: 50 bis unter 60 Jahre
  unit: Anzahl Personen
  short: 50 bis unter 60
  export_id: Anzahl Einwohner, 50 bis unter 60 Jahre
- name: ueber_60
  type: Optional[int]
  description: 60 Jahre und älter
  unit: Anzahl Personen
  short: 60 und älter
  export_id: Anzahl Einwohner, 60 Jahre und älter
---
Anmerkungen: Wohnbevölkerung (Einwohner mit Hauptwohnsitz) in Konstanz nach Altersgruppen zum Stichtag 31.12. des jeweiligen Jahres.
