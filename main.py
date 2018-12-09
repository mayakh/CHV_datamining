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
indic = np.unique(df1.Examens).tolist()
nind = np.zeros(len(indic))
print(indic[0])
print(nind)
for i in range(len(df1.Examens)):
    if df1.Examens[i]==indic[0]:
        nind[0] = nind[0]+1
    elif df1.Examens[i]==indic[1]:
        nind[1] = nind[1]+1
    elif df1.Examens[i]==indic[2]:
        nind[2] = nind[2]+1
    elif df1.Examens[i]==indic[3]:
        nind[3] = nind[3]+1
    elif df1.Examens[i]==indic[4]:
        nind[4] = nind[4]+1
    elif df1.Examens[i]==indic[5]:
        nind[5] = nind[5]+1
    elif df1.Examens[i]==indic[6]:
        nind[6] = nind[6]+1
print(indic)
print(nind)

plt.bar(range(len(indic)), nind)
plt.ylabel('Number of exams')
plt.show()


# df1['Examens'] = df1.Examens.astype(str)
# np.zeros(len(df1.Patient))

