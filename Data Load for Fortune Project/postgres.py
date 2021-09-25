
import os
import sys
import psycopg2
import psycopg2.extras as extras
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

def copy_from_stringio(conn, df, table):
    # save dataframe to an in memory buffer
    buffer = StringIO()
    df.to_csv(buffer,index= False, header = False)
    buffer.seek(0)
    print(df)
    cursor = conn.cursor()
    try:
       cursor.copy_from(buffer, table,columns=['Sector Name'])
       conn.commit()
    except (Exception, psycopg2.DatabaseError) as error:
        print("Error: %s" % error)
        conn.rollback()
        cursor.close()
        return 1
    print("copy_from_stringio() done")
    cursor.close()
