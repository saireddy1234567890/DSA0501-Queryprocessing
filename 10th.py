import pandas as pd
data = pd.read_csv("C:/Users/Hari Prasad/Desktop/Query proccessing/dept.csv")
unique_rows = data['DEPARTMENT_ID'].unique()
print("Unique_id:\n",unique_rows)
