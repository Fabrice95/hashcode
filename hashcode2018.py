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
        
        
        #data = ['a'=0,'b'=0,'x','y','s','f'} for i in range(0,N)]
        for i in range(nN):
#			a, b, x, y, s, f = [int(n) for n in myfile.readline().split()]
#			lines.append(['a': a ,'b': b,'x':x,'y':y,'s':s,
            lines.append( [int(n) for n in myfile.readline().split()] )
            
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
    with open("out", "w") as out:
        for i in range(nF):
            out.write(`i`+" ")
            for e in #list_of_rides:
                out.write(`e`+" ")

        
        
  
start()
