# Spark: Batch Processing

*We use **Spark** as a tool for batch-processing of the raw data in our data lake (GCS bucket). We run spark through GCP's **Dataproc** cluster and load the processed data directly to our **Big Query data warehouse**.*

## Install Spark on VM [For testing]

To install **Spark/pySpark**, follow the instructions here: 

```
https://github.com/DataTalksClub/data-engineering-zoomcamp/blob/main/05-batch/setup/linux.md
```

Add the following lines to your `~/.bashrc`

```vim
# Add JAVA variables to PATH
export JAVA_HOME="${HOME}/spark/jdk-11.0.2"
export PATH="${JAVA_HOME}/bin:${PATH}"

# Add SPARK variables to PATH
export SPARK_HOME="${HOME}/spark/spark-3.3.2-bin-hadoop3"
export PATH="${SPARK_HOME}/bin:${PATH}"

# Add PySpark Variables to PYTHONPATH
export PYTHONPATH="${SPARK_HOME}/python/:$PYTHONPATH"
export PYTHONPATH="${SPARK_HOME}/python/lib/py4j-0.10.9.5-src.zip:$PYTHONPATH"
```

### Connect Spark to GCS using Hadoop

1. Navigate to `spark` folder in project and create a directory `spark/lib` and navigate to it.

```
:~e2e-data-pipeline$ ls cd spark
:~e2e-data-pipeline/spark$ mkdir lib
:~e2e-data-pipeline/spark$ cd lib
```

2. Download the connector

```
gsutil cp gs://hadoop-lib/gcs/gcs-connector-hadoop3-2.2.5.jar gcs-connector-hadoop3-2.2.5.jar
```

The location of this connector needs to be remembered and pointed to, when setting up the cluster.

## Setup Dataproc Cluster in GCP [for Production]

Follow the instructions [here](https://youtu.be/osAiAYahvh8?list=PL3MmuxUbc_hJed7dXYoJw8DoCuVHhGEQb) to setup a Dataproc cluster on GCP. Use the following information when prompted:

* Cluster Name: `capstone-cluster`
* Location -- Region/Zone: `europe-north1-a` (same as compute engine)
* Cluster Type: Single Node (optional components: Jupyter, Docker), ** subnetwork set to default

Add a service account with `Dataproc Administrator` role privileges.

## Setup Job

Our job involves reading in the input files (`appearances.parquet` and `competitions.parquet`) and merging them into one data file: `data_all.parquet`. We test this framework locally using the notebook: [processing_data_pyspark_local.ipynb](./processing_data_pyspark_local.ipynb).

Then we create a [python notebook](./processing_data_pyspark_bigquery.py) out of this, which is tuned to Dataproc and not a local cluster. It takes as inputs `appearances.parquet` and `competitions.parquet` and outputs a bigquery table, `data_all`.

## Submit job using PySpark on Dataproc

1. Create job as a python file: [processing_data_pyspark_bigquery.py](./processing_data_pyspark_bigquery.py)

2. Upload the script to GCS:
    ```
    gsutil cp processing_data_pyspark_bigquery.py gs://capstone_datalake/code
    ```
3. Write results to big query ([docs](https://cloud.google.com/dataproc/docs/tutorials/bigquery-connector-spark-example#pyspark)):

    ```
    gcloud dataproc jobs submit pyspark \
        --cluster=capstone-cluster \
        --region=europe-north1 \
        --jars=gs://spark-lib/bigquery/spark-bigquery-latest_2.12.jar \
        gs://capstone_datalake/code/processing_data_pyspark_bigquery.py \
        -- \
            --input_appearances=gs://capstone_datalake/appearances.parquet \
            --input_competitions=gs://capstone_datalake/competition.parquet \
            --output=capstone_dataset.data_all
    ```

4. Check BigQuery for table: `e2e-data-pipeline-capstone.capstone_dataset.data_all`