---
title: Abfall- und Wertstoffmenge je Einw. in kg
teaser: Text
source: Entsorgungsbetriebe Konstanz
columns:
- name: jahr
  type: int
  description: Jahr der Erhebung
  short: Jahr
- name: rest
  type: int
  description: Restmüll
  unit: kg pro Einwohner
- name: bio
  type: int
  description: Biomüll
  unit: kg pro Einwohner
- name: glas
  type: Optional[int]
  description: Glas
  unit: kg pro Einwohner
- name: papier
  type: int
  description: Papier
  unit: kg pro Einwohner
- name: gruen
  type: int
  description: Grünabfall
  unit: kg pro Einwohner
- name: gelb
  type: int
  description: Gelber Sack
  unit: kg pro Einwohner
- name: sperr
  type: Optional[int]
  description: Sperrmüll
  unit: kg pro Einwohner
- name: sonstige
  type: Optional[int]
  description: sonstige Wertstoffe (Holz, Metall, E-Schrott)
  unit: kg pro Einwohner
---
Anmerkungen:

Einwohner: amtliche Einwohnerzahl des Vorjahres (Quelle: Statistisches Landesamt Baden-Württemberg)
Restmüll: Abfälle aus Haushalten sowie aus „Nichthaushalten“, da Restabfälle von Kleingewerbe und anderen Herkunftsbereichen (z. B. aus dem Tourismusbereich) zusammen mit häuslichem Restmüll erfasst wird. 
Biomüll: Bioabfälle sind biologisch abbaubare Abfälle aus Haushalten. Dazu gehören beispielsweise Essensreste, Obst- und Gemüsereste aber auch Gartenabfälle wie beispielsweise Rasenschnitt und Laub.
Glas: Altglas bzw. Verpackungsglas, wie Einwegflaschen, Konservengläser und Glasflakons, die in den Sammelcontainer für Altglas nach Farbe getrennt gesammelt werden.
Papier: Altpapier wie Papier, Pappe, Kartonagen
Grünabfall: Grünabfälle aus dem Garten wie geschnittene Äste und Zweige, Strauch- und Heckenschnitt, Laub, Weihnachtsbäume. Größere Schwankungen sind bei den Grünabfällen nicht ungewöhnlich, da die Grünabfallmenge sehr stark von der Witterung in der Vegetationszeit abhängig ist. 
Gelber Sack: Verkaufsverpackungen aus Kunststoff, Aluminium, Weißblech und Verbundmaterialien.
Sperrmüll: sperrige Einrichtungs- und Gebrauchsgegenstände, die aufgrund ihrer Größe nicht in die Restmüllbehälter passen und auf den Wertstoffhöfen entsorgt werden.
Sonstige Wertstoffe: Holz, Metalle, Elektroaltgeräte, mineralische Stoffe, Hartkunststoffe sowie Flachglas, die auf den Wertstoffhöfen getrennt gesammelt werden.
