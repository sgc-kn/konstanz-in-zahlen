---
title: Bus
source: Stadtwerke Konstanz
columns:
- name: jahr
  type: int
  description: Jahr der Erhebung
  short: Jahr
- name: bestand
  type: int
  description: Omnibusbestand
  short: Omnibusbestand
- name: davon_e
  type: Optional[int]
  description: darunter E-Bus
  short: darunter E-Bus
- name: personen
  type: float
  description: Beförderte Personen - ohne D-Ticket
  unit: Mio.
  short: beförderte Personen (in Mio.) - ohne D-Ticket
- name: strecke
  type: Optional[float]
  description: Busstrecke
  unit: km
  short: Busstrecke (in km)
---
