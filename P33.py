import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt

df=pd.read_csv('Py2/student.csv')

#plt.figure(figsize=(8,8))

plt.subplot(3,1,1)
sns.kdeplot(df['Age'])

bike=pd.read_csv('Py2/bike.csv')
bike['Day']=bike.groupby(['Year','Month','Hour']).ngroup()
daily_rentals=bike.groupby('Day')['Count'].sum().reset_index()

plt.subplot(3,1,2)
plt.plot(daily_rentals['Day'],daily_rentals['Count'])

temp=pd.read_csv('Py2/heart_transplant.csv')
temp['Transplant'] = temp['Transplant'].replace({'treatment': 1, 'control': 0})
temp['Survival Time'] = temp['Age of death'] - temp['Age']

mean_survival = temp.groupby('Transplant')['Survival Time'].mean()

plt.subplot(3,1,3)

mean_survival.plot(kind='bar')

plt.grid(True, axis='y')

plt.show()

# Display the calculated mean survival times for reference
print(mean_survival)
