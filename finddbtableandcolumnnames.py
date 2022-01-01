import pandas as pd 
import sqlite3
import xlsxwriter

file_path =r"" #FILE_PATH
conn = sqlite3.connect(r'') #dbpath

writer=pd.ExcelWriter(file_path, engine ='xlsxwriter')

df = pd.read_sql("SELECT name from sqlite_master WHERE type = 'table'", conn)

for table_name in df['name']:
  sheet_name = table_name
  SQL = "SELECT * FROM " + sheet_name
  dft = pd.read_sql(SQL, conn)
  dft.to_excel(writer, sheet_name = sheet_name, index = False)
  
writer.save()