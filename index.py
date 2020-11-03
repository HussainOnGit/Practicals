import numpy as np
import pandas as pd


train_df = pd.read_csv(r"D:\Learning Node and stuff\python\train.csv", index_col = 'PassengerId')  
test_df = pd.read_csv(r"D:\Learning Node and stuff\python\test.csv",  index_col = 'PassengerId')

test_df['Survived'] = -888
df = pd.concat((train_df, test_df))
# print(df.iloc[4:10,  3:8])
print(df.head())
print(df.describe())
#print(df[['Name','Age','Survived']].min())