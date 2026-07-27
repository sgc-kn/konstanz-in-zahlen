---
title: Betriebe / Niederlassungen nach Größe (Unternehmensregister)
source: Statistisches Landesamt Baden-Württemberg (Unternehmensregister)
order: 2
columns:
- name: jahr
  type: int
  description: Jahr
  short: Betriebe/Niederlassungen nach Betriebsgröße seit 2008
  export_id: Jahr der Erhebung
- name: bis9
  type: Optional[int]
  description: 0 – 9 Beschäftigte
  unit: Anzahl
  export_id: 0 – 9 sozialversicherungspfl. Beschäftigte
- name: bis49
  type: Optional[int]
  description: 10 – 49 Beschäftigte
  unit: Anzahl
  export_id: 10 – 49 sozialversicherungspfl. Beschäftigte
- name: bis249
  type: Optional[int]
  description: 50 – 249 Beschäftigte
  unit: Anzahl
  export_id: 50 – 249 sozialversicherungspfl. Beschäftigte
- name: ueber250
  type: Optional[int]
  description: 250 und mehr Beschäftigte
  unit: Anzahl
  export_id: 250 und mehr sozialversicherungspfl. Beschäftigte
---
Anmerkungen: Das statistische Unternehmensregister ist eine regelmäßig aktualisierte Datenbank mit Informationen zu Niederlassungen, Rechtlichen Einheiten, Unternehmen und Unternehmensgruppen aus allen Wirtschaftsbereichen mit Angaben zu Umsatz und/oder Beschäftigten. Ausgenommen sind jedoch unter anderem die Abschnitte „Land- und Forstwirtschaft, Fischerei“ und „Öffentliche Verwaltung, Verteidigung, Sozialversicherung“, der WZ 2008.

- Einbezogen in das statistische Unternehmensregister werden Niederlassungen und rechtliche Einheiten, die einen bestimmten Relevanz-Schwelle überschreiten (mind. 1 sv Beschäftigten, Höhe Umsatz).
- Eine Niederlassung (bis 2017: „Betriebe“) ist eine örtlich abgegrenzte Einheit, die einer Rechtlichen Einheit zugeordnet ist.
- Größe der Niederlassungen nach Zahl der sozialversicherungspflichtig Beschäftigten. Die Anzahl der Beschäftigten wird als Durchschnittswert dargestellt.

Beginnend mit dem Berichtsjahr 2024 stellt das Unternehmensregister die einzelnen Beschäftigtenmerkmale auf das sogenannte Jobkonzept um. Der Vergleich von Einheiten und Beschäftigtenwerten mit dem Vorjahr ist daher nicht sinnvoll.
Weitere Informationen unter https://www.destatis.de/DE/Themen/Branchen-Unternehmen/Unternehmen/Unternehmensregister/_inhalt.html .
