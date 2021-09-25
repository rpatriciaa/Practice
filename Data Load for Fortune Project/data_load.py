import pandas as pd
from postgres import connect,copy_from_stringio

# CONNECTION string
param_dic = {
    "host"      : "localhost",
    "database"  : "fortune_dev",
    "user"      : "dbadmin",
    "password"  : "12345",
    "options"   : "-c search_path=fortune"
}

sectors = pd.read_csv('Pandas/Fortune1000.csv',usecols=['sector'],header=0).drop_duplicates()


conn = connect(param_dic)
copy_from_stringio(conn,sectors,"Sectors_DIM")
conn.close()