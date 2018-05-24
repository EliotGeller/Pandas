#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import pandas as pd

df = pd.read_csv("outbreaks.csv", index_col = False)
print(df.head())

print()
print(df.columns)

print()
print(df.isnull().sum())

#print()
#print(df["State"])

print()
print(df.describe())

print()
print(df["State"].value_counts())

#print()
#print(df["Location"].value_counts())

print()
print(df["Food"].value_counts())

print()
print(df["Fatalities"].value_counts())

print()
fatalityDF = df.loc[df["Fatalities"] > 0]
print(fatalityDF.head())

print()
print(fatalityDF["Location"].value_counts())

#print()
#fatalityDF.hist(column = "Fatalities", by = "Month",
#                figsize = (15, 10),
#                bins = int(max(fatalityDF["Fatalities"])))

print()
stateWise = df.loc[df["State"] == "California"]
print(stateWise["Food"].value_counts()) 

print()
locationWise = df.loc[df["Location"] == "Restaurant"]
print(locationWise["State"].value_counts())

print()
hospWise = df.loc[df["Hospitalizations"] > 0]
print(hospWise["State"].value_counts())

print()
print(locationWise["Food"].value_counts())