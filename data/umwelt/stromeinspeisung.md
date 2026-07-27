---
title: Stromeinspeisung aus erneurbaren Energien sowie aus Blockheizkraftwerken
source: Stadtwerke Konstanz
order: 8
columns:
- name: jahr
  type: int
  description: Jahr
  short: "Stadtwerke Konstanz: Stromeinspeisung aus erneuerbaren Energien und Blockheizkraftwerken seit 2003"
  export_id: Jahr
- name: insgesamt
  type: float
  description: Stadtwerke Insgesamt
  unit: Mio. kWh
  export_id: Stadtwerke Insgesamt
- name: deponie
  type: Optional[float]
  description: Deponie (beendet 31.12.2020; Energienutzungsgrad = 30-40%)
  unit: Mio. kWh
  export_id: Deponie (beendet 31.12.2020)
- name: photovoltaik
  type: float
  description: Photovoltaik (Energienutzungsgrad = 12–18%)
  unit: Mio. kWh
  export_id: Photovoltaik
- name: bhkw
  type: float
  description: BHKW (Energienutzungsgrad = 80-90%)
  unit: Mio. kWh
  export_id: BHKW (mit einem Energienutzungsgrad von 80-90%)
---
Anmerkungen: Die Stadtwerke Konstanz (SWK) sind wichtiger Strom- und Gasversorger für die Konstanzer Bevölkerung. 
Der Energienutzungsgrad gibt an, wie viel der zugeführten Energie tatsächlich genutzt wird, um eine bestimmte Leistung zu erbringen. Ein hoher Energie-Nutzungsgrad bedeutet, dass ein großer Teil der eingesetzten Energie in nutzbare Energie (wie Wärme oder Strom) umgewandelt wird, während nur ein kleiner Teil als Verlust (z.B. in Form von Abwärme) verloren geht.
2011 fand bei der Deponie eine Direktvermarktung an die Stadtwerke Tübingen statt, deshalb liegen für dieses Jahr keine Daten vor.
