#!/usr/bin/env python

import sys


lines = []


def start():

    global grid_rows_R, grid_colums_C, vehicles_F, rides_N, bonus_B, steps_T

    # Check arguments 
    if (len(sys.argv) < 2):
        print("usage: {} <input file>".format(sys.argv[0]))
        sys.exit(1)

    # Open input file
    with open(sys.argv[1], "r") as myfile:
        nR, nC, nF, nN, nB, nT = [int(n) for n in myfile.readline().split()]

        for i in range(nN):
            lines.append(myfile.readline().split())
        print(lines)
    # Launch
    #fonction()
    #output()

    

def fonction ():
    global lines 

    # code
       
    
    
    
        
def output():
    global videos
    #print
        
        
  
start()
