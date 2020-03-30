#Simple usage of pandas to read flat files

import pandas as pd 

#read csv
print("All records in CSV")
print("------------------")
richest = pd.read_csv("richest_people_on_earth.csv")
print(richest.head())

#read tsv - tab separated file
print("All records in TSV")
print("------------------")
richest_tsv = pd.read_csv("richest_people_on_earth.tsv", sep="\t")
print(richest_tsv.head())

#read only specific columns from the CSV
print("Only 3 columns - Name, Country, Org Name from all records")
print("----------------------------------------------------------")
cols = ['Name', 'Country', 'Org Name']
richest_cols = pd.read_csv("richest_people_on_earth.csv", usecols=cols)
print(richest_cols)

#read only first 3 rows from CSV
print("Print only 3 rows")
print("-----------------")
richest_top3 = pd.read_csv("richest_people_on_earth.csv", nrows=3, skiprows=1, header=None)
print(richest_top3)

#Skip 2 rows and read the rest
print("Skip first 2 rows and print the rest")
print("------------------------------------")
richest_skip2 = pd.read_csv("richest_people_on_earth.csv", nrows=3, skiprows=2)
print(richest_skip2)

#Data types in the dataframe
print("Print data types in the dataframe")
print("---------------------------------")
print(richest.dtypes)

#Set the contact number column to string
print("Set the contact number as string data type")
print("------------------------------------------")
data_types = {'Contact number':'object'}
richest_new_dt = pd.read_csv("richest_people_on_earth.csv", dtype=data_types)
print(richest_new_dt.dtypes)

#Fill the missing vales of Contact number with null
print("Fill the missing vales of Contact number with null")
print("--------------------------------------------------")
null_values = {'Contact number':'0'}
richest_fill_na = pd.read_csv("richest_people_on_earth.csv", na_values=null_values, dtype=data_types)
print(richest_fill_na)
