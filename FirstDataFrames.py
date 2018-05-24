#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import pandas as pd

customIndex = ["M", "T", "W", "Th", "F", "S", "Su" ]
#customColumns = ["A", "B", "C", "D", "E", "F", "G"]

data = {"day": ["M", "T", "W", "Th", "F", "S", "Su" ], 
        "sleep": [8, 9, 9, 7, 5, 10, 8],
        "work": [8, 8, 8, 7, 10, 8, 8],
        "fun time": [0, 1, 2, 3, 4, 5, 6]}

df = pd.DataFrame(data) #, index = customIndex)

#print(df)
#print()
#print(df.head(3))
#print()
#print(df.tail(2))

df.set_index(["day"], inplace = True)
print(df)
print()
print(df[["sleep", "work"]])