#Simple usage of pandas to read flat files

import pandas as pd 

#read csv
richest = pd.read_csv("richest_people_on_earth.csv")
print(richest.head())

#read tsv - tab separated file
richest_tsv = pd.read_csv("richest_people_on_earth.tsv", sep="\t")
print(richest_tsv.head())