from dataclasses import dataclass
from pathlib import Path
from typing import Dict
from . import csv, model
from .table import MetaTable, Table

# TODO maybe enforce some rules on the table names (e.g. snake case, alnum + underscore)
# table names must be valid excel sheet and file names


@dataclass(frozen=True)
class Dataset:
    """A dataset containing multiple tables of validated Pydantic model instances."""

    tables: Dict[str, Table]


def load_meta(path: Path) -> Dict[str, MetaTable]:
    csv_files = list(path.glob("*.csv"))

    tables = dict()
    for csv_path in csv_files:
        name = csv_path.stem  # w/o path and extension

        model_path = (path / name).with_suffix(".md")

        tables[name] = model.load(model_path)

    return tables


def load(path: Path) -> Dataset:
    meta = load_meta(path)

    tables = dict()
    for name, x in meta.items():
        csv_path = (path / name).with_suffix(".csv")
        tables[name] = csv.load_and_validate(csv_path, x)

    return Dataset(tables=tables)


def save(dataset: Dataset, path: Path) -> None:
    for name, table in dataset.tables.items():
        csv_path = path / f"{name}.csv"
        csv.save(table, path=csv_path)


def load_readme(path: Path) -> str:
    readme_path = path / "README.md"

    if not readme_path.is_file():
        raise FileNotFoundError(f"Missing README.md for dataset: {readme_path}")

    with open(readme_path, "r") as f:
        content = f.read()

    return content.strip()
