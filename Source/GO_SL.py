# -*- coding: utf-8 -*-
"""
Created on Fri Sep 18 15:45:19 2020

@author: Anjan Payra
"""

#storing YDIP_common_nb.txt in dictionary
f1=open('D:\\remma\\New_ECC\\YMBD\\YMBD_Common_Pair.txt','r')
store1=f1.readlines()

d1={}

for i in store1:
    i=i.strip('\n')
    i=i.rstrip()
    hld1=i.split()
    pair=hld1[0]+','+hld1[1]
    neighbours=hld1[2:len(hld1)]
    d1[pair]=neighbours
    
#print(d1)

#storing YDIP_GO.txt in dictionary
f2=open('D:\\remma\\New_ECC\\YDIP_GO.txt','r')
store2=f2.readlines()

d2={}

for i in store2:
    go_mdf=[]
    i=i.strip('\n')
    i=i.rstrip()
    hld2=i.split('|')
    go=hld2[1].split(';')
    for j in go:
        j=j.strip()
        go_mdf.append(j)
    d2[hld2[0]]=go_mdf
    
#print(d2)

#storing YDIP_Sub.txt in dictionary
f3=open('D:\\remma\\New_ECC\\YDIP_Sub.txt','r')
store3=f3.readlines()

d3={}

for i in store3:
    i=i.strip('\n')
    i=i.rstrip()
    hld3=i.split('|',1)
    d3[hld3[0]]=hld3[1]
    
#print(d3)

#function to count go's of keys in d1 using d2
def fun1(k0,k1):
    total_occurence1=[]
    if k0 in d2.keys():
        total_occurence1.append(len(d2[k0]))
    if k1 in d2.keys():
        total_occurence1.append(len(d2[k1]))
    if len(total_occurence1)>0:
        return min(total_occurence1)
    else:
        return 0.0

#function to count go's of values of keys in d1 using d2
def fun2(v1):
    total_occurence2=[]
    for i in v1:
        if i in d2.keys():
            total_occurence2.append(d2[i])
    flat_list = [item for sublist in total_occurence2 for item in sublist]
    flat_list=list(set(flat_list))
    if len(flat_list)>0:
        return len(flat_list)
    else:
        return 0.0
    
#function to count go's of both key in d1 using d3
def fun3(k0):
    check=['Nucleus','Cytoplasm','Membrane','Golgi','Mitochondrion','Endoplasmic','Vacuole','Bud','cell wall','Peroxisome']
    count=0
    if k0 in d3.keys():
        for i in check:
            if i in d3[k0]:
                count+=1
    return count
    
#function to count go's of the neigbors(values) in d1 using d3
def fun4(v2):
    check=['Nucleus','Cytoplasm','Membrane','Golgi','Mitochondrion','Endoplasmic','Vacuole','Bud','cell wall','Peroxisome']
    count=0
    for i in v2:
        if i in d3.keys():
            for j in check:
                if j in d3[i]:
                    count+=1
    return count
    
    
def main():
    f4=open('D:\\remma\\New_ECC\\YMBD\\result1.txt','w')#for result1
    f5=open('D:\\remma\\New_ECC\\YMBD\\result2.txt','w')#for result2
    
    #part 1 passing keys as arguments in fun1() and values as arguments in fun2() from d1 using d2
    for k, v in d1.items(): 
        b=k.split(',')
        denominator=fun1(b[0],b[1])
        numerator=fun2(v)
        if denominator==0:
            t=str(k)+','+str(0.0)
            print(k,',',str(0.0))
            f4.writelines(t+'\n')
        else:
            result=numerator/denominator
            t=str(k)+','+str(result)
            print(k,',',str(result))
            f4.writelines(t+'\n')
    f4.close()
    
    #part 2 passing keys as arguments in fun1() and values as arguments in fun2() from d1 using d3
    for k, v in d1.items(): 
        b=k.split(',')
        denominator1=fun3(b[0])
        denominator2=fun3(b[1])
        #print(denominator1)
        #print(denominator2)
        denominator=denominator1*denominator2
        numerator=fun4(v)
        #print(numerator)
        if denominator==0:
            t=str(k)+','+str(0.0)
            print(k,',',str(0.0))
            f5.writelines(t+'\n')
        else:
            result=(numerator**2)/denominator
            t=str(k)+','+str(result)
            print(k,',',str(result))
            f5.writelines(t+'\n')
    f5.close()
         
main()