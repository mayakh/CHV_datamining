import numpy as np
import os
import glob
import matplotlib as mpl
from matplotlib import pyplot as plt
import nibabel as nib
import pandas as pd
import xlsxwriter as xlwt
import openpyxl
from sklearn import datasets, linear_model
from sklearn.metrics import mean_squared_error, r2_score
import statsmodels.api as sm
from scipy import stats



def sort_indications(df1):
    # Load a sheet into a DataFrame by name: df1
    #df1 = xl.parse('radio jan-juin18 - Copie')
    indic = np.unique(df1.Examens).tolist()
    nind = np.zeros(len(indic))
    # count number of indicated exam occurrence
    for i in range(len(df1.Examens)):
        for j in indic:
            if df1.Examens[i] == j:
                nind[indic.index(j)] = nind[indic.index(j)]+1
    fig, ax = plt.subplots()
    plt.bar(range(len(indic)), nind)
    plt.ylabel('Number of occurrences')
    plt.xticks(range(len(indic)))
    plt.show()
    fig.savefig('/Users/mayakhalife/Documents/CHV_RIS/MSKindications.svg')   # save the figure to file
    df2 = pd.DataFrame({'Indications': indic})
    # Create a Pandas Excel writer using XlsxWriter as the engine.
    writer = pd.ExcelWriter('/Users/mayakhalife/Documents/CHV_RIS/MSKindications.xlsx', engine='xlsxwriter')
    # Convert the dataframe to an XlsxWriter Excel object.
    df2.to_excel(writer, sheet_name='Sheet1')
    # Close the Pandas Excel writer and output the Excel file.
    writer.save()

def sort_patient_age(df1):
    # get patients birthdate
    birthdate = np.zeros((len(df1[df1.columns[5]].values), 1))
    for i in range(len(df1[df1.columns[5]].values)):
        bd = df1[df1.columns[5]].values[i]
        bd = pd.to_datetime(bd)
        birthdate[i] = 2018 - bd.year
    fig, ax = plt.subplots()
    plt.bar(range(len(df1[df1.columns[5]].values)), birthdate)
    plt.ylabel('Number of occurrences')
    plt.show()

def sort_patient_age(df1):
    # get Xray room/scanner
    rooms = np.unique(df1.Salles).tolist()
    nroom = np.zeros(len(rooms))
    # count number of rooms  occurrence
    for i in range(len(df1.Salles)):
        for j in rooms:
            if df1.Salles[i] == j:
                nroom[rooms.index(j)] = nroom[rooms.index(j)]+1
    print(nroom)

def main():
    """Main"""
    # Assign spreadsheet filename to `file`
    filename_ = '/Users/mayakhalife/Documents/CHV_RIS/radiojan-juin18.xlsx'

    # Load spreadsheet
    df1 = pd.read_excel(filename_, dtype={'Name': str, 'Value': str}, skiprows=[0, 1, 2])
    # sort_indications(df1)
    # sort_patient_age(df1)
    sort_patient_age(df1)

if __name__ == '__main__':
    main()