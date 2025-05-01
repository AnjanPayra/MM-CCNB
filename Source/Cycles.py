# -*- coding: utf-8 -*-
"""
Created on Sun Jan 31 19:58:13 2021

@author: Anjan Payra
"""

import networkx as nx

G = nx.read_adjlist('D:\\remma\\New_ECC\\YMBD\\YMBD.txt', delimiter=',')
nx.draw(G,with_labels=True)
n=list(G.nodes)
file_input1=open('D:\\remma\\New_ECC\\YMBD\\YMBD.txt','r')
file_output1=open('D:\\remma\\New_ECC\\YMBD\\YMBD_ECC_Pair.txt','w')
file_output2=open('D:\\remma\\New_ECC\\YMBD\\YMBD_Common_Pair.txt','w')
for line2 in file_input1:
    line2=line2.strip('\n')
    str2=line2.split(',')
    s1=''
    s1+=str2[0]
    s2=''
    s2+=str2[1]
    Mdegree=max(G.degree(s1),G.degree(s2))
    l=list(nx.common_neighbors(G, s1,s2))
    Ecc=len(l)/Mdegree
    print(line2,'|',l,'|',Ecc)
    file_output2.write(s1+'\t'+s2)
    for p in l:
        file_output2.write('\t'+p)
    file_output2.write('\n')
        
    file_output1.write(s1+'|'+s2+'|'+str(Ecc)+'\n')
    #file_output1.write(line2+'|'+str(l)+'|'+str(Ecc)+'\n')
file_output1.close()