import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

df = pd.read_csv('Py2/student.csv')

marks_column=['Final Physics marks','Final Chemistry marks','Final Maths marks','Final English marks']
marks=[]

student_detail = df[df['Roll number']=='RN_15']

for subject in marks_column:
    marks.append(student_detail[subject].values[0])

plt.bar(marks_column,marks)
plt.show()

weight_column=['weight_january', 'weight_april','weight_july', 'weight_october']
weights=[]
for month in weight_column:
    weights.append(student_detail[month].values[0])

plt.plot(weight_column,weights,marker='.')
plt.show()