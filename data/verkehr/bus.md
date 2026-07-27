---
title: Bus
source: Stadtwerke Konstanz
columns:
- name: jahr
  type: int
  description: Jahr
  short: Omnibusbestand der Stadtwerke Konstanz seit 2000
  export_id: Jahr der Erhebung
- name: bestand
  type: int
  description: Omnibusbestand
  unit: Anzahl Busse
  export_id: Omnibusbestand
- name: davon_e
  type: Optional[int]
  description: darunter E-Busse
  unit: Anzahl Busse
  export_id: darunter E-Bus
- name: personen
  type: float
  description: Bus Fahrgäste (D-Ticket nicht inklusive) seit 2000
  unit: Anzahl Fahrgäste (Mio.)
  short: beförderte Personen (Mio.) - ohne D-Ticket
  export_id: Beförderte Personen - ohne D-Ticket
- name: strecke
  type: Optional[float]
  description: Busstreckenentwicklung seit 2004
  unit: km
  short: Busstrecke (in km)
  export_id: Busstrecke
---
Anmerkungen: Weiter Informationen finden Sie unter: https://www.stadtwerke-konstanz.de/bus/infos/ .

- Fahrgäste:
     Durch die Corona-Pandemie kam es 2020 und 2021 zu Rückgängen bei der Anzahl der Fahrgäste.
     Fahrgäste mit Deutschland-Ticket sind ab 2022 nicht in den Daten enthalten.
- Busstrecke: Hier handelt es sich um die Länge der Strecke des Busnetzes.
