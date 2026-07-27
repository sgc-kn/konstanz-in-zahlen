---
title: Tourismus
source: Statistisches Landesamt Baden-Württemberg (Tourismusstatistik)
order: 4
columns:
- name: jahr
  type: int
  description: Jahr
  short: Ankünfte und Übernachtungen in der Stadt Konstanz seit 2004
  export_id: Jahr der Erhebung
- name: ankuenfte
  type: int
  description: Gesamte Ankünfte 
  unit: Anzahl Ankünfte
  export_id: Ankünfte insgesamt
- name: ankuenfte_ausland
  type: int
  description: darunter Gäste aus Ausland
  unit: Anzahl Ankünfte
  short: TOFIX
  export_id: 'Ankünfte: darunter Gäste aus Ausland'
- name: uebernachtungen
  type: int
  description: Gesamte Übernachtungen
  unit: Anzahl Übernachtungen
  export_id: Übernachtungen insgesamt
- name: uebernachtungen_ausland
  type: int
  description: darunter Gäste aus Ausland
  unit: Anzahl Übernachtungen
  short: TOFIX
  export_id: 'Übernachtungen: darunter Gäste aus Ausland'
- name: deutschland
  type: Optional[int]
  description: 'Herkunftsland: Deutschland'
  unit: Anzahl Übernachtungen
  short: Deutschland
  export_id: 'Übernachtungen nach Herkunftsländern: Deutschland'
- name: schweiz
  type: Optional[int]
  description: 'Herkunftsland: Schweiz'
  unit: Anzahl Übernachtungen
  short: Schweiz
  export_id: 'Übernachtungen nach Herkunftsländern: Schweiz'
- name: frankreich
  type: Optional[int]
  description: 'Herkunftsland: Frankreich'
  unit: Anzahl Übernachtungen
  short: Frankreich
  export_id: 'Übernachtungen nach Herkunftsländern: Frankreich'
- name: oesterreich
  type: Optional[int]
  description: 'Herkunftsland: Österreich'
  unit: Anzahl Übernachtungen
  short: Österreich
  export_id: 'Übernachtungen nach Herkunftsländern: Österreich'
- name: sonstige
  type: Optional[int]
  description: 'Herkunftsland: Sonstige Länder'
  unit: Anzahl Übernachtungen
  short: sonstige Länder
  export_id: 'Übernachtungen nach Herkunftsländern: sonstige Länder'
---
Anmerkungen: Beherbergungsstatistik ist eine statistische Erfassung und Auswertung von Ankunfts- und Übernachtungszahlen in der Tourismusbranche. Die Beherbergungsstatistik bezieht sich auf Einrichtungen für die vorübergehende Beherbergung (unter zwei Monaten) von Gästen. Seit Januar 2012 werden Beherbergungsstätten mit zehn und mehr Betten sowie Campingplätze mit zehn und mehr Stellplätzen erfasst. Zuvor hatte eine niedrigere Abschneidegrenze von neun und mehr Schlafgelegenheiten gegolten. Kleinbetriebe mit weniger Betten bzw. Stellplätzen sind also in der Darstellung eben so wenig enthalten wie das Dauercamping bei den Campingplätzen. 

- Herkunftsland: Maßgebend ist grundsätzlich der ständige Wohnsitz oder der gewöhnliche Aufenthaltsort eines Gastes, nicht dagegen dessen Staatsangehörigkeit bzw. Nationalität.
- Gäste aus Ausland: Auch hier zählt der Wohnsitz und nicht die Nationalität des Gastes. 
