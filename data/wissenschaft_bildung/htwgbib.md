---
title: Bibliothek der HTWG
source: HTWG Hochschule Konstanz Technik, Wirtschaft und Gestaltung
columns:
- name: jahr
  type: int
  description: Jahr der Erhebung
  short: Jahr
- name: bestand
  type: int
  description: Medienbestand
  short: Medienbestand
- name: bdigital
  type: Optional[int]
  description: 'Medienbestand: davon elektronisch'
  short: davon elektronisch
- name: zeitschrifen
  type: Optional[int]
  description: Zeitschriften/eJournals
  short: Zeitschriften/eJournals
- name: zdigital
  type: Optional[int]
  description: 'Zeitschriften/eJournals: davon elektronisch'
  short: davon elektronisch
- name: ausleihe
  type: int
  description: Ausleihen
  short: Ausleihen
- name: downloads
  type: Optional[int]
  description: Online-Ausleihen/ Downloads
  short: Online-Ausleihen/ Downloads
- name: besucher
  type: Optional[int]
  description: BibliotheksbesucherInnen
  short: BibliotheksbesucherInnen
---
Anmerkungen:

- downloads: Ab 2022 gerundete Werte
