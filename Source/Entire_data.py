# -*- coding: utf-8 -*-
"""
Created on Wed Nov 11 20:45:21 2020

@author: Anjan Payra
"""

file_output1 = open('D:\\remma\\New_ECC\\ML\\Entire_data\\YMBD__ECC_CC_GO_SL.csv', 'w')
file_input1 = open('D:\\remma\\New_ECC\\YMBD\\unique.txt', 'r')
hold1 = file_input1.readlines()
for line2 in hold1:
    line2=line2.strip('\n')
    
           
    file_input2 = open('D:\\remma\\New_ECC\\YMBD\\YMBD_ECC_final.csv', 'r')
    for line1 in file_input2:
        line1=line1.strip('\n')
        str2=line1.split(',')        
        if(line2==str2[0]):
           file_output1.write(line1+',')
           
    file_input2 = open('D:\\remma\\New_ECC\\ML\\Clustering Coefficient\\YMBD_CC.csv', 'r')
    for line1 in file_input2:
        line1=line1.strip('\n')
        str2=line1.split(',')        
        if(line2==str2[0]):
           file_output1.write(str2[1]+',')
           
    file_input2 = open('D:\\remma\\New_ECC\\YMBD\\YMBD_GO_final.csv', 'r')
    for line1 in file_input2:
        line1=line1.strip('\n')
        str2=line1.split(',')        
        if(line2==str2[0]):
           file_output1.write(str2[1]+',')
           
    file_input2 = open('D:\\remma\\New_ECC\\YMBD\\YMBD_Subcell_final.csv', 'r')
    for line1 in file_input2:
        line1=line1.strip('\n')
        str2=line1.split(',')        
        if(line2==str2[0]):
           file_output1.write(str2[1]+'\n')
    
file_input1.close()
file_output1.close()