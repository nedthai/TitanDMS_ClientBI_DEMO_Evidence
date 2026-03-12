import pyodbc
import pandas as pd
import duckdb
import os
import time

# SQL Server Connection Configuration
SERVER = r'TITAN-VN-P-91\MSSQLSERVER2019'
DATABASE = 'DemoDealerAI'
PORT = '1433'
USERNAME = 'sa'
PASSWORD = 'Thanhlong@00'

# DuckDB Connection Configuration
# We place the duckdb file in the ../data/ directory relative to this script
DUCKDB_PATH = os.path.join(os.path.dirname(__file__), '..', 'data', 'DemoDealerAI.duckdb')

# List of tables to extract based on Database Building.sql
TABLES = [
    'DimCompany',
    'DimLocation',
    'DimMake',
    'DimModelType',
    'DimModel',
    'DimDate',
    'DimVehicleClass',
    'DimVehicleType',
    'DimVehicleSalesGroup',
    'DimVehicleStockcardStatus',
    'DimDaysInStockCategory',
    'DimVehicle',
    'DimVehicleAcquisition',
    'FactVehicleStockCurrent',
    'FactVehicleStockMovement',
    'FactVehicleSales'
]

def get_sql_server_connection():
    # Construct connection string for pyodbc
    conn_str = (
        f'DRIVER={{ODBC Driver 17 for SQL Server}};'
        f'SERVER={SERVER},{PORT};'
        f'DATABASE={DATABASE};'
        f'UID={USERNAME};'
        f'PWD={PASSWORD};'
    )
    # Note: If ODBC Driver 17 is not available, try 'SQL Server'
    try:
        conn = pyodbc.connect(conn_str)
        return conn
    except pyodbc.Error as e:
        print(f"Error connecting using ODBC Driver 17: {e}")
        print("Falling back to 'SQL Server' driver...")
        conn_str_fallback = (
            f'DRIVER={{SQL Server}};'
            f'SERVER={SERVER},{PORT};'
            f'DATABASE={DATABASE};'
            f'UID={USERNAME};'
            f'PWD={PASSWORD};'
        )
        return pyodbc.connect(conn_str_fallback)

def main():
    print(f"Starting ETL process from SQL Server ({SERVER}) to DuckDB ({DUCKDB_PATH})")
    start_time = time.time()
    
    # Establish connections
    try:
        sql_conn = get_sql_server_connection()
        print("Successfully connected to SQL Server.")
    except Exception as e:
        print(f"Failed to connect to SQL Server: {e}")
        return

    try:
        duck_conn = duckdb.connect(DUCKDB_PATH)
        print("Successfully connected to DuckDB.")
    except Exception as e:
        print(f"Failed to connect to DuckDB: {e}")
        sql_conn.close()
        return

    total_rows = 0

    for table in TABLES:
        print(f"Extracting table: {table} ...", end=" ", flush=True)
        query = f"SELECT * FROM dbo.{table}"
        try:
            # Read from SQL Server into pandas DataFrame
            df = pd.read_sql(query, sql_conn)
            row_count = len(df)
            
            # Save into DuckDB safely
            # Note: duckdb can directly read the 'df' variable from the local scope
            duck_conn.execute(f"CREATE OR REPLACE TABLE {table} AS SELECT * FROM df")
            
            print(f"Done. ({row_count} rows)")
            total_rows += row_count
        except Exception as e:
            print(f"Error processing table {table}: {e}")

    # Close connections
    duck_conn.close()
    sql_conn.close()

    end_time = time.time()
    duration = end_time - start_time
    print(f"\nETL process completed in {duration:.2f} seconds.")
    print(f"Total rows extracted: {total_rows}")

if __name__ == "__main__":
    main()
