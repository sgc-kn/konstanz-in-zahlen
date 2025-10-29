from pathlib import Path
from pydantic import BaseModel, model_validator
from typing import List, Optional, Self
import io
import jinja2
import re
import ruamel.yaml


class ColumnSchema(BaseModel):
    name: str  # python field name, CSV header
    type: str  # literal python code (type hint)
    description: str  # human readable description
    unit: Optional[str] = None
    short: Optional[str] = None  # short description, used as column title
    computed: Optional[str] = None  # literal python code (expression)

    @model_validator(mode="after")
    def no_redunant_short(self) -> Self:
        if self.short is not None and self.short == self.description:
            raise ValueError(
                f"short description and description of column {self.name} are the same. Please remove the short description."
            )
        return self


yaml = ruamel.yaml.YAML()
yaml.default_flow_style = False
yaml.width = 9999

j2_dir = Path(__file__).parent
j2_loader = jinja2.FileSystemLoader(str(j2_dir))
j2_env = jinja2.Environment(loader=j2_loader, keep_trailing_newline=True)
j2_template = j2_env.get_template("table_schema.py.j2")


class TableSchema(BaseModel):
    title: str
    source: Optional[str] = None
    columns: List[ColumnSchema]
    description: Optional[str] = None

    @classmethod
    def from_markdown_file(cls, file_path: Path) -> "TableSchema":
        with open(file_path, "r", encoding="utf-8") as f:
            text = f.read()

        m = re.match(r"\A---\s*\n(.*?\n)---\s*\n(.*)\Z", text, flags=re.DOTALL)
        if not m:
            data = dict(description=text)
        else:
            data = yaml.load(io.StringIO(m.group(1)))
            data["description"] = m.group(2).strip()

        return cls.model_validate(data)

    def to_markdown_file(self, file_path: Path) -> None:
        file_path = file_path.with_suffix(".md")
        data = self.model_dump(exclude_none=True)
        body = data.pop("description", None)
        with open(file_path, "w", encoding="utf-8") as f:
            print("---", file=f)
            yaml.dump(data, f)
            print("---", file=f)
            if body:
                print(body, file=f)

    def to_python_file(self, file_path: Path) -> None:
        imports = []

        if self.description and self.source:
            # TODO German language leak ahead:
            table_description = self.description + "\n\nQuelle: " + self.source
        elif self.description:
            table_description = self.description
        elif self.source:
            table_description = "Quelle: " + self.source
        else:
            table_description = None

        for c in self.columns:
            if c.computed:
                imports.append("from pydantic import computed_field")
                break

        for c in self.columns:
            if c.type.startswith("Optional["):
                imports.append("from typing import Optional")
                break

        def field_info(col: ColumnSchema) -> str:
            kwargs: dict[str, str] = dict()

            if col.short is not None:
                kwargs["title"] = col.short

            kwargs["description"] = col.description

            if col.unit is not None:
                kwargs["description"] += ", Einheit: " + col.unit

            return ", ".join([f"{k} = {repr(v)}" for k, v in kwargs.items()])

        imports = sorted(imports)

        text = j2_template.render(
            table=self,
            table_description=table_description,
            imports=imports,
            field_info=field_info,
        )
        file_path = file_path.with_suffix(".py")
        file_path.write_text(text, encoding="utf-8")

    def get_column(self, name: str) -> Optional[ColumnSchema]:
        for column in self.columns:
            if column.name == name:
                return column
        return None
