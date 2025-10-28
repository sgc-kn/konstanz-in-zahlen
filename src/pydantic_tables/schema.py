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
    description: Optional[str] = None  # TODO make obligatory
    unit: Optional[str] = None
    short: Optional[str] = None
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

        for c in self.columns:
            if c.computed:
                imports.append("from pydantic import computed_field")
                break

        for c in self.columns:
            if c.type.startswith("Optional["):
                imports.append("from typing import Optional")
                break

        tab_data = self.model_dump(exclude_none=True)
        tab_data.pop("columns", None)
        tab_data.pop("description", None)
        tab_data.pop("title", None)
        if tab_data:
            tab_yaml = io.StringIO()
            yaml.dump(tab_data, tab_yaml)
            tab_yaml = tab_yaml.getvalue()
        else:
            tab_yaml = None

        columns = []
        for c in self.columns:
            col_data = c.model_dump(exclude_none=True)
            col_data.pop("computed", None)
            col_data.pop("description")
            col_data.pop("name")
            col_data.pop("type")
            if col_data:
                col_yaml = io.StringIO()
                yaml.dump(col_data, col_yaml)
                col_yaml = col_yaml.getvalue()
            else:
                col_yaml = None
            columns.append((c, col_yaml))

        imports = sorted(imports)

        text = j2_template.render(
            table=self,
            table_yaml=tab_yaml,
            imports=imports,
            columns=columns,
        )
        file_path = file_path.with_suffix(".py")
        file_path.write_text(text, encoding="utf-8")

    def get_column(self, name: str) -> Optional[ColumnSchema]:
        for column in self.columns:
            if column.name == name:
                return column
        return None
