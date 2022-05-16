from tqdm import tqdm
import boto3
import pandas as pd
import sqlalchemy


def save_bucket_s3(db, table, s3_client):
    pd.read_sql(table, db).to_csv(f"../data/{table}.csv")
    #s3_client.upload_file(Bucket='bucket_name', Filename=f"{table}.csv", Key=f'raw/gc/full_load/{table}.csv')
    

db = sqlalchemy.create_engine("sqlite:///../data/gc.db")
tables = db.table_names()
s3_client = 1 #boto3.client('s3')

for i in tqdm(tables):
    save_bucket_s3(db,i,s3_client)

