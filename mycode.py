import pandas as pd
import os

data = {'Name':['Chiranjeev','Rajat'],
'Age':[23,25],
'City' :['Delhi','Rewari']}

df = pd.DataFrame(data)

new_row = {'Name':'Amit','Age':30,'City':'Mumbai'}
df.loc[len(df)] = new_row
data_dir = 'data'

os.makedirs(data_dir,exist_ok = True)
file_path = os.path.join(data_dir,'sample_data.csv')

df.to_csv(file_path,index=False)
print(f"CSV file saved to {file_path}")
