---
title: Universitätsbibliothek
source: Universität Konstanz (Kommunikations-, Informations-, Medienzentrum)
columns:
- name: jahr
  type: int
  description: Jahr
- name: bestand
  type: int
  description: Medienbestand
- name: bdigital
  type: Optional[int]
  description: 'Medienbestand: davon elektronisch'
  short: davon elektronisch
- name: zeitschrifen
  type: Optional[int]
  description: Zeitschriften (lfd. gehalten)
- name: zdigital
  type: Optional[int]
  description: 'Zeitschriften: davon elektronisch'
  short: davon elektronisch
- name: ausleihe
  type: int
  description: Ausleihen
- name: downloads
  type: Optional[int]
  description: Elektronische Downloads
  short: elektronische Downloads
- name: besucher
  type: Optional[int]
  description: BibliotheksbesucherInnen
---
