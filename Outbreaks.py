#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import pandas as pd
#import matplotlib.pyplot as plt

df = pd.read_csv("outbreaks.csv", 
                 usecols = ["Year", "Month", "Hospitalizations"],
                 index_col = None)

print(df.head(10))
print()
print(df.tail())
print()

print("Number of rows of data: ", len(df))
print()

print("Number of missing data:\n", df.isnull().sum())
print()

print("Number of missing data points, for individual column:\n",
      df.isnull()["Hospitalizations"].sum())

print()
print(df.describe())
print()
df = df.dropna()
print(len(df))

df = df.sort_values("Hospitalizations", ascending = False)
print()
print("Printing new head:\n", df.head(10))

print()
print("Hospitalizations > 0:\n")
print(df[df.Hospitalizations > 0])
print()

df2 = df[df.Hospitalizations > 0]
print(len(df2))
print()

print (df.head())
print()
print(df['Year'].value_counts())
print("Counting value occurances:\n", df['Year'].value_counts().sum())
print("Length of df:\n", len(df))
print()

print(df2['Year'].value_counts())
print("Counting value occurances df2:\n", df2['Year'].value_counts().sum())
print("Length of df2:\n", len(df2))
print()

yearlyData = df2.loc[df2['Year'] == 2006]
print(yearlyData)
print(yearlyData['Year'].value_counts())
print()
months = df2['Month'].unique()
print()

print("Monthly occurances for df:\n",
      df["Month"].value_counts())
print()
print("Monthly occurances for df2:\n",
      df2["Month"].value_counts())
print()

years = df2["Year"].unique()
years.sort()
#print(years)

#for year in years:
#    print()
#    print(year)
#    currentYearData = df2.loc[df2["Year"] == year]
#    print(currentYearData["Month"].value_counts())
#    print()
    
print()
print(df2.describe(percentiles = [0.2, 0.4, 0.6, 0.8, 0.9, 0.95]))
#fig = plt.figure()
#ax1 = plt.subplot(211)
#ax2 = plt.subplot(212)
print()

df2.hist(column = "Hospitalizations", bins = 100, grid = False,
         xlabelsize = 10, xrot = 45, ylabelsize = 15, by = "Month",
         figsize = (15, 10)) #, ax = ax1)
#df.hist(column = "Year", bins = len(years), grid = False,
#         xlabelsize = 15, xrot = 45, ylabelsize = 15, ax = ax2)
#plt.show()
