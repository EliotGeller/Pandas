#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import pandas as pd

data = {"Val1": [1, 2, 5, 3, 4],
        "Val2": [1, 2, 3, 4, 5],
        "Val3": [7, 9, 6, 2, 3]}

df = pd.DataFrame(data)

df.sort_values(0, axis = 1, ascending = False, inplace = True,
               kind = "quicksort", na_position = "last")

df.sort_index(axis = 1, inplace = True)

#print(df)
#print()

df = df.set_value(index = 3, col = "Val2", value = 5)

#print(df)
#print()

newData = [9, 8, 7, 6, 5]
df["Val4"] = newData

#print(df)
#print()

dataUpdate = {"Val5": [1, 9, 2, 8, 3]}
#df = df.append([dataUpdate], ignore_index = True)

#df.sort_values("Val5", axis = 0, ascending = False, inplace = True,
#               kind = "quicksort", na_position = "last")

df = df.add(2)
dfFinal = pd.concat([df, df])
print(dfFinal)
print()