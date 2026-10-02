import psycopg2
import config
print(3333333333)

with psycopg2.connect(
    dbname=config.PGDATABASE,
    user=config.PGUSER,
    password=config.PGPASSWORD,
    host=config.PGHOST,
    port=5432,
) as connection:
    with connection.cursor() as cursor:
        sql_query = "SELECT 1"
        result = cursor.execute(sql_query)
        print(11111111)
        print(result)
        1/0
