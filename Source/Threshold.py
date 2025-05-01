# -*- coding: utf-8 -*-
"""
Created on Sat Sep 19 00:52:27 2020

@author: Anjan Payra
"""

# computation of node weight threshold k=1,2,3 for low, medium and high

import statistics
import math

file_input1 = open('D:\\remma\\New_ECC\\Common_Final\\YDIP_ESS_GO_SL_Final_100.csv', 'r')
weight_proteins = file_input1.readlines()
file_output1 = open('D:\\remma\\New_ECC\\Common_Final\\YDIP_ESS_GO_SL_thresholds.txt', 'w')
weight = []
for line in weight_proteins:
    store = line.split(',')
    weight.append(float(store[1]))
arthmtc_mean = statistics.mean(weight)
stndrd_dev = statistics.stdev(weight)
print(arthmtc_mean)
print(stndrd_dev)
# k=1
low_thrshld = arthmtc_mean + (1 * stndrd_dev * (1 - (1 / (1 + math.pow(stndrd_dev, 2)))))
file_output1.write('low threshold' + '|' + str(low_thrshld) + '\n')
# k=2
medium_thrshld = arthmtc_mean + (2 * stndrd_dev * (1 - (1 / (1 + math.pow(stndrd_dev, 2)))))
file_output1.write('medium threshold' + '|' + str(medium_thrshld) + '\n')
# k=3
high_thrshld = arthmtc_mean + (3 * stndrd_dev * (1 - (1 / (1 + math.pow(stndrd_dev, 2)))))
file_output1.write('high threshold' + "|" + str(high_thrshld) + '\n')
# computation of edge weight threshold k=1,2,3 for low, medium and high
file_output1.close()

