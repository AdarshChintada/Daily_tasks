# data preprocessing

import pandas as pd
import numpy as np

df = pd.read_excel("report.xlsx", header=None)

#preprocessing

#1.remove rows from header and tail

df.drop(df.head(6).index, inplace=True)
df.drop(df.tail(4).index, inplace=True)
# Replace empty cells with NaN
df.replace(" ", np.nan, inplace=True)

#2.remove empty columns and rows
df.dropna(how='all',axis=0,inplace=True)
df.dropna(how='all',axis=1,inplace=True)

#3.drop rows/columns based on threshold
df.dropna(axis='columns', thresh=2, inplace=True)

#4.Merging data from 1st column to the 0th column
df[0] = df[0].fillna(df[1])
df.drop(columns=1, inplace=True)
#print(df)
# 5.reset index
min_cells = 2   # minimum cells that contain data in each row
index_values = []
current_index = 1
# Loop 
for index, row in df.iterrows():
    if row.count() >= min_cells:
        index_values.append(current_index)
        current_index += 1
    else:
        current_index = 1
        index_values.append("S.No") #if there is one cell containing data, then considered it as heading for the upcoming data
#6.reset index
df.index=index_values
df.index.values[0] = '' #set the first row's index to an empty string


#highlight rows

# df.reset_index(drop=True, inplace=True)

# non_null = row.count()
# highlight = lambda row: ['background-color: red' if non_null < min_values_required else '' for _ in row]
# df.head(10).style.apply(highlight,axis=1)


# highlight_style = 'background-color: red'
# def highlight_row(row):
#     non_null_count = row.count()
#     if non_null_count < min_values_required:
#         return [highlight_style] * len(row)
# styled_df = df.style.apply(highlight_row, axis=1)
# styled_df


#7.Save DataFrame to a CSV file with no header
df.to_csv("output.csv", header=False)

