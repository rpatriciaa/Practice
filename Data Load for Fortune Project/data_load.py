import pandas as pd
from postgres import connect,copy_from_stringio,select_data
from mapping import mapping
from con import param_dic


conn = connect(param_dic)
#sectors = pd.read_csv('Data Load for Fortune Project/Fortune1000.csv',header=0, sep=';', usecols=['sector'], skipinitialspace=True).drop_duplicates()
#copy_from_stringio(conn,sectors['sector'],"Sectors_DIM",['Sector Name'])
sector_with_ids = select_data(conn,'fortune."Sectors_DIM"').rename(columns={0: 'id', 1: 'sector'})
companies = pd.read_csv('Data Load for Fortune Project/Fortune1000.csv',header=0, skipinitialspace=True).drop_duplicates()
merged = mapping(sector_with_ids,companies)
copy_from_stringio(conn,merged[['id','name']],'Companies_DIM',['Sector_ID','Company_Name'])

conn.close()
