# Spark: Batch Processing

*We use **Spark** as a tool for batch-processing of the raw data in our data lake (GCS bucket). We run spark locally on our VM and load the processed data back to the GCS bucket/datalake.*

## Install Spark on VM

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

## Connect Spark to GCS using Hadoop

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

## Workflow: Raw --> Processed data --> BQ Table