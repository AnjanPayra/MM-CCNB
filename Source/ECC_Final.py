# -*- coding: utf-8 -*-
"""
Created on Fri Sep 18 06:43:21 2020

@author: Anjan Payra
"""

file_output1 = open('D:\\remma\\New_ECC\\YMBD\\YMBD_ECC_final.csv', 'w')
file_input1 = open('D:\\remma\\New_ECC\\YMBD\\unique.txt', 'r')
hold1 = file_input1.readlines()
count=0
for line2 in hold1:
    line2=line2.strip('\n')
    sum=0.0
    file_input2 = open('D:\\remma\\New_ECC\\YMBD\\YMBD_ECC_Pair.txt', 'r')
    for line1 in file_input2:
        line1=line1.strip('\n')
        str2=line1.split('|')        
        if(line2==str2[0]):
            sum=sum+float(str2[2])
        if(line2==str2[1]):
            sum=sum+float(str2[2])
        
    
    
    file_output1.write(line2+','+str(sum)+'\n')
                
                   #else:
        #    file_output3.write(line2+'\n')
file_input1.close()
file_output1.close()    