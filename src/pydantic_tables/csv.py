import csv
from csv import DictReader, DictWriter
from pathlib import Path
from typing import Dict, List
from .table import MetaTable, Table, validate_data_and_create_table

csv.register_dialect("pytab")  # set CSV format here, e.g. delimiter=";"


def save(table: Table, *, path: Path) -> None:
    csv_path = path.with_suffix(".csv")

    with open(csv_path, "w", newline="") as file:
        writer = DictWriter(
            file,
            fieldnames=table.model.model_fields,
            dialect="pytab",
            extrasaction="ignore",
        )
        writer.writeheader()
        for row in table.data:
            writer.writerow(row.model_dump())


def load_raw_data(path: Path) -> List[Dict]:
    with open(path, "r", newline="") as file:
        csv_reader = DictReader(file, dialect="pytab")
        rows = [row for row in csv_reader]

    return rows


def load_and_validate(path: Path, meta: MetaTable) -> Table:
    raw = load_raw_data(path)
    return validate_data_and_create_table(raw, meta)
