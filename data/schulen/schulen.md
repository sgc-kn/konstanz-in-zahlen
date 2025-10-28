---
title: Allgemeinbildende Schulen (städtische Schulen)
source: Stadt Konstanz, Amt für Bildung und Sport
columns:
- name: jahr
  type: str
  description: Schuljahr
- name: grund_schulen
  type: int
  description: 'Grundschulen: Schulen'
  short: 'Grundschulen: Schulen'
- name: grund
  type: int
  description: 'Grundschulen: SchülerInnen'
  short: 'Grundschulen: SchülerInnen'
- name: hauptwerkreal_schulen
  type: int
  description: 'Haupt-/Werkrealschulen: Schulen'
  short: 'Haupt-/Werkrealschulen: Schulen'
- name: hauptwerkreal
  type: int
  description: 'Haupt-/Werkrealschulen: SchülerInnen'
  short: 'Haupt-/Werkrealschulen: SchülerInnen'
- name: real_schulen
  type: int
  description: 'Realschulen: Schulen'
  short: 'Realschulen: Schulen'
- name: real
  type: int
  description: 'Realschulen: SchülerInnen'
  short: 'Realschulen: SchülerInnen'
- name: gemeinschaft_schulen
  type: int
  description: 'Gemeinschaftsschulen: Schulen'
  short: 'Gemeinschaftsschulen: Schulen'
- name: gemeinschaft
  type: int
  description: 'Gemeinschaftsschulen: SchülerInnen'
  short: 'Gemeinschaftsschulen: SchülerInnen'
- name: gymnasien_schulen
  type: int
  description: 'Gymnasien: Schulen'
  short: 'Gymnasien: Schulen'
- name: gymnasien
  type: int
  description: 'Gymnasien: SchülerInnen'
  short: 'Gymnasien: SchülerInnen'
- name: sonderpaedagogisch_schulen
  type: int
  description: 'Sonderpädagogische Bildungs- und Beratungszentren: Schulen'
  short: 'Sonderpädagogische Bildungs- und Beratungszentren: Schulen'
- name: sonderpaedagogisch
  type: int
  description: 'Sonderpädagogische Bildungs- und Beratungszentren: SchülerInnen'
  short: 'Sonderpädagogische Bildungs- und Beratungszentren: SchülerInnen'
- name: insgesamt_schulen
  type: int
  computed: self.grund_schulen + self.hauptwerkreal_schulen + self.real_schulen + self.gemeinschaft_schulen + self.gymnasien_schulen + self.sonderpaedagogisch_schulen
  description: 'insgesamt: Schulen'
- name: insgesamt
  type: int
  computed: self.grund + self.hauptwerkreal + self.real + self.gemeinschaft + self.gymnasien + self.sonderpaedagogisch
  description: 'insgesamt: SchülerInnen'
---
Anmerkungen: Die Stadt Konstanz als Schulträger ist für die Errichtung, Unterhaltung und Verwaltung der allgemeinbildenden städtischen Schule verantwortlich. Die SchülerInnen kommen im Wesentlichen aus der Stadt Konstanz. Nur ein geringer Anteil (ca 12%) kommt von außerhalb.


