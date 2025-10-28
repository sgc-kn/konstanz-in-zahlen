---
title: Ausgaben für Schulen
source: Stadt Konstanz, Kämmerei
columns:
- name: jahr
  type: int
  description: Jahr
- name: haushalt_mio
  type: float
  description: Ergebnishaushalt in Mio. €
  unit: Mio. €
  short: 'Ergebnishaushalt: in Mio. €'
- name: haushalt_proschueler
  type: int
  description: Ergebnishaushalt pro SchülerIn
  unit: €
  short: 'Ergebnishaushalt: pro SchülerIn'
- name: investitionen_mio
  type: float
  description: Investitionen in Mio. €
  unit: Mio. €
  short: 'Investitionen: in Mio. €'
- name: investitionen_proschueler
  type: int
  description: Investitionen pro SchülerIn
  unit: €
  short: 'Investitionen: pro SchülerIn'
- name: mio_insgesamt
  type: float
  description: 'insgesamt: in Mio €'
  unit: Mio. €
  computed: self.haushalt_mio + self.investitionen_mio
- name: proschueler_insgesamt
  type: int
  description: 'insgesamt: pro SchülerIn'
  unit: €
  computed: self.haushalt_proschueler + self.investitionen_proschueler
- name: bedarf
  type: Optional[int]
  description: Nettoressourcenbedarf Schulen (pro SchülerIn) in €
  unit: €
---
Anmerkungen: Die Stadt Konstanz als Schulträger ist für Errichtung, Unterhaltung und Verwaltung der allgemeinbildenden städtischen Schule verantwortlich und trägt in der Regel die Sachkosten. Dies umfasst die Kosten u.a. für Gebäude, technische Ausstattung u.v.m. sowie die Personalkosten für Sekretariat und Hausmeister (während die Personalkosten für Lehrer an öffentlichen Schulen vom Land übernommen werden). Der Ergebnishaushalt umfasst die Aufwendungen und Erträge im Haushaltsjahr.
