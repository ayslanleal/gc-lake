import argparse
import os

import pandas as pd
import boto3
import sqlalchemy

if not os.path.exists('../data/incremental/tb_lobby_stats_player/'):
    os.mkdir('../data/incremental/tb_lobby_stats_player/')

parser = argparse.ArgumentParser()
parser.add_argument("--nPlayers", "-n", default=100)
args = parser.parse_args()

db = sqlalchemy.create_engine("sqlite:///../data/incremental/gc_incremental.db")
s3_client = boto3.client('s3')

with open("incremental_query.sql", "r") as open_file:
    query = open_file.read()

query = query.format(nPlayers=args.nPlayers)

df = pd.read_sql(query,db)

last_id = df['idLobbyGame'].min()
filename = f"../data/incremental/tb_lobby_stats_player/{last_id}.csv"
df.to_sql("tb_lobby_stats_player", db, if_exists='append', index=False)

df['Op'] = 'I'
df.to_csv(filename, index=False)
#s3_client.upload_file(filename, '', f"raw/gc/cdc/tb_lobby_stats_player/{last_id}.csv")