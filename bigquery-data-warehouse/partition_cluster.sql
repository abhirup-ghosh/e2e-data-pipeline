-- Creating a paritioned and clustered table
CREATE OR REPLACE TABLE `e2e-data-pipeline-capstone.prod.fact_football_data_partitioned_clustered`
PARTITION BY DATE(date)
CLUSTER BY player_id AS
SELECT * FROM `e2e-data-pipeline-capstone.prod.fact_football_data`;