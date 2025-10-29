import importlib.util
import pydantic
import sys

from dataclasses import dataclass
from pathlib import Path
from types import ModuleType
from .table import MetaTable
from .schema import TableSchema


class ModelLoadError(Exception):
    """Raised when a model cannot be loaded from a Python file."""

    pass


@dataclass(frozen=True)
class ModelPath:
    path: Path

    def __post_init__(self):
        if self.path.suffix != ".md":
            raise ValueError(
                f'Model paths must end in ".md". The given path does not: {self.path}'
            )
        if len(self.path.parts) < 2:
            raise ValueError(
                f"Model must have at least two parts, the dataset and the table. The given path is too short: {self.path}"
            )


def module_name(model: ModelPath) -> str:
    return f"data.{model.path.parent.stem}.{model.path.stem}"


def module_path(model: ModelPath) -> Path:
    return model.path.with_suffix(".py")


def _load_module(model: ModelPath, schema: TableSchema) -> ModuleType:
    """Helper function for load function (below)"""

    # Dynamically build Python module with Pydantic BaseModel:
    path = module_path(model)

    try:
        spec = importlib.util.spec_from_file_location(module_name(model), path)
        if spec is None or spec.loader is None:
            raise ModelLoadError(f"Cannot create module spec for {path}")

        # avoid loading module twice
        if spec.name in sys.modules:
            return sys.modules[spec.name]

        schema.to_python_file(path)

        module = importlib.util.module_from_spec(spec)
        sys.modules[spec.name] = module  # required to avoid recursive imports

        try:
            spec.loader.exec_module(module)
        except BaseException:
            # deregister/uncache module if execution fails
            if sys.modules.get(spec.name) is module:
                del sys.modules[spec.name]
            raise

    except Exception as e:
        raise ModelLoadError(f"Error loading module from {path}: {e}") from e

    return module


def load(model: ModelPath | Path) -> MetaTable:
    """Load a Pydantic model from its schema file.

    Raises:
        ModelLoadError: If the file cannot be loaded, doesn't have a Model,
                       or Model is not a BaseModel subclass.
    """

    if isinstance(model, Path):
        model = ModelPath(model)

    path = module_path(model)
    schema = TableSchema.from_markdown_file(model.path)
    module = _load_module(model, schema)

    if not hasattr(module, "Schema"):
        raise ModelLoadError(f"Module {path} does not have a 'Schema' attribute")

    model_class = module.Schema

    if not isinstance(model_class, type):
        raise ModelLoadError(f"'Schema' in {path} is not a class")

    if not issubclass(model_class, pydantic.BaseModel):
        raise ModelLoadError(f"'Schema' in {path} is not a Pydantic BaseModel subclass")

    return MetaTable(model=model_class, schema=schema)
