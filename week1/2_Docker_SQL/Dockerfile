FROM python:3.9
RUN apt-get install wget
RUN pip install pandas sqlalchemy psycopg2 typer pyarrow alive_progress
WORKDIR /app
COPY ingestion_script.py ingestion_script.py
ENTRYPOINT [ "python","ingestion_script.py" ]