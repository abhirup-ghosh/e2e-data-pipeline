# Mage: Orchestrator

*We use **Mage** as an orchestrator to load raw data from Github (source) and export it to a GCS bucket (data lake). We do minimal processing of the raw data (set explicit data types and export as parquet files). The heavy-lifting of the processing would be done in subsequent steps with Spark and dbt.*

Pre-requisites: 
1. [Setup GCP resources (GCS bucket, Bigquery dataset, Dataproc cluster)](../terraform-iac/README.md)
2. [Download raw data files as csv files](../data/README.md)

## Build and start Mage on VM

**These instructions have been slightly modified from those of the [main project](https://github.com/mage-ai/mage-zoomcamp) to be self-sufficient within the context of our project.**

1. Clone the repo:

    ```bash
    git clone https://github.com/abhirup-ghosh/e2e-data-pipeline.git
    ```

2. Navigate to the orchestrator directory:

    ```bash
    cd e2e-data-pipeline/orchestrator-mage
    ```

3. Rename `dev.env` as `.env` — this will _ensure_ the file is not committed to Git by accident, since it _will_ contain credentials in the future.

    ```bash
    mv dev.env .env
    ```

4. Build and start the container

    ```bash
    docker-compose build
    docker-compose up
    ```

5. Navigate to http://localhost:6789 in your local macine browser (provided port 6789 had been already forwarded from VM to local machine using VS Code Remote-SSH)

## Build New Pipeline: API --> Datalake

We need to build a pipeline that loads raw data from the two csv files:
* appearances.csv
* competitions.csv

and exports them to our GCS bucket `capstone_datalake`. In order to do that, we follow these steps:

1. Build new pipeline by uploading the zip file `orchestrator-mage/etl_github_gcs_raw_data.zip`

2. Run@Once to load and export `appearances.parquet` and `competitions.parquet` to `capstone_datalake/raw`.

**The pipeline looks like this:**

![alt text](etl_github_gcs_raw_data.png)

**Datalake looks this:**

![alt text](<datalake.png>)