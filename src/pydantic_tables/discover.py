from pathlib import Path


def data() -> Path:
    cwd = Path.cwd()

    if (cwd / "data").is_dir():
        return cwd / "data"

    raise RuntimeError(f"Data path not found. The current working directory is: {cwd}")


def csv_files(data: Path) -> list[Path]:
    return list(data.glob("**/*.csv"))


def dataset(data: Path, name: str) -> Path:
    path = data / name
    if not path.is_dir():
        raise KeyError(f"dataset does not exist: {name}")
    return path


def datasets(data: Path) -> list[Path]:
    return list(data.glob("*"))
