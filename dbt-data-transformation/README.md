# dbt Cloud: Data transformation 

*We use dbt cloud to transform the data inside the Big Query data warehouse. The transformation involves restricting the data to first-tier domestic leagues of the top 5 European leagues -- Germany, Spain, England, France and Italy.*

Pre-requisites: [Orchestrate raw data into GCS bucket using Mage](../mage-orchestrator/README.md).

## Setup dbt project

1. Setup dbt developer account at https://cloud.getdbt.com/
2. Follow the instructions [here](https://github.com/DataTalksClub/data-engineering-zoomcamp/blob/main/04-analytics-engineering/dbt_cloud_setup.md) to create a dbt project.
3. Create project with:
    * project name: `e2e-data-pipeline-capstone`
    * project sub-directory: `dbt`
    * repository: `git@github.com:abhirup-ghosh/e2e-data-pipeline.git`
    * BigQuery connection: `gcp_service_capstone.json` (same service account as terraform resources)

## Setup dbt Model

**AIM:** create a dbt model that will keep filter the data for appearances only in the first tiers of the 5 big leagues in Europe: Germany, Spain, England, France and Italy. We also do not need all columns.

1. Create dbt model using [schema.yml](./models/staging/schema.yml) and [fact_football_data.sql](./models/staging/fact_football_data.sql)
2. Filter the data to first-tier domestic leagues in Germany, Spain, England, France and Italy.
3. `dbt build` to create the table: `e2e-data-pipeline-capstone.capstone_datalake.dbt_aghosh.fact_football` inside BigQuery data warehouse.
4. Deploy a Nightly production that creates the table `prod`

A successful deployment of **Nightly**.
![alt text](<nightly_deployment.png>)

🚨 Region error: dbt Developer account only allows the creation of resources in the US region. All of our other resources, including the raw data table in BigQuery are in the europe-north1 region. Hence, we create a replica of `e2e-data-pipeline-capstone.capstone_datalake.data_all` in the US region and make it primary. Only in this combination, would we be able to read from this table and write to `e2e-data-pipeline-capstone.capstone_datalake.dbt_aghosh`.