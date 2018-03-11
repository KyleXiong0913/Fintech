# Solutions as below
# 1. we divide the customers into 3 segments,
# 2. The reason we have 3 segments are because
# we assume customers can be have main goals on House, Travel and Car
# based on their HG Time (Months), TG Time (Months) and CG Time (Months)
# 3. Use knn (k nearest neighbors) algorithm to do the classification based on age and monthly income. 
# and use accuracy(correctly_predicted_number_of_data/total_number_of_data) as the scoring methods.
# import the necessary libraries
from pandas import DataFrame, read_csv
from sklearn.neighbors import KNeighborsClassifier

import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import csv

xl = pd.ExcelFile('Fintech.xlsx')
# 1991 * 12
print("Names of the all the sheets in the excelfile")
print(xl.sheet_names)

df1 = xl.parse("Cust List Qn 2")
# df2 = xl.parse("Cust List Qn 3")
# print the first worksheet of the dataframe
# 9999 * 7
# print(df1)
print(df1.dtypes)

# Get the related columns.
df11 = df1[['HG Time (Months)','TG Time (Months)','CG Time (Months)']]
# print(df11);
# 
df12 = df11.max(axis=1)
# print(df12);

df13 = df11.idxmax(axis=1)
# print(df13)

df21 = df1[['Age', 'Monthly Income']]
df2 = pd.concat([df21, df13], axis=1)
print("Names of the all the columns used for classification in dataframe")
print(df21.columns)
# Here we print df2
# print("Below print the content of df2")
# print(df2)
print("Number of nearest neighbors k is")
a = 2
print(a)
neigh = KNeighborsClassifier(n_neighbors=a)
neigh.fit(df21,df13)
df31 = neigh.predict(df21);
# print("Below we print df31")
# print(df31)
df32 = pd.DataFrame(df31)
# print(df32)
# Then we need to compare value of df32 and df13
df_Test = pd.concat([df32, df13], axis=1)
df_Test.columns = ['Predicted', 'Real']
# print(df_Test)
df_Test['Result'] = np.where(df_Test['Predicted'] == df_Test['Real'], 1, 0)
# print(df_Test)
# int S = 0;
S = np.sum(df_Test['Result'], axis=0)
print("Accuracy of the k nearest neighbor classification is")
S1 = S/1991
print(S1)
# df33['que'] = np.where((df[''] >= df['two']) & (df['one'] <= df['three'])
#                     , df['one'], np.nan)
# Here we print df31
# print the second worksheet of the dataframe
# print(df2)

# 1991 rows * 12 columns
# 9999 rows * 7 columns