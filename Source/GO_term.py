# -*- coding: utf-8 -*-
"""
Created on Wed Sep  9 16:54:15 2020

@author: Anjan Payra
"""

file_output1 = open('D:\\remma\\New_ECC\\YDIP_GO.txt', 'w')
file_input1 = open('D:\\remma\\New_ECC\\unique.txt', 'r')
hold1 = file_input1.readlines()
count=0
for line2 in hold1:
    line2=line2.strip('\n')
    count=count+1
    print(count)
    file_input2 = open('D:\\remma\\New_ECC\\Ent_GO.txt', 'r')
    for line1 in file_input2:
        line1=line1.strip('\n')
        str2=line1.split('||')
        
       # print(len(str2), "  ",count)
        if(line2==str2[0]):
            if(len(str2[1])):
                file_output1.write(line2+'|'+str2[1]+'\n')
                break
                   #else:
        #    file_output3.write(line2+'\n')
file_input1.close()
file_output1.close() 
          
 
file_output1 = open('D:\\remma\\New_ECC\\YDIP_Sub.txt', 'w')
file_input1 = open('D:\\remma\\New_ECC\\unique.txt', 'r')
hold1 = file_input1.readlines()
count=0
for line2 in hold1:
    line2=line2.strip('\n')
    count=count+1
    print(count)
    file_input2 = open('D:\\remma\\New_ECC\\Ent_Sub.txt', 'r')
    for line1 in file_input2:
        line1=line1.strip('\n')
        str2=line1.split('||')
        
       # print(len(str2), "  ",count)
        if(line2==str2[0]):
            if(len(str2[1])):
                file_output1.write(line2+'|'+str2[1]+'\n')
                break
                   #else:
        #    file_output3.write(line2+'\n')
file_input1.close()
file_output1.close()    