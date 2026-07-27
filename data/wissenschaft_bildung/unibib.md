---
title: Universitätsbibliothek
source: Universität Konstanz (Kommunikations-, Informations-, Medienzentrum)
columns:
- name: jahr
  type: int
  description: Jahr
  short: Bestand und Nutzung der Universitätsbibliothek seit 2000
  export_id: Jahr
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
  description: Zeitschriften (lfd. gehalten)
  unit: Anzahl
  export_id: Zeitschriften (lfd. gehalten)
- name: zdigital
  type: Optional[int]
  description: 'Zeitschriften: davon elektronisch'
  unit: Anzahl
  short: davon elektronisch
  export_id: 'Zeitschriften: davon elektronisch'
- name: ausleihe
  type: int
  description: Ausleihen
  unit: Anzahl
  export_id: Ausleihen
- name: downloads
  type: Optional[int]
  description: Elektronische Downloads
  unit: Anzahl
  short: elektronische Downloads
  export_id: Elektronische Downloads
- name: besucher
  type: Optional[int]
  description: BibliotheksbesucherInnen
  unit: Anzahl
  export_id: BibliotheksbesucherInnen
---
