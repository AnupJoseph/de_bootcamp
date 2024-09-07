# de_bootcamp


## Usefull Shell commands
* To create a docker named volume
    ```sh
    docker volume create ny_taxi_postgres_data
    ```

* To create a network
    ```sh
    docker network create pg-network
    ```
* To start the postgres docker container
    ```sh
    docker run -it -e POSTGRES_USER="root" -e POSTGRES_PASSWORD="root" -e POSTGRES_DB="ny_taxi" -v ny_taxi_postgres_data:/var/lib/postgresql/data -p 5432:5432 --network=pg-network --name pg-database postgres:13 
    ```
* To connect with `pgcli`
    ```sh
    pgcli -h localhost -p 5432 -u root -d ny_taxi
    ```

* To run the `pgadmin` tool
    ```sh
    docker run -it -e PGADMIN_DEFAULT_EMAIL="admin@admin.com" -e PGADMIN_DEFAULT_PASSWORD="root" -p 8080:80 --network=pg-network dpage/pgadmin4
    ```

* To run the ingestion script
    ```sh
    python ingest_data.py --user=root --password=root --host=localhost --port=5432 --db=ny_taxi --table-name=yellow_taxi_trips --url="https://d37ci6vzurychx.cloudfront.net/trip-data/yellow_tripdata_2022-01.parquet"
    ```
    Doing the same in a docker container
    ```sh
    docker run -it --network=pg-network taxi_ingest:v001 --user=root --password=root --host=pg-database --port=5432 --db=ny_taxi --table-name=yellow_taxi_trips --url="https://d37ci6vzurychx.cloudfront.net/trip-data/yellow_tripdata_2022-01.parquet"
    ```