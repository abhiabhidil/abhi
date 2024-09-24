import pandas as pd
import numpy as np

student=pd.read_csv('Python/student_marks.csv')

student['math score']=student['math score'].fillna(student['math score'].max())
student['reading score']=student['reading score'].fillna(student['reading score'].max())
student['writing score']=student['writing score'].fillna(student['writing score'].max())

mean_math =student['math score'].mean()
meab_reading= student['reading score'].mean()
mean_writing= student['writing score'].mean()

std_math=student['math score'].std()
std_reading=student['reading score'].std()
std_writing=student['writing score'].std()

print(mean_math," ", std_math)
print(meab_reading," ", std_reading)
print(mean_writing," ", std_writing)

student_dict={}

for index,row in student.iterrows():
    group_letter=row['group'][-1]
    student_id=f"S{index+1}_{group_letter}"
    student_dict[student_id]=[row['math score'],row['reading score'],row['writing score']]

id_input=input("Enter:")
if id_input in student_dict:
    print(student_dict[id_input])
else:
    print("Not Found")
