---
title: Luftwerte
source: Landesanstalt für Umwelt Baden-Württemberg (LUBW)
order: 6
columns:
- name: jahr
  type: int
  description: Jahr
  short: Luftschadstoffe gemessen in der Konstanzer Luftmessstation seit 2000
  export_id: Jahr der Erhebung
- name: no2
  type: float
  description: Stickstoffdioxid NO2 (Jahresmittelwert)
  unit: µg pro m³
  short: Stickstoffdioxid  NO2 ( JMW µg/m³)
  export_id: Stickstoffdioxid NO2
- name: o3
  type: float
  description: Ozon O3 (Jahresmittelwert)
  unit: µg pro m³
  short: Ozon O3 (JMW µg/m³)
  export_id: Ozon O3 (Jahresmittelwert)
- name: pm10_jahresmittel
  type: float
  description: Feinstaub PM10 (Jahresmittelwert)
  unit: µg pro m³
  short: Jahresmittelwert  (JMW µg/m³)
  export_id: Feinstaub PM10 Jahresmittelwert
- name: pm10_maxtagesmittel
  type: Optional[float]
  description: Feinstaub PM10 (max. Tagesmittelwert)
  unit: µg pro m³
  short: max. Tagesmittelwert
  export_id: Feinstaub PM10 max. Tagesmittelwert
- name: ueberschreitungen
  type: int
  description: Anzahl Tage mit Feinstaub PM10 (Tagesmittelwert) >50 µg pro m³ pro Tag seit 2000
  unit: Tage
  short: Tagesmittelwert >50 µg/m³ pro Tag (Anzahl Tage)
  export_id: 'Feinstaub PM10 Tagesmittelwert >50 µg/m³ pro Tag'
---
Anmerkungen: Die Landesanstalt für Umwelt Baden-Württemberg (LUBW) betreibt in Konstanz eine Luftmessstation. Erfasst werden die Luftschadstoffe Stickstoffdioxid (NO2), Ozon (O3) und Feinstaub (PM 10). Die aktuellen Luftmesswerte sowie Jahresstatistiken stehen auf den Internet-Seiten der LUBW zur Verfügung.

- JMV: Jahresmittelwert
- Feinstaub PM 10: Particulate Matter (PM) bezeichnet inhalierbare Partikel mit einem Durchmesser von ≤ 10 µm, die gesundheitlich relevant sind.
- Grenzwert: In der Europäischen Union (EU) gibt es festgeschriebene Grenzwerte für verschiedene Luftschadstoffe, die in allen Mitgliedstaaten eingehalten werden müssen. Geplant ist ab 2030 deutlich niedrigere Grenzwerte anzusetzen.
