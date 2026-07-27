---
title: Abwasser
source: Entsorgungsbetriebe Konstanz
order: 5
columns:
- name: jahr
  type: int
  description: Jahr
  short: Reinigungsleistung für verschiedene Verschmutzungen seit 2001
  export_id: Jahr der Erhebung
- name: menge
  type: float
  description: In Kläranlage behandelte Schmutzwassermenge seit 2001
  unit: Mio. m³ pro Jahr
  short: in Kläranlage behandelte Schmutzwassermenge (in Mio m³ pro Jahr)
  export_id: in Kläranlage behandelte Schmutzwassermenge (in Mio. m³/Jahr)
- name: ew
  type: float
  description: Angeschlossene Einwohnerwerte (EW) seit 2001
  unit: Einwohnerwerte (Mio. kWh)
  export_id: angeschlossene Einwohnerwerte (EW)
- name: organisch
  type: float
  description: Reinigungsleistung (organische Verschmutzung)
  unit: '%'
  short: organische Verschmutzung (in %)
  export_id: Reinigungsleistung bez. auf organische Verschmutzung (in %)
- name: phosphor
  type: float
  description: Reinigungsleistung (Phosphorelimination)
  unit: '%'
  short: Phosphorelimination (in %)
  export_id: Reinigungsleistung bez. auf Phosphorelimination (in %)
---
Anmerkungen:
An die Zentralkläranlage Konstanz sind auch die Gemeinden Allensbach, Reichenau und Kreuzlingen (CH), Tägerwilen (CH) und Gottlieben (CH) angeschlossen.

- EW = Einwohner + in Einwohneräquivalente umgerechnete Schmutzfrachten aus Touristik, Gewerbe und Industrie. 
  - Mithilfe des Einwohnerwertes (EW) lässt sich die Belastung der Kläranlage abschätzen. Grundsätzlich sind die zu behandelnden Abwassermengen wegen der Mischkanalisation (Abfluss von Schmutz- und Regenwasser in einem Kanalsystem) wesentlich durch die Niederschlagsereignisse im Laufe des Jahres mitverursacht. 
- Abwasser: Wasser, das durch bauliche Maßnahmen abgeleitet wird (Schmutzwasser aus Haushaltsabflüssen, Niederschlagswasser durch Straßenabflüsse o.ä., Fremdwasser durch bauliche Schäden).
- Phosphorelimination: Abwasserreinigung durch die Entfernung von Phosphorverbindungen aus Abwässern in der Kläranlage. Phosphor ist ein Pflanzennährstoff, der im Überschuss zur Nährstoffüberlastung von Gewässern und somit biologischen Kollabs des Gewässers führen kann.
