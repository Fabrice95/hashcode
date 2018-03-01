#!/usr/bin/env python

import sys


lines = []
output = []

nR = 0
nC = 0
nF = 0
nN = 0
nB = 0
nT = 0

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
            lines.append( [int(n) for n in myfile.readline().split()] )
            
        print(lines)
        
        #lecture du output
        for i in range(nF):
            lines.append( [int(n) for n in myfile.readline().split()] )
        
        
        test()
    # Launch
    #fonction()
    #output()

    
    
	

def test ():
    global lines
     
	distance = 0    
	points = 0
    # code
    for i in range(nF) : #pour chaque voiture
		time = 0 # time au début	
		vx = 0 # position x
		vy = 0 # position y
		for ride in output[i]: # pour chaque course
			lineride = lines[ride]
			
			# temps pour arriver au lieu de départ
			distance = abs( lineride[0] - vx) + abs(lineride[1] - vy)
			time += distance
			
			distance = abs( lineride[0] - lineride[2]) + abs(lineride[1] - lineride[3])
			if time + distance > lineride[5]:
				print "ERREUR arrive trop tard voiture " + i + " course " + ride
				sys.exit(1)
			if time == lineride[4] :
				points += nB
			time += distance
			points +=distance
			
			vx = lineride[2]
			vy = lineride[3]
    
    print "Points obtenus" + points
    
        
def output():
    global videos
    #print
        
        
  
start()

  
start()
