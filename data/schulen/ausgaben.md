---
title: Ausgaben für Schulen
source: Stadt Konstanz, Kämmerei
columns:
- name: jahr
  type: int
  description: Jahr
  short: Städtischer Haushalt für Schulen seit 2001
  export_id: Jahr
- name: haushalt_mio
  type: float
  description: Ergebnishaushalt
  unit: Mio. €
  short: 'Ergebnishaushalt: in Mio. €'
  export_id: Ergebnishaushalt in Mio. €
- name: haushalt_proschueler
  type: int
  description: Ergebnishaushalt
  unit: € pro SchülerIn
  short: 'Ergebnishaushalt: pro SchülerIn'
  export_id: Ergebnishaushalt pro SchülerIn
- name: investitionen_mio
  type: float
  description: Investitionen
  unit: Mio. €
  short: 'Investitionen: in Mio. €'
  export_id: Investitionen in Mio. €
- name: investitionen_proschueler
  type: int
  description: Investitionen
  unit: € pro SchülerIn
  short: 'Investitionen: pro SchülerIn'
  export_id: Investitionen pro SchülerIn
- name: mio_insgesamt
  type: float
  description: Insgesamt
  unit: Mio. €
  computed: haushalt_mio + investitionen_mio
  export_id: 'insgesamt: in Mio €'
- name: proschueler_insgesamt
  type: int
  description: Insgesamt
  unit: € pro SchülerIn
  computed: haushalt_proschueler + investitionen_proschueler
  export_id: 'insgesamt: pro SchülerIn'
- name: bedarf
  type: Optional[int]
  description: Nettoressourcenbedarf Schulen
  unit: € pro SchülerIn
  export_id: Nettoressourcenbedarf Schulen (pro SchülerIn) in €
---
Anmerkungen: Die Stadt Konstanz als Schulträger ist für Errichtung, Unterhaltung und Verwaltung der allgemeinbildenden städtischen Schule verantwortlich und trägt in der Regel die Sachkosten. Dies umfasst die Kosten u.a. für Gebäude, technische Ausstattung, sowie die Personalkosten für Sekretariat und Hausmeister (während die Personalkosten für Lehrer an öffentlichen Schulen vom Land übernommen werden). Der Ergebnishaushalt umfasst die Aufwendungen und Erträge im Haushaltsjahr.
