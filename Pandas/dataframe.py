import pandas as pd
import re


#from list of list to dataframe
lst_fruits = [['Apple', 15], ['Orange', 30], 
       ['Banana', 22], ['Strawberry', 10]]

df_fruits= pd.DataFrame(lst_fruits,columns=['Fruit Name','Price'])

#tuples 

tpl_fruits = [('Apple','Lower',10),('Orange','Higher',32),('Banana','Equal',22)]

df_tuple = pd.DataFrame(tpl_fruits, columns=['Fruit Name','Direction','Price'])

#print(df_tuple.pivot('Fruit Name','Direction','Price'))

#regex
#replace stringgs
df_fruits = df_fruits.replace(to_replace = 'Apple', value='Pear(new)', regex=True)
print(df_fruits)

##
def Clean_names(fruit_name):
    if re.search('\(.*', fruit_name):
        pos = re.search('\(.*', fruit_name).start()
        return fruit_name[:pos]
    else:
        return fruit_name
          
# Updated the city columns
df_fruits['Fruit Name'] = df_fruits['Fruit Name'].apply(Clean_names)
  
# Print the updated dataframe
print(df_fruits)


#series + dataframe

fruits = ['Apple','Apple','Orange','Banana']
prices = [10,10,15,12]
ser_fruits = pd.Series(fruits)
ser_prices = pd.Series(prices)

frame = {'Fruits': ser_fruits, 'Prices': prices}

df_ser_fruits = pd.DataFrame(frame)

#basic functions
print(df_ser_fruits['Prices'].max())
print(df_ser_fruits['Prices'].idxmax())
print(df_ser_fruits['Prices'].min())
print(df_ser_fruits['Prices'].idxmin())
print(df_ser_fruits['Prices'].median())
print(df_ser_fruits['Prices'].mean())
print(df_ser_fruits['Prices'].std())
print(df_ser_fruits['Fruits'].value_counts())
print(df_ser_fruits['Fruits'].unique())