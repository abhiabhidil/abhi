import numpy as np
import pandas as pd


df=pd.read_csv('Python/world_population.csv')
#mf=df()
data=df[["Country","2022 Population","Growth Rate"]]
for x,y in data.iterrows():
    print(x, y)
#print(df[['Country','2000 Population']])
