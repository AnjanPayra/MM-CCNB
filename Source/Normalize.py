# -*- coding: utf-8 -*-
"""
Created on Sun Oct 24 00:22:17 2021

@author: Anjan Payra
"""

# apply the min-max scaling in Pandas using the .min() and .max() methods
def min_max_scaling(df):
    # copy the dataframe
    df_norm = df.copy()
    # apply min-max scaling
    for column in df_norm.columns:
        df_norm[column] = (df_norm[column] - df_norm[column].min()) / (df_norm[column].max() - df_norm[column].min())
        
    return df_norm



import pandas as pd 
#Obtain the dataset 
file_output1 = open('D:\\remma\\New_ECC\\ML\\Entire_data\\YDIP__ECC_CC_GO_SL_Nor.csv', 'w')

df = pd.read_csv("D:\\remma\\New_ECC\\ML\\Entire_data\\YDIP__ECC_CC_GO_SL.csv", sep=",")    
# call the min_max_scaling func
row, col = df.shape

min_max_scaling(df)

df_cars_normalized