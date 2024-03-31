#!/usr/bin/env python
# coding: utf-8

import argparse

import pyspark
from pyspark.sql import SparkSession

parser = argparse.ArgumentParser()

parser.add_argument('--input_appearances', required=True)
parser.add_argument('--input_competitions', required=True)
parser.add_argument('--output', required=True)

args = parser.parse_args()

input_appearances = args.input_appearances
input_competitions = args.input_competitions
output = args.output

spark = SparkSession.builder \
    .appName('test') \
    .getOrCreate()

spark.conf.set('temporaryGcsBucket', 'dataproc-staging-europe-north1-1021722663072-fkqjxac0')

# reading data as spark dataframes with previously 

df_appearances = spark.read\
                    .parquet(input_appearances)

df_competitions = spark.read\
                    .parquet(input_competitions)

df_data_all = df_appearances.join(df_competitions, on='competition_id', how='left')

df_data_all.registerTempTable('data_all')

df_data_all.write.format('bigquery') \
    .option('table', output) \
    .save()
    
