import duckdb
from lib import listar_arquivos_filtrados
import pandas as pd
import sqlite3

files = listar_arquivos_filtrados('data/sample')
sql = """
CREATE OR REPLACE TABLE {1} AS
SELECT *
FROM read_csv_auto(
    '{0}',
    normalize_names=True
)
"""

with duckdb.connect('data/dev.sample.db') as con:
    con.execute("INSTALL sqlite")
    con.execute("LOAD  sqlite")

    for file in files:
        con.sql(sql.format(f'{file}', file.stem))
        # con.execute(f"EXPORT DATABASE '{file.stem}.sqlite' (FORMAT 'sqlite')")

    x = con.sql("show tables")
    print(x)


# sql = """
# SELECT *
# FROM read_csv_auto(
#     '{0}',
#     normalize_names=True
# )
# """

# # Conectar ao DuckDB e carregar o CSV
# con = duckdb.connect()
# for file in files:
#     df = con.execute(sql.format(f'{file}')).fetchdf()

#     # Conectar ao banco de dados SQLite
#     conn = sqlite3.connect('data/dev.sample.db')


#     # Exportar para o SQLite
#     df.to_sql(file.stem, conn, if_exists="replace", index=False)

# # Fechar a conexão
# conn.close()