# Databricks notebook source
# MAGIC %sql
# MAGIC 
# MAGIC select * from bronze_gc.tb_lobby_stats_player

# COMMAND ----------

import sys 

sys.path.insert(0, '../lib')

from utils import db


# COMMAND ----------

tb_origin = 'bronze_gc.tb_lobby_stats_player'
tb_target = 'silver_gc.tb_lobby_stats_player'

id_origin = 'idLobbyGame', 'idPlayer'
id_target = 'idLobbyGame', 'idPlayer'

strongly_date_origin = 'dtCreatedAt'
strongly_date_target = 'dtCreatedAt'

checkpoint_path = f'/mnt/datalake/silver/{tb_target.split(".")[-1]}_checkpoint'


# COMMAND ----------

query = db.import_query('queries/tb_lobby_stats_player.sql')
df = db.etl(query,tb_origin)
df = etl(query, tb_origin, spark)

# COMMAND ----------

df_stream = spark.readStream.format("delta")
                 .option("readChangeFeed", "true")
                 .option("startingVersion", 0)
                 .table(tb_origin)

stream = (df_stream.writeStream.format('delta')
                   .foreachBatch( lambda df, batchId: upsert_delta(df, batchId, delta_table, id_field, strongly_date))
                   .option('checkpointLocation', checkpoint_path)
                   .start())


# COMMAND ----------


