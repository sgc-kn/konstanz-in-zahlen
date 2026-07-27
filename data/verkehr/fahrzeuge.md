---
title: Kraftfahrzeugbestand
source: Kraftfahrt-Bundesamt
columns:
- name: jahr
  type: int
  description: Jahr (Stichtag 01.01. des Folgejahres)
  short: Kraftfahrzeugbestand der Stadt Konstanz seit 2000
  export_id: Jahr
- name: pkw_privat
  type: Optional[int]
  description: Pkw pro 1.000 Einw. (Wohnbevölkerung)
  unit: Anzahl
  export_id: Pkw je 1.000 Einw. (Wohnbevölkerung)
- name: pkw_insgesamt
  type: Optional[int]
  description: Pkw (privat + gewerblich)
  unit: Anzahl
  short: Pkw insgesamt (privat + gewerblich)
  export_id: Personenkraftwagen (privat + gewerblich)
- name: nutzfahrzeug
  type: int
  description: Nutzfahrzeuge
  unit: Anzahl
  export_id: Nutzfahrzeuge
- name: kraftrad
  type: int
  description: Krafträder
  unit: Anzahl
  export_id: Krafträder
---
Anmerkungen: Statistik des Kraftfahrt-Bundesamt. 

- Pkw pro 1.000 Einwohner: Privat und gewerblich zugelassene Personenkraftwagen je 1.000 Einwohner (Wohnbevölkerung, eigene Fortschreibung Stadt Konstanz).
- Pkw insgesamt: Bestand an privat und gewerblich zugelassenen Personenkraftwagen.
- Nutzfahrzeug: Kraftfahrzeug, das auf Grund seiner Bauart zum Transport von Personen, Gütern und/oder zum Ziehen von Anhängefahrzeugen bestimmt ist.
- Kraftrad: zwei und dreirädrige Kraftfahrzeuge (z.B. Roller, Motorrad) sowie leichte vierrädrigen Kraftfahrzeuge (bis 425 kg Leermasse, bis 45 km/h, bis 50 Kubikzentimeter).


- Ab 2008 wurden nur noch angemeldete Fahrzeuge gezählt, maßgebend ist hier der Wohnort des Halters.
