#Simple usage of pandas to read flat files

import pandas as pd 

#read csv
richest = pd.read_csv("richest_people_on_earth.csv")
print(richest.head())

#read tsv - tab separated file
richest_tsv = pd.read_csv("richest_people_on_earth.tsv", sep="\t")
print(richest_tsv.head())

#read only specific columns from the CSV
cols = ['Name', 'Country', 'Org Name']
richest_cols = pd.read_csv("richest_people_on_earth.csv", usecols=cols)
print(richest_cols)

#read only first 3 rows from CSV
richest_top3 = pd.read_csv("richest_people_on_earth.csv", nrows=3, skiprows=1, header=None)
print(richest_top3)

#Skip 2 rows and read the rest
richest_skip2 = pd.read_csv("richest_people_on_earth.csv", nrows=3, skiprows=2)
print(richest_skip2)