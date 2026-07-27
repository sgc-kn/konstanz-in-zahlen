---
title: Fähre
source: Stadtwerke Konstanz
columns:
- name: jahr
  type: int
  description: Jahr
  short: Beförderungen der Fährschiffe der Stadtwerke Konstanz seit 2000
  export_id: Jahr
- name: schiffe
  type: Optional[int]
  description: Anzahl der Fährschiffe seit 2000
  unit: Anzahl Fährschiffe
  export_id: Fährschiffe
- name: personen
  type: Optional[float]
  description: Beförderte Personen
  unit: Anzahl (Mio.)
  short: Personen (in Mio.)
  export_id: beförderte Personen
- name: fahrzeuge
  type: Optional[float]
  description: Beförderte PKW und Nutzfahrzeuge
  unit: Anzahl (Mio.)
  short: Pkw und Nutzfahrzeuge (in Mio.)
  export_id: beförderte PKW und Nutzfahrzeuge
- name: zweirad
  type: Optional[float]
  description: Motor- und Fahrräder
  unit: Anzahl (Mio.)
  short: Motor- und Fahrräder (in Mio.)
  export_id: Motor- und Fahrräder
---
Anmerkungen: Weitere Informationen finden Sie unter: https://www.stadtwerke-konstanz.de/faehre/infos/ .

- 2001, 2002: 1 Reserveschiff
- Ab Juni 2008 Methodenwechsel bei statistischer Erfassung
