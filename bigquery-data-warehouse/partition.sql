-- Creating a paritioned table
CREATE OR REPLACE TABLE `e2e-data-pipeline-capstone.prod.fact_football_data_partitioned`
PARTITION BY DATE(date) AS
SELECT * FROM `e2e-data-pipeline-capstone.prod.fact_football_data`;