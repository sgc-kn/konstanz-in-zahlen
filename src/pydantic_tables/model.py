import importlib.util
import pydantic

from pathlib import Path
from .table import MetaTable
from .schema import TableSchema


class ModelLoadError(Exception):
    """Raised when a model cannot be loaded from a Python file."""

    pass


def load(path: Path) -> MetaTable:
    """Load a Pydantic model from its schema file.

    Raises:
        ModelLoadError: If the file cannot be loaded, doesn't have a Model,
                       or Model is not a BaseModel subclass.
    """

    if path.suffix != ".md":
        raise ValueError(f'Model path must end in ".md": {path}')

    # Dynamically build Python module with Pydantic BaseModel:
    schema = TableSchema.from_markdown_file(path)
    path = path.with_suffix(".py")
    schema.to_python_file(path)

    try:
        spec = importlib.util.spec_from_file_location(path.stem, path)
        if spec is None or spec.loader is None:
            raise ModelLoadError(f"Cannot create module spec for {path}")

        module = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(module)

    except Exception as e:
        raise ModelLoadError(f"Error loading module from {path}: {e}") from e

    if not hasattr(module, "Table"):
        raise ModelLoadError(f"Module {path} does not have a 'Table' attribute")

    model_class = module.Table

    if not isinstance(model_class, type):
        raise ModelLoadError(f"'Table' in {path} is not a class")

    if not issubclass(model_class, pydantic.BaseModel):
        raise ModelLoadError(f"'Table' in {path} is not a Pydantic BaseModel subclass")

    return MetaTable(model=model_class, schema=schema)
