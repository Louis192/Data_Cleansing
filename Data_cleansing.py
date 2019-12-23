import pandas as pd
df=pd.read_csv('Booking3.csv')
df.head(5)

import re
def new_column(s):
    return " ".join(s.split('\n')[:1])


df["room_2"]=df["room"].apply(lambda x: x if str(x) == 'nan' else new_column(x))
df=df.loc[:,~df.columns.str.contains('^Unnamed')]
df=df.drop(columns=["room"])
df=df.loc[:,~df.columns.str.contains('^Unnamed')]
df.head()