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
- name: grund
  type: int
  description: 'Grundschulen: SchülerInnen'
- name: hauptwerkreal_schulen
  type: int
  description: 'Haupt-/Werkrealschulen: Schulen'
- name: hauptwerkreal
  type: int
  description: 'Haupt-/Werkrealschulen: SchülerInnen'
- name: real_schulen
  type: int
  description: 'Realschulen: Schulen'
- name: real
  type: int
  description: 'Realschulen: SchülerInnen'
- name: gemeinschaft_schulen
  type: int
  description: 'Gemeinschaftsschulen: Schulen'
- name: gemeinschaft
  type: int
  description: 'Gemeinschaftsschulen: SchülerInnen'
- name: gymnasien_schulen
  type: int
  description: 'Gymnasien: Schulen'
- name: gymnasien
  type: int
  description: 'Gymnasien: SchülerInnen'
- name: sonderpaedagogisch_schulen
  type: int
  description: 'Sonderpädagogische Bildungs- und Beratungszentren: Schulen'
- name: sonderpaedagogisch
  type: int
  description: 'Sonderpädagogische Bildungs- und Beratungszentren: SchülerInnen'
- name: insgesamt_schulen
  type: int
  description: 'insgesamt: Schulen'
  computed: self.grund_schulen + self.hauptwerkreal_schulen + self.real_schulen + self.gemeinschaft_schulen + self.gymnasien_schulen + self.sonderpaedagogisch_schulen
- name: insgesamt
  type: int
  description: 'insgesamt: SchülerInnen'
  computed: self.grund + self.hauptwerkreal + self.real + self.gemeinschaft + self.gymnasien + self.sonderpaedagogisch
---
Anmerkungen: Die Stadt Konstanz als Schulträger ist für die Errichtung, Unterhaltung und Verwaltung der allgemeinbildenden städtischen Schule verantwortlich. Die SchülerInnen kommen im Wesentlichen aus der Stadt Konstanz. Nur ein geringer Anteil (ca 12%) kommt von außerhalb.
