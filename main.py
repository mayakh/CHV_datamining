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
from scipy import stats
import fileinput


def sort_patient_age(df1):
    # get patients birthdate
    age_list = list(df1['Age'])
    age = np.zeros(len(age_list))
    for j in range(len(age_list)):
        if "an" in age_list[j]:
            a_index = str(age_list[j]).index('a')
            age[j] = age_list[j][0:a_index-1]
        else:
            age[j] = 0

    # birthdate = np.zeros((len(df1[df1.columns[5]].values), 1))
    nind = np.zeros([9])
    # count number of age group occurrence
    for i in range(len(age)):
        if age[i]<10:
            nind[0] = nind[0]+1
        elif age[i]<20:
            nind[1] = nind[1]+1
        elif age[i]<30:
            nind[2] = nind[2]+1
        elif age[i] < 40:
            nind[3] = nind[3] + 1
        elif age[i] < 50:
            nind[4] = nind[4] + 1
        elif age[i] < 60:
            nind[5] = nind[5] + 1
        elif age[i] < 70:
            nind[6] = nind[6] + 1
        elif age[i] < 80:
            nind[7] = nind[7] + 1
        else:
            nind[8] = nind[8] + 1
    print(nind)


def sort_indications(df1):
    # Load a sheet into a DataFrame by name: df1
    #df1 = xl.parse('radio jan-juin18 - Copie')g
    indic = list(df1['Examen(s)'])
    # indic_u = list(np.unique(indic))
    # create a shortlist
    slist = ['Genou', 'Coude', 'Main', 'Poignet', 'Hanche', 'Pied', 'Jambe', 'Calcaneum', 'Cheville', 'Femur',
            'Rachis', 'Humerus', 'Bassin', 'Articulation', 'Avant-bras', 'scapulaire', 'Opn', 'Sternum',
            'segments du membre inf', 'segments du membre sup', 'Arthrographie', 'pulmonaire', 'paule']
    nind = np.zeros(len(slist))

    k = 0
    dpt = list(df1['UF   Demandeur'])
    # count number of indicated exam occurrence
    for i in range(len(indic)):
        if dpt[i] == '0991 URGENCES':
            k = k + 1
            fl = 0
            for j in range(len(slist)):
                if (slist[j] in indic[i]) and (fl == 0):
                    nind[j] = nind[j]+1
                    fl = 1

    print(k)
    print(slist)
    print(nind)

    # print(len(indic_u))
    # fig, ax = plt.subplots()
    # plt.bar(range(len(indic)), nind)
    # plt.ylabel('Number of occurrences')
    # plt.xticks(range(len(indic)))
    # plt.show()
    # fig.savefig('/Users/mayak./Documents/CHV_RIS/MSK/MSKindications.svg')   # save the figure to file
    # df2 = pd.DataFrame({'Indications': indic})
    # Create a Pandas Excel writer using XlsxWriter as the engine.
    # writer = pd.ExcelWriter('/Users/mayak./Documents/CHV_RIS/MSK/MSKindications.xlsx', engine='xlsxwriter')
    # Convert the dataframe to an XlsxWriter Excel object.
    # df2.to_excel(writer, sheet_name='Sheet1')
    # Close the Pandas Excel writer and output the Excel file.
    # writer.save()


def sort_patient_sex(df1):
    # get patients birthdate
    sex_list = list(df1['Sexe'])
    # print(sex_list.dtype)
    nind = np.zeros(2)
    for j in range(len(sex_list)):
        if sex_list[j] == 'M':
            nind[0] = nind[0]+1
        else:
            nind[1] = nind[1]+1
    print(nind)


def sort_rooms(df1):
    # get Xray room/scanner
    for i in range(len(df1.columns)):
        if df1.columns[i] == "Salle(s)":
            c_rooms = df1[df1.columns[i]].values
    rooms = np.unique(c_rooms.tolist())
    nroom = np.zeros(len(rooms))
    # count number of rooms  occurrence
    for i in range(len(c_rooms)):
        for j in rooms:
            if c_rooms[i] == j:
                nroom[rooms[j]] = nroom[rooms[j]]+1


def main():
    """Main"""
    # Assign spreadsheet filename to `file`
    filename_ = '/Users/mayak./Documents/CHV_RIS/MSK/msk_toutes_salle_radio_2017-2018.xlsx'

    # Load spreadsheet
    df1 = pd.read_excel(filename_)
    sort_indications(df1)
    # sort_patient_age(df1)
    # sort_rooms(df1)
    # sort_patient_sex(df1)
if __name__ == '__main__':
    main()
