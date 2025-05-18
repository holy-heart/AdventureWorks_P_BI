import pyodbc
import pandas as pd

conn = pyodbc.connect('DRIVER={SQL Server};SERVER=localhost\\SQLEXPRESS;DATABASE=AdventureWorksDW2019;Trusted_Connection=yes;')


df = pd.read_sql('SELECT TOP 5 * FROM DimCustomer', conn)
print(df)