# Mage: Orchestrator

## Build and start Mage

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

3. Build and start the container

    ```bash
    docker-compose build
    docker-compose up
    ```

4. Navigate to http://localhost:6789 in your local macine browser (provided port 6789 had been already forwarded from VM to local machine using VS Code Remote-SSH)

## ETL: API to GCS

Pipeline: http://localhost:6789/pipelines/github_to_gcs_raw_data/triggers 

Code: [github_to_gcs_raw_data](magic-zoomcamp/pipelines/github_to_gcs_raw_data)

Steps:

* Load data from `data/` folder using 
* Export to GCS bucket 
