# 1. First based on customer's income, select the most affordable goal amount 
# (the largest goal amount that less than the income)
# 2. Assume with the increase of the age, the customer's willing to 
# spend on eduction, hous, travel and car have some relationship with the income.
# Education, (100-age)% of income.
# Travel, (80-age)% of income, less than 0% assign 0%
# House, (1.5*age)% of income, more than 100% assign 100%
# Car, age% of income
# Based on the relationship and goal amount above, we can decide the goal amount that we can fill in

from pandas import DataFrame, read_csv
import matplotlib.pyplot as plt
import pandas as pd
import csv
import numpy as np

xl = pd.ExcelFile('Fintech.xlsx')
# Then print the names of all the sheets.
print("Names of the all the sheets in the excelfile")
print(xl.sheet_names)

# df1 = xl.parse("Cust List Qn 2")
df2 = xl.parse("Cust List Qn 3")

# print the second worksheet of the dataframe
# print(df2)
print("All the data types of the file")
print(df2.dtypes);

# Create new columns indicate if corresponding goal amount is less than income
df2['Education_status'] = np.where(df2['Education Goal Amount'] <= df2['Income'], 1, 0)
df2['House_status'] = np.where(df2['House Goal Amount'] <= df2['Income'], 1, 0)
df2['Travel_status'] = np.where(df2['Travel Goal Amount'] <= df2['Income'], 1, 0)
df2['Car_status'] = np.where(df2['Car Goal Amount'] <= df2['Income'], 1, 0)

# print(df2)

# Set the real 
df2['Education_Goal'] = np.where(df2['Education_status'] == 1, df2['Education Goal Amount'], 0)
df2['House_Goal'] = np.where(df2['House_status'] == 1, df2['House Goal Amount'], 0)
df2['Travel_Goal'] = np.where(df2['Travel_status'] == 1, df2['Travel Goal Amount'], 0)
df2['Car_Goal'] = np.where(df2['Car_status'] == 1, df2['Car Goal Amount'], 0)
# frame['Recom'] = frame[['test1','test2','test3']].max(axis=1)

df21 = df2[['Education_Goal', 'House_Goal', 'Travel_Goal', 'Car_Goal']]

df31 = df21.idxmax(axis=1)

df3 = pd.concat([df2['Cust ID'], df31], axis=1)

df3.columns = ['Cust ID', 'Recommended Goal']
# print("Custom ID and corresponding recommended goal")
# print(df3);

# Create new dataframe
df4 = pd.concat([df2[['Age', 'Income']],df31], axis=1)
# Print the column names we need to print
df4.columns = ['Age','Income','Recommended Goal']
# print("Age, Income and corresponding recommended goal")
# print(df4.columns)

# Based on Age and Income, calculate the Goal Amount.
df4['Goal_Amount'] = np.where(df4['Recommended Goal'] == 'House_Goal', 1.5*df4['Age']/100*df4['Income'], 0)
df4['Goal_Amount'] = np.where(df4['Recommended Goal'] == 'Education_Goal', (100-df4['Age'])/100*df4['Income'], df4['Goal_Amount'])
df4['Goal_Amount'] = np.where(df4['Recommended Goal'] == 'Travel_Goal', (80-df4['Age'])/100*df4['Income'], df4['Goal_Amount'])
df4['Goal_Amount'] = np.where(df4['Recommended Goal'] == 'Travel_Goal', df4['Age']/100*df4['Income'], df4['Goal_Amount'])

# In case sometimes Goal Amount is less than 0 and sometimes Goal Amount is more than Income.
df4['Goal_Amount'] = np.where(df4['Goal_Amount'] < 0, 0, df4['Goal_Amount'])
df4['Goal_Amount'] = np.where(df4['Goal_Amount'] > df4['Income'], df4['Income'], df4['Goal_Amount'])

print("Age, Income, Corresponding recommended goal and Goal amount")
print(df4.columns)
print(df4)
# print(df4)

#for index, row in df2.iterrows():
#	if()
#	temp = row['Education Goal Amount']
#	if (temp < row[''])
#		df2[] 
#  ....:     print row['c1'], row['c2']