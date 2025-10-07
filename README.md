# Konstanz in Zahlen

[German abstract; English version below]

Dieses Repository enthält jährliche Statistiken über die Stadt Konstanz. Diese
Statistiken werden seit 20 Jahren als Heft gepflegt und veröffentlicht. 
Aktuelle und historische PDF-Veröffentlichungen sind auf der Stadtwebsite
verfügbar: https://www.konstanz.de/leben+in+konstanz/statistik/

Die Daten befinden sich im `data` Verzeichnis und sind nach Kategorie in mehreren
Unterverzeichnissen organisiert. Die einzelnen Tabellen liegen als CSV-Dateien
vor und folgen dem Namensschema `data/<kategorie>/<tabelle>.csv`. Die Metadaten
zu den einzelnen Tabellen liegen direkt daneben (`data/<kategorie>/<tabelle>.md`).

## What is this about?

This repository holds yearly statistics about the City of Constance. These
statistics are maintained and published as booklet since 20 years.
Recent and historic PDF publications are available on the city website:
https://www.konstanz.de/leben+in+konstanz/statistik/

We keep the data in CSV files, one file per table. Each table has its
schema defined in a Markdown file with Yaml Header. We automatically
generate Pydantic models from this schema and validate the data against
the schema.

We strive to:
- make the data machine readable (CSV files)
- avoid unnecessary inconsistencies (strict schema validation)
- be transparent about how the dataset evolves over time (version control)

Data lives in the `data` directory and is organized in datasets, each
holding multiple tables (`data/<dataset>/<table>.csv)`). The schema is
stored right next to the respective table (`data/<dataset>/<table>.md`).
The Pydantic models are written to (`data/<dataset>/<table>.py`).

To edit the data, start a Github Codespace. All dependencies will be
installed automatically. (Please create an issue if not!) Propose your
changes as Github Pull Request.

You can export and import data to and from Excel using `pytab export
/data/<dataset>` and `pytab import data/<dataset>`. The default location
for the Excel file is `pytab import data/<dataset>/<dataset>.xlsx`, but
you can overwrite this with the `--input` and `--output` parameters.

We are implementing Pytest-based tests in the `test` directory.
Additionally, Shell-based tests are defined in the `justfile`. Run all
tests locally with `just ci`. Some problems can be fixed automatically
with `just fix`.

In `src/pydantic_tables` we develop a library, Pydantic Tables, to apply
this kind of data management to other datasets.

## License

We release our code under the EUPL-1.2 license. See the LICENSE file
for details. Contributions to this project are licensed under the same
terms.

We release the data to the public domain using the Creative Commons
Zero (CC0) license version 1.0. The license terms are available online:
https://creativecommons.org/publicdomain/zero/1.0/
