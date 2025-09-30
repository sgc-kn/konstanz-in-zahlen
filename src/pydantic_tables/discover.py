from pathlib import Path


def root() -> Path:
    """Find the project root by locating pyproject.toml"""
    path = Path(__file__).resolve()
    for parent in path.parents:
        if (parent / "pyproject.toml").exists():
            return parent
    raise FileNotFoundError("Could not find pyproject.toml to determine project root.")


def csv_files() -> list[Path]:
    return list(root().glob("data/**/*.csv"))


def dataset(name: str) -> Path:
    path = root() / "data" / name
    if not path.is_dir():
        raise KeyError(f"dataset does not exist: {name}")
    return path


def datasets() -> list[Path]:
    return list(root().glob("data/**"))
