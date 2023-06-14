import pandas as pd 
import os
import json


config_path = 'Data/train_config.json' 
# Opening JSON file
data = json.load(open(config_path))
training_data_FileName =  data['training_data_FileName']
data_dir = data["data_loc"]




for dirname, _, filenames in os.walk(data_dir):
    for filename in filenames:
        if filename == training_data_FileName:
            testdata_path = os.path.join(dirname, filename)
        else:
            continue


target_col = 'Survived'
data = pd.read_csv(testdata_path)

cols_dropped = []
cols_keep = []

for col in data:
    nulls = data[col].isnull().sum()
    if nulls >0 or data[col].dtype == 'object':
        cols_dropped.append(col)
    else:
        cols_keep.append(col)
        continue


print(data.info())

print(cols_dropped)

print(cols_keep)

data = data[cols_keep]


print(data)




print(data['Fare'].std())
print(data['Fare'].mean())