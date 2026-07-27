---
title: Bibliothek der HTWG
source: HTWG Hochschule Konstanz Technik, Wirtschaft und Gestaltung
columns:
- name: jahr
  type: int
  description: Jahr
  short: Bestand und Nutzung der Bibliothek der HTWG seit 2000
  unit: Anzahl
  export_id: Jahr der Erhebung
- name: bestand
  type: int
  description: Medienbestand
  unit: Anzahl
  export_id: Medienbestand
- name: bdigital
  type: Optional[int]
  description: 'Medienbestand: davon elektronisch'
  unit: Anzahl
  short: davon elektronisch
  export_id: 'Medienbestand: davon elektronisch'
- name: zeitschrifen
  type: Optional[int]
  description: Zeitschriften/eJournals
  unit: Anzahl
  export_id: Zeitschriften/eJournals
- name: zdigital
  type: Optional[int]
  description: 'Zeitschriften/eJournals: davon elektronisch'
  unit: Anzahl
  short: davon elektronisch
  export_id: 'Zeitschriften/eJournals: davon elektronisch'
- name: ausleihe
  type: int
  description: Ausleihen
  unit: Anzahl
  export_id: Ausleihen
- name: downloads
  type: Optional[int]
  description: Online-Ausleihen/ Downloads
  unit: Anzahl
  export_id: Online-Ausleihen/ Downloads
- name: besucher
  type: Optional[int]
  description: BibliotheksbesucherInnen
  unit: Anzahl
  export_id: BibliotheksbesucherInnen
---
Anmerkungen: Ab 2022 werden bei den Downloads gerundete Werte angegeben.
