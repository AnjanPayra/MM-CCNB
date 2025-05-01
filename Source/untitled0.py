# -*- coding: utf-8 -*-
"""
Created on Fri Dec 31 00:17:24 2021

@author: Anjan Payra
"""

import networkx as nx

G = nx.read_adjlist('D:\\remma\\New_ECC\\YHQ\\YHQ.txt', delimiter=',')
nx.write_adjlist(G,"D:\\remma\\Multi-level Support Mapping\\YHQ_CC.csv")
#nx.draw(G,with_labels=True)
