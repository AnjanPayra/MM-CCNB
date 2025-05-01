# -*- coding: utf-8 -*-
"""
Created on Sat Oct 23 11:59:14 2021

@author: Anjan Payra
"""

import networkx as nx

G = nx.read_adjlist('D:\\remma\\New_ECC\\YHQ\\YHQ.txt', delimiter=',')
file_output1=open('D:\\remma\\New_ECC\\ML\\YHQ_CC.csv','w')
#nx.draw(G,with_labels=True)
c=nx.clustering(G)
#type(c)
for key, value in c.items(): 
        file_output1.write('%s,%s\n' % (key, value))
file_output1.close()
