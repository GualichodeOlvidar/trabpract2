import pandas as pd
import yfinance as yf
from sqlalchemy import create_engine
from config import DB_CONFIG

# Descargar datos financieros
ticker = 'AAPL'
data = yf.download(ticker, start='2022-01-01', end='2023-12-31')
data.reset_index(inplace=True)

# Crear conexión a PostgreSQL
db_url = f"postgresql+psycopg2://{DB_CONFIG['user']}:{DB_CONFIG['password']}@{DB_CONFIG['host']}:{DB_CONFIG['port']}/{DB_CONFIG['database']}"
engine = create_engine(db_url)

# Crear tabla y cargar datos
data.to_sql('stock_data', engine, if_exists='replace', index=False)

print(f"Datos cargados correctamente ({len(data)} registros) en la tabla 'stock_data'.")
