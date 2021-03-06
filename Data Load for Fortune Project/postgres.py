import pandas as pd
import sys
import psycopg2
from io import StringIO

#Connect functions
def connect(params_dic):
    conn = None
    try:
        print('Connecting to the PostgreSQL database...')
        conn = psycopg2.connect(**params_dic)
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
        sys.exit(1) 
    print("Connection successful")
    return conn

def copy_from_stringio(conn, df, table,cols):
    # save dataframe to an in memory buffer
    buffer = StringIO()
    df.to_csv(buffer,index= False, header = False,sep=';')
    buffer.seek(0)

    cursor = conn.cursor()
    try:
       cursor.copy_from(buffer, table,sep=';',columns=cols)
       conn.commit()
    except (Exception, psycopg2.DatabaseError) as error:
        print("Error: %s" % error)
        conn.rollback()
        cursor.close()
        return 1
    print("copy_from_stringio() done")
    cursor.close()

def select_data(conn,table):
    cursor = conn.cursor()
    query = 'SELECT * FROM ' + table
    try:
       cursor.execute(query)
       fdata = cursor.fetchall()
       conn.commit()
    except (Exception, psycopg2.DatabaseError) as error:
        print("Error: %s" % error)
        conn.rollback()
        cursor.close()
        return 1
    print("Select statement done")
    cursor.close()

    return pd.DataFrame(data=fdata, index=None)
