import pandas
from pathlib import Path
from .dataset import Dataset
from .table import validate_data_and_create_table
from . import model


def save(dataset: Dataset, *, path: Path) -> None:
    # TODO / nice to have: put pydantic field descriptions onto excel column headers
    # or do a three level header: column name, python type, description
    # this would allow edit/provide the model in excel

    if path.suffix != ".xlsx":
        raise ValueError(f"invalid suffix on path (should be .xlsx): {path}")

    with pandas.ExcelWriter(path) as writer:
        for name, table in dataset.tables.items():
            df = pandas.DataFrame([instance.dict() for instance in table.data])
            df.to_excel(writer, sheet_name=name, index=False)


def load(path: Path, models_path: Path) -> Dataset:
    dataset = dict()
    excel_file = pandas.ExcelFile(path)
    for name in excel_file.sheet_names:
        schema_path = (models_path / str(name)).with_suffix(".md")
        schema = model.load(schema_path)

        df = pandas.read_excel(path, sheet_name=name)
        rows = df.to_dict(orient="records")

        table = validate_data_and_create_table(rows, schema, ignore_extra=True)
        dataset[name] = table

    return Dataset(tables=dataset)
