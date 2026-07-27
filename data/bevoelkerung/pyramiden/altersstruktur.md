---
title: Altersstruktur der Wohnbevölkerung
source: Stadt Konstanz, Amt für Digitalisierung und IT (eigene Einwohnerfortschreibung)
columns:
- name: alter
  type: str
  description: Alter in Jahren
  short: Alter
  export_id: Alter in Jahren
- name: maenner_nichtdeutsch
  type: Optional[int]
  description: Männer - nichtdeutsch
  unit: Anzahl Personen
  export_id: Männer - nichtdeutsch
- name: frauen_nichtdeutsch
  type: Optional[int]
  description: Frauen - nichtdeutsch
  unit: Anzahl Personen
  export_id: Frauen - nichtdeutsch
- name: maenner_deutsch
  type: Optional[int]
  description: Männer - deutsch
  unit: Anzahl Personen
  export_id: Männer - deutsch
- name: frauen_deutsch
  type: Optional[int]
  description: Frauen - deutsch
  unit: Anzahl Personen
  export_id: Frauen - deutsch
---
Anmerkungen: - Die Bevölkerungspyramide stellt die Anzahl der Einwohner der Stadt Konstanz nach Alter, Geschlecht und deutscher, bzw. nichtdeutscher Staatsangehörigkeit dar.
- Jeder Balken entspricht der Anzahl der Einwohner in dem jeweiligen Alter. 
- Von der Mitte ausgehend nach links ist die Anzahl Männer abgebildet, nach rechts die Anzahl Frauen. 
- Jeder Balken ist unterteilt in deutsche und nichtdeutsche Staatsangehörigkeit. Diese beiden Zahlen müssen addiert werden um die gesamte Bevölkerung pro Alter und Geschlecht abzubilden.
- In der Einwohnerstatistik erfolgt bei Geschlecht eine Merkmalsaggregation auf die beiden Ausprägungen „weiblich“ und „männlich“. Personen mit der Angabe „divers“ oder „ohne Angabe“ werden aus Geheimhaltungsgründen auf Basis des Geburtsdatums einer der beiden Ausprägungen zugeordnet.
