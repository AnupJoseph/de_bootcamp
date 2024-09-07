# Internal
import os

# External
import typer
import pandas as pd
from rich import print
from sqlalchemy import create_engine, event
import pyarrow.parquet as pq
from alive_progress import alive_it

# Project Specific config


def main(
    user: str = typer.Option("root", help="Username"),
    password: str = typer.Option("root", help="Password"),
    host: str = typer.Option("root", help="Database host"),
    port: int = typer.Option("root", help="Database port"),
    db: str = typer.Option("root", help="Database name"),
    table_name: str = typer.Option("root", help="Table to save in the DB"),
    url: str = typer.Option("root", help="Parquet file URL"),
):
    csv_name = "output.csv"

    os.system(f"wget {url} -O {csv_name}")
    engine = create_engine(f"postgresql://{user}:{password}@{host}:{port}/{db}")

    parquet_file = pq.ParquetFile(csv_name)

    for batch in alive_it(parquet_file.iter_batches()):
        batch_df = batch.to_pandas()
        batch_df.to_sql(name=table_name, con=engine, if_exists="append")


if __name__ == "__main__":
    typer.run(main)
