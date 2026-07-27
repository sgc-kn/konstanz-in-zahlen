---
title: Allgemeinbildende Schulen (städtische Schulen)
source: Stadt Konstanz, Amt für Bildung und Sport
columns:
- name: jahr
  type: str
  description: Schuljahr
  short: Allgemeinbildende städtische Schulen und ihre SchülerInnen seit 2000
  export_id: Schuljahr
- name: grund_schulen
  type: int
  description: Grundschulen
  unit: Anzahl Schulen
  export_id: 'Grundschulen: Schulen'
- name: grund
  type: int
  description: Grundschulen
  unit: Anzahl SchülerInnen
  export_id: 'Grundschulen: SchülerInnen'
- name: hauptwerkreal_schulen
  type: int
  description: Haupt-/Werkrealschulen
  unit: Anzahl Schulen
  export_id: 'Haupt-/Werkrealschulen: Schulen'
- name: hauptwerkreal
  type: int
  description: Haupt-/Werkrealschulen
  unit: Anzahl SchülerInnen
  export_id: 'Haupt-/Werkrealschulen: SchülerInnen'
- name: real_schulen
  type: int
  description: Realschulen
  unit: Anzahl Schulen
  export_id: 'Realschulen: Schulen'
- name: real
  type: int
  description: Realschulen
  unit: Anzahl SchülerInnen
  export_id: 'Realschulen: SchülerInnen'
- name: gemeinschaft_schulen
  type: int
  description: Gemeinschaftsschulen
  unit: Anzahl Schulen
  export_id: 'Gemeinschaftsschulen: Schulen'
- name: gemeinschaft
  type: int
  description: Gemeinschaftsschulen
  unit: Anzahl SchülerInnen
  export_id: 'Gemeinschaftsschulen: SchülerInnen'
- name: gymnasien_schulen
  type: int
  description: Gymnasien
  unit: Anzahl Schulen
  export_id: 'Gymnasien: Schulen'
- name: gymnasien
  type: int
  description: Gymnasien
  unit: Anzahl SchülerInnen
  export_id: 'Gymnasien: SchülerInnen'
- name: sonderpaedagogisch_schulen
  type: int
  description: Sonderpädagogische Bildungs- und Beratungszentren
  unit: Anzahl Schulen
  export_id: 'Sonderpädagogische Bildungs- und Beratungszentren: Schulen'
- name: sonderpaedagogisch
  type: int
  description: Sonderpädagogische Bildungs- und Beratungszentren
  unit: Anzahl SchülerInnen
  export_id: 'Sonderpädagogische Bildungs- und Beratungszentren: SchülerInnen'
- name: insgesamt_schulen
  type: int
  description: Insgesamt
  unit: Anzahl Schulen
  computed: grund_schulen + hauptwerkreal_schulen + real_schulen + gemeinschaft_schulen + gymnasien_schulen + sonderpaedagogisch_schulen
- name: insgesamt
  type: int
  description: Insgesamt
  unit: Anzahl SchülerInnen
  computed: grund + hauptwerkreal + real + gemeinschaft + gymnasien + sonderpaedagogisch
---
Anmerkungen: Die Stadt Konstanz als Schulträger ist für die Errichtung, Unterhaltung und Verwaltung der allgemeinbildenden städtischen Schule verantwortlich.
