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
    name: str,
    password: str,
    host: str,
    port: int,
    database_name: str,
    table_name: str,
    url: str,
):
    csv_name = "output.csv"

    os.system(f"wget {url} -O {csv_name}")
    engine = create_engine(
        f"postgresql://{name}:{password}@{host}:{port}/{database_name}"
    )

    parquet_file = pq.ParquetFile(csv_name)

    for batch in alive_it(parquet_file.iter_batches()):
        batch_df = batch.to_pandas()
        batch_df.to_sql(name=table_name, con=engine, if_exists="append")


if __name__ == "__main__":
    typer.run(main)
