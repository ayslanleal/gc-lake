from pyspark.sql import types

def import_query(path):
    with open(path , 'r') as open_file:
        query = open_file.read()
    return query

def import_schema(table_name):
    with open(f'schemas/{table_name}.json', 'r') as open_file:
        schema = json.load(open_file)
    return types.StructType.fromJson(schema)


def table_exists(table_name , spark):
    query = f"""show tables from bronze_gc like '{table_name}'"""
    df = spark.sql(query)
    return df.count() > 0


def etl(query, table, spark):
    query_format = query.format(table=table)
    df = spark.sql(query_format)
    return df