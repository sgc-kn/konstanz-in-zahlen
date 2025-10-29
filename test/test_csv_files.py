import pytest

from pathlib import Path
from pydantic_tables import csv, discover, model

root = discover.data()


@pytest.mark.parametrize("csv_file", [str(p) for p in discover.csv_files(root)])
def test_csv_has_schema(csv_file: str):
    """Test: Ensure each table.csv has a corresponding table.md"""
    schema = Path(csv_file).with_suffix(".md")
    assert schema.exists(), f"Missing {schema} file for {csv_file}"


@pytest.mark.parametrize("csv_file", [str(p) for p in discover.csv_files(root)])
def test_schema(csv_file: str):
    """Test: Validate schema"""
    csv_path = Path(csv_file)
    schema_path = csv_path.with_suffix(".md")
    if not schema_path.exists():
        pytest.skip(f"Skipping because {csv_path} has no schema")

    model_ = model.load(schema_path)
    csv.load_and_validate(csv_path, model_)


@pytest.mark.parametrize("csv_file", [str(p) for p in discover.csv_files(root)])
def test_csv_data(csv_file: str):
    """Test: Validate CSV against its schema"""
    csv_path = Path(csv_file)
    schema_path = csv_path.with_suffix(".md")

    # tested above
    if not schema_path.exists():
        pytest.skip(f"Skipping because {csv_path} has no schema")

    # tested above
    try:
        model_ = model.load(schema_path)
    except:  # noqa: E722
        pytest.skip(f"Skipping becasue {csv_path} has invalid schema")

    # new aspect of this test
    csv.load_and_validate(csv_path, model_)
