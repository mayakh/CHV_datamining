import numpy as np
import os
import glob
import matplotlib as mpl
from matplotlib import pyplot as plt
import nibabel as nib
import pandas as pd
from sklearn import datasets, linear_model
from sklearn.metrics import mean_squared_error, r2_score
import statsmodels.api as sm
from scipy import stats

# Assign spreadsheet filename to `file`
filename_ = '/Users/mayakhalife/Documents/CHV_RIS/radiojan-juin18.xlsx'


# Load spreadsheet
df1 = pd.read_excel(filename_, dtype={'Name': str, 'Value': str}, skiprows=[0, 1, 2])
# Load a sheet into a DataFrame by name: df1
#df1 = xl.parse('radio jan-juin18 - Copie')
print(df1.columns)
print(df1.Examens)
# df1['Examens'] = df1.Examens.astype(str)
# np.zeros(len(df1.Patient))

