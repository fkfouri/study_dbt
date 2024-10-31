import duckdb
from lib import listar_arquivos_filtrados
# import pandas as pd

files = listar_arquivos_filtrados('data/sample')
sql = """
CREATE OR REPLACE TABLE {0} AS
SELECT *
FROM read_csv_auto(
    '{1}',
    normalize_names=True
)
"""

with duckdb.connect('data/dev.sample.db') as con:
    for file in files:
        con.sql(sql.format(file.stem, f'{file}'))

    x = con.sql("show tables")
    print(x)