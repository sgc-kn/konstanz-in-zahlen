---
title: Abfall- und Wertstoffmenge je Einw. in kg
source: Entsorgungsbetriebe Konstanz
order: 1
columns:
- name: jahr
  type: int
  description: Jahr
  short: Abfall- und Wertstoffmenge pro Einwohner seit 2001
  export_id: Jahr der Erhebung
- name: rest
  type: int
  description: Restmüll
  unit: kg pro Einwohner
  export_id: Restmüll
- name: bio
  type: int
  description: Biomüll
  unit: kg pro Einwohner
  export_id: Biomüll
- name: glas
  type: Optional[int]
  description: Glas
  unit: kg pro Einwohner
  export_id: Glas
- name: papier
  type: int
  description: Papier
  unit: kg pro Einwohner
  export_id: Papier
- name: gruen
  type: int
  description: Grünabfall
  unit: kg pro Einwohner
  export_id: Grünabfall
- name: gelb
  type: int
  description: Gelber Sack
  unit: kg pro Einwohner
  export_id: Gelber Sack
- name: sperr
  type: Optional[int]
  description: Sperrmüll
  unit: kg pro Einwohner
  export_id: Sperrmüll
- name: sonstige
  type: Optional[int]
  description: Sonstige Wertstoffe (Holz, Metall, E-Schrott)
  unit: kg pro Einwohner
  export_id: sonstige Wertstoffe (Holz, Metall, E-Schrott)
---
Anmerkungen: Weitere Informationen finden Sie unter: https://www.konstanz.de/entsorgungsbetriebe/start .

- Einwohner: amtliche Einwohnerzahl des Vorjahres (Quelle: Statistisches Landesamt Baden-Württemberg)
- Restmüll: Abfälle aus Haushalten sowie aus „Nichthaushalten“, da Restabfälle von Kleingewerbe und anderen Herkunftsbereichen (z. B. aus dem Tourismusbereich) zusammen mit häuslichem Restmüll erfasst wird. 
- Biomüll: Bioabfälle sind biologisch abbaubare Abfälle aus Haushalten. Dazu gehören beispielsweise Essensreste, Obst- und Gemüsereste aber auch Gartenabfälle wie beispielsweise Rasenschnitt und Laub.
- Glas: Altglas bzw. Verpackungsglas, wie Einwegflaschen, Konservengläser und Glasflakons, die in den Sammelcontainer für Altglas nach Farbe getrennt gesammelt werden.
- Papier: Altpapier wie Papier, Pappe, Kartonagen
- Grünabfall: Grünabfälle aus dem Garten wie geschnittene Äste und Zweige, Strauch- und Heckenschnitt, Laub, Weihnachtsbäume. Größere Schwankungen sind bei den Grünabfällen nicht ungewöhnlich, da die Grünabfallmenge sehr stark von der Witterung in der Vegetationszeit abhängig ist. 
- Gelber Sack: Verkaufsverpackungen aus Kunststoff, Aluminium, Weißblech und Verbundmaterialien.
- Sperrmüll: sperrige Einrichtungs- und Gebrauchsgegenstände, die aufgrund ihrer Größe nicht in die Restmüllbehälter passen und auf den Wertstoffhöfen entsorgt werden.
- Sonstige Wertstoffe: Holz, Metalle, Elektroaltgeräte, mineralische Stoffe, Hartkunststoffe sowie Flachglas, die auf den Wertstoffhöfen getrennt gesammelt werden.
