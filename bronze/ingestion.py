# Databricks notebook source
from pyspark.sql import types
import json

def import_schema(table_name):
    with open(f'schemas/{table_name}.json', 'r') as open_file:
        schema = json.load(open_file)
    return types.StructType.fromJson(schema)

def table_exists(table_name):
    query = f"""show tables from bronze_gc like '{table_name}'"""
    df = spark.sql(query)
    return df.count() > 0

# COMMAND ----------

table_name = "tb_players"
raw_path = f'/mnt/datalake/raw/gc/full_load/{table_name}.csv'
table_schema = import_schema(table_name)


# COMMAND ----------

if not table_exists(table_name):
    df = spark.read.schema(table_schema).csv(raw_path, header=True)
    df.write.format('delta').saveAsTable(f'bronze_gc.{table_name}')

# COMMAND ----------



# COMMAND ----------


