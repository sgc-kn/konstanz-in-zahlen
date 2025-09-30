import typer
from . import dataset, excel
from .schema import TableSchema
from pathlib import Path

app = typer.Typer(help="pytab - the pydantic tables command line utiliy")


@app.command("export")
def _export(
    directory: Path = typer.Argument(..., help="Directory containing the CSV files"),
    output: Path = typer.Option(
        None, "--output", "-o", help="Destination for output Excel file"
    ),
):
    """Export data to Excel."""

    if not directory.exists():
        typer.echo(f"Error: Directory {directory} does not exist", err=True)
        raise typer.Exit(1)

    if not directory.is_dir():
        typer.echo(f"Error: {directory} is not a directory", err=True)
        raise typer.Exit(1)

    csv_files = list(directory.glob("*.csv"))

    if not csv_files:
        typer.echo(f"No CSV files found in {directory}")
        raise typer.Exit(1)

    dataset_ = dataset.load(directory)

    if output is None:
        output = directory / (directory.stem + ".xlsx")

    excel.save(dataset_, path=output)

    typer.echo(f"Exported {len(csv_files)} CSV files to Excel: {output}")


@app.command("import")
def _import(
    directory: Path = typer.Argument(..., help="Directory containing the CSV files"),
    excel_file: Path = typer.Option(None, "--input", "-i", help="Source Excel file"),
):
    """Import data from Excel."""

    if not directory.exists():
        typer.echo(f"Error: Directory {directory} does not exist", err=True)
        raise typer.Exit(1)

    if not directory.is_dir():
        typer.echo(f"Error: {directory} is not a directory", err=True)
        raise typer.Exit(1)

    if excel_file is None:
        excel_file = directory / (directory.stem + ".xlsx")

    if not excel_file.exists():
        typer.echo(f"Error: Excel file {excel_file} does not exist", err=True)
        raise typer.Exit(1)

    if not excel_file.is_file():
        typer.echo(f"Error: {excel_file} is not a file", err=True)
        raise typer.Exit(1)

    dataset_ = excel.load(excel_file, directory)

    if len(dataset_.tables) < 1:
        typer.echo(f"No sheets found in {excel_file}")
        raise typer.Exit(1)

    dataset.save(dataset_, directory)

    typer.echo(f"Imported {len(dataset_.tables)} table(s) from Excel: {excel_file}")
    for name in dataset_.tables.keys():
        typer.echo(f"  - {name}.csv")


@app.command("format-markdown")
def _format_markdown(
    path: Path = typer.Argument(..., help="Path to the markdown schema file."),
):
    """
    Format table schema markdown files (inplace).

    This just parses the schema and emits it again.
    """

    if not path.exists():
        typer.echo(f"Error: Path {path} does not exist", err=True)
        raise typer.Exit(1)

    if not path.is_file():
        typer.echo(f"Error: {path} is not a file", err=True)
        raise typer.Exit(1)

    schema = TableSchema.from_markdown_file(path)
    schema.to_markdown_file(path)


@app.command("create-pydantic-model")
def _create_pydantic_model(
    paths: list[Path] = typer.Argument(..., help="Path to the markdown schema file."),
):
    """
    Translate table schema markdown file to python.
    """

    if len(paths) == 0:
        typer.echo("Error: provide at least one path", err=True)

    for path in paths:
        if not path.exists():
            typer.echo(f"Error: Path {path} does not exist", err=True)
            raise typer.Exit(1)

        if not path.is_file():
            typer.echo(f"Error: {path} is not a file", err=True)
            raise typer.Exit(1)

        schema = TableSchema.from_markdown_file(path)
        path = path.with_suffix(".py")
        schema.to_python_file(path)

        print("wrote python schema: ", path)


if __name__ == "__main__":
    app()
