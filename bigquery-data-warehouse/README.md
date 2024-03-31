# BigQuery: Data warehouse

*We use BigQuery as our data warehouse, and produce materialised tables paritioned by date and clustered by player_id, from the external data `prod.fact_football_data` outputed by dbt data transformations.*

Pre-requisites: [Production processed materialised table `e2e-data-pipeline-capstone.prod.fact_football_data` -- output of data transformation tool dbt](../dbt-data-transformation/README.md)

## Queries

We use the SQL queries in this folder to create two tables:
* `fact_football_data_partitioned`: partitioned on date
* `fact_football_data_partitioned_clustered`: partitioned on data and clustered by player_id

### Partitioning

```sql
-- Creating a paritioned table
CREATE OR REPLACE TABLE `e2e-data-pipeline-capstone.prod.fact_football_data_partitioned`
PARTITION BY DATE(date) AS
SELECT * FROM `e2e-data-pipeline-capstone.prod.fact_football_data`;
```

### Partitioning and clustering

```sql
-- Creating a paritioned and clustered table
CREATE OR REPLACE TABLE `e2e-data-pipeline-capstone.prod.fact_football_data_partitioned_clustered`
PARTITION BY DATE(date)
CLUSTER BY player_id AS
SELECT * FROM `e2e-data-pipeline-capstone.prod.fact_football_data`;
```

## BigQuery Tables

**Final list of external/materialised tables created on BigQuery**

![alt text](<bigquery_tables_final.png>)