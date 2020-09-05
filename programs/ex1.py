"""
Use the dataset named "People Charm case.csv" that deals with HR analytics
perform the following tasks
1.What is the third quartile value for the variable "lastEvaluvation"
2.Construct a crosstable for the variables 'dept' and "salary" and display them
3.find out highest frequency value in the category low salary
expected output=
0.87
salary       high   low  medium
dept
IT             83   609     535
RandD          51   364     372
accounting     74   358     335
hr             45   335     359
management    225   180     225
marketing      80   402     376
product_mng    68   451     383
sales         269  2099    1772
support       141  1146     942
technical     201  1372    1147
higest frequency: 2099

"""
import pandas as pd
import numpy as np

data = pd.read_csv('People Charm case.csv')
print(np.percentile(data['lastEvaluation'], 75))
a = pd.crosstab(columns=data['salary'], index=data["dept"])
print(a)
print('higest frequency: ', max(a['low']))