#!/usr/bin/env python

import sys


lines = []
output = []

#~ nR = 0
#~ nC = 0
#~ nF = 0
#~ nN = 0
#~ nB = 0
#~ nT = 0

def start():

    global nR, nC, nF, nN, nB, nT

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
        
        
    with open(sys.argv[2], "r") as myfile2:
        #lecture du output
        for i in range(nF):
            output.append( [int(n) for n in myfile2.readline().split()][1::] )
        print(output)
        
        print("")
        test()
    # Launch
    #fonction()
    #output()

    
    
	

def test ():
	global lines
	distance=0
	points = 0
	# code

	for i in range(nF): #pour chaque voiture
		time = 0 # time au début
		vx = 0 # position x
		vy = 0 # position y
		for ride in output[i]: # pour chaque course
			lineride = lines[ride]
			print(lineride)
			
			# temps pour arriver au lieu de départ
			distance = abs( lineride[0] - vx) + abs(lineride[1] - vy)
			time += distance
			
			if lineride[4] > time :
				time = lineride[4]
				points+= nB
			
			distance = abs( lineride[0] - lineride[2]) + abs(lineride[1] - lineride[3])
			if time + distance > lineride[5]:
				print ("ERREUR arrive trop tard voiture " +str(i) + " course " + str(ride))
				sys.exit(1)

			time += distance
			
			#print("voiture " + str(i) + " à la course " + str(ride) + " au temps " + str(time))
			points +=distance
			
			vx = lineride[2]
			vy = lineride[3]
	print ("Points obtenus " + str(points))
    
        
        
        
  
start()

  
