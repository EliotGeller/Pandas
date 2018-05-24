#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import pandas as pd
import numpy as np

data = {"Part 1": [1, 2, 3, 4, 1, 10],
        "Part 2": [5, 4, 3, 2, 4, 10],
        "Part 3": [1, 9, 2, 8, 1, 10],
        "Part 4": [1, 2, 3, 4, 1, 2],
        "NaN Part": [4, 3, np.nan, 1, 4, 3]}

newIndex = ["A", "B", "C", "D", "E", "F"]

df = pd.DataFrame(data, index = newIndex)

print(df)
print()


#print("Getting value: ", df.get_value("A", "Part 2"))
#print()
#
for index, series in df.iterrows():
    if int(series["Part 1"]) == int(1):
        df.drop(index, axis = 0, inplace = True)
        
print("After iteration:\n", df)
        
#print()
#
#print("Checking if there are any NaN values\n", df.isnull())
#print(df.notnull())
#print()
#
#df.dropna(1, thresh = 4, inplace = True)
#print(df)

#df.drop_duplicates(subset = ["NaN Part", "Part 4"], keep = "last", 
#                   inplace = False)
#
#df.drop(["A", "C", "D"], axis = 0, inplace = True)
#
#print(df)
#
