#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Mar  1 19:11:49 2018

@author: martin
"""

import sys

input_file_name = "b_should_be_easy.in"
#input_file_name = "a_example.in"
#input_file_name = "c_no_hurry.in"
#input_file_name = "d_metropolis.in"
#input_file_name = "e_high_bonus.in"

sys.argv = ["hashcode2018", input_file_name]
#from hashcode2018 import *

import hashcode2018 

lines, nR, nC, nF, nN, nB, nT = hashcode2018.start()

#add idx to end
lines2 = []
for i in range(len(lines)):
    tmp = lines[i]
    tmp.append(i)
    lines2.append(tmp)

lines2 = lines2[0:nN]
# sort by bonus, steps
sorted_lines = sorted(lines2, key = lambda x: (x[-3], x[-2]), reverse=True)

rides = {}
for i in range(nF):
    if i >= nN:
        break
    rides[i] = []

idx = 0
for i in range(len(sorted_lines)):
    if i >= nN:
        break
    if idx >= nF or idx >= nN:
        idx = 0
    rides[idx].append(sorted_lines[i][-1])
    idx += 1

print("===============")
for i in range(nF):
    print(len(rides[i]), " ".join(list(map(str, rides[i]))))

with open(sys.argv[1] + ".out", "w") as myfile:
    for i in range(nF):
        #print(len(rides[i]), " ".join(list(map(str, rides[i]))))
        res = str(len(rides[i])) +  " "+ " ".join(list(map(str, rides[i]))) + "\n"
        myfile.write(res)

    