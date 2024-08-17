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
    docker run -it -e POSTGRES_USER="root" -e POSTGRES_PASSWORD="root" -e POSTGRES_DB="ny_taxi" -v ny_taxi_postgres_data:/var/lib/postgresql/data -p 5432:5432 --network=pg-network postgres:13 
    ```
* To connect with `pgcli`
    ```sh
    pgcli -h localhost -p 5432 -u root -d ny_taxi
    ```

* To run the `pgadmin` tool
    ```sh
    docker run -it -e PGADMIN_DEFAULT_EMAIL="admin@admin.com" -e PGADMIN_DEFAULT_PASSWORD="root" -p 8080:80 --network=pg-network dpage/pgadmin4
    ```