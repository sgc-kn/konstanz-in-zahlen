---
title: Verkehrsnetz
source: Stadt Konstanz, Tiefbauamt; Stadt Konstanz, Amt für Stadtplanung und Umwelt
columns:
- name: jahr
  type: int
  description: Jahr
  short: Verkehrsnetzentwicklung der Stadt Konstanz seit 2000
  export_id: Jahr der Erhebung
- name: strasse
  type: int
  description: Straßennetz
  unit: km
  export_id: Straßennetz
- name: fahrrad
  type: Optional[float]
  description: Radverkehrsinfrastruktur (ohne Tempo-30-Zonen)
  unit: km
  export_id: Radverkehrsinfrastruktur (ohne Tempo-30-Zonen)
---
Anmerkungen:
Beim Straßennetz handelt es sich um alle öffentlichen Straßen im Stadtgebiet, unabhängig von Träger oder Eigentümer. Privatstraßen sind nicht erfasst.

- Bei der Radverkehrsinfrastruktur werden zwischen 2007 und 2015 die Tempo-30-Zonen miteingerechnet. Andere große Veränderungen innerhalb der Daten lassen sich durch Methodenwechsel erklären.
