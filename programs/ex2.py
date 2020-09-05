"""
Read the "churn.csv" data set and
perform the following tasks
1.what is the average monthly charge paid by a customer for the services he/she has signed up for?
2.The data type of the variable tenure from the churn dataframe is
expected output:
average: 62.4734817814
tenure Data type: object
"""
import numpy as np
import pandas as pd

data = pd.read_csv('churn.csv')
print(data.head())
print('average:', np.mean(data['MonthlyCharges']))
print('tenure Data type: ', data['tenure'].dtype)


