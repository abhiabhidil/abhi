import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

df=pd.read_csv('Py2/student.csv')

meanAge=df['Age'].mean()
stdAge=df['Age'].std()

df['Zscore']=(df['Age']-meanAge)/stdAge

df_f=df[df['Zscore'].notna()]

#print(df_f)

outliers=df_f[(df_f['Zscore'] > 3) | (df_f['Zscore'] < -3)]

print(outliers)

notOutliers=df_f[(df_f["Zscore"]<3) & (df_f['Zscore']>-3)]
#print(notOutliers)
a_18=0
a18_21=0
a21_=0
for i,row in notOutliers.iterrows():
    if row['Age']<=18:
        a_18+=1
    elif row['Age']>18 and row['Age']<=21:
        a18_21+=1
    else:
        a21_+=1

x=np.array([a_18,a18_21,a21_])
y=["Age ≤ 18", "18 < Age ≤ 21", "Age > 21"]

plt.pie(x, labels=y)
plt.show()
