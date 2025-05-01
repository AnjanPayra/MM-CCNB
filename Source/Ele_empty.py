# -*- coding: utf-8 -*-
"""
Created on Fri Sep 11 10:36:09 2020

@author: Anjan Payra
"""

file_output1 = open('D:\\remma\\New_ECC\\YDIP_GO.txt', 'w')
file_output2= open('D:\\remma\\New_ECC\\YDIP_Sub.txt', 'w')
file_input1 = open('D:\\remma\\New_ECC\\GO_SubCell.txt', 'r')
hold1 = file_input1.readlines()
for line2 in hold1:
    line2=line2.strip('\n')
    str2=line2.split('\t')
    if(len(str2[0])&len(str2[1])):
        file_output1.write(str2[0]+'||'+str2[1]+'\n')
    if(len(str2[0])&len(str2[2])):
        file_output2.write(str2[0]+'||'+str2[2]+'\n')
file_input1.close()
file_output1.close()     