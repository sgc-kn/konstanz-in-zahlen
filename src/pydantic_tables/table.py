import numpy
import pandas
from dataclasses import dataclass
from pydantic import BaseModel
from typing import List, Type, Dict
from .schema import TableSchema, ColumnSchema


@dataclass(frozen=True)
class MetaTable:
    schema: TableSchema
    model: Type[BaseModel]

    @property
    def field_names(self) -> list[str]:
        return list(self.model.model_fields.keys())

    def field_meta(self, field_name: str) -> ColumnSchema | None:
        return self.schema.get_column(field_name)


@dataclass(frozen=True)
class Table(MetaTable):
    data: List[BaseModel]

    @property
    def field_names(self) -> list[str]:
        return super().field_names

    def to_pandas(self):
        """Convert table to Pandas DataFrame"""
        return pandas.DataFrame([r.model_dump() for r in self.data])


def validate_data_and_create_table(
    rows: List[Dict], meta: MetaTable, *, ignore_extra: bool = False
) -> Table:
    """Create table from list of dictionaries. Validates input data."""
    data = []
    for row in rows:
        for key, val in row.items():
            if val == "" or (isinstance(val, float) and numpy.isnan(val)):
                row[key] = None

            if not ignore_extra and key not in meta.model.model_fields:
                raise ValueError(f"extra column {key} in data")

        instance = meta.model.model_validate(row)
        data.append(instance)

    return Table(schema=meta.schema, model=meta.model, data=data)
