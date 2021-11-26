#!/usr/bin/python

#this python utility script creates a supercell from a given set of atomic coords
#NOTE: will only extend in the positive axes directions (no negatives)

import sys


#define arguments
if len(sys.argv) != 5:
    print("ERROR: Incorrect number of arguments.", file=sys.stderr)
    print("Use the following format:", file=sys.stderr)
    print("     supercell.py input_file a b c ", file=sys.stderr)
    sys.exit(2)

a, b, c = sys.argv[2:5] #the number of times to multiply cell by in each axis
a = int(a)
b = int(b)
c = int(c)
input_file = sys.argv[1] #the filename to read for atom coords


# atomic coord data should be formatted like this
# currently only crystal coords supported, will provide functionality for angstrom sometime
'''
ATOMIC_POSITIONS {crystal}
Au       0.0000000000      0.0000000000      0.0000000000                 
Au       0.0000000000      0.5000000000      0.5000000000                 
Au       0.5000000000      0.0000000000      0.5000000000                 
Au       0.5000000000      0.5000000000      0.0000000000
'''

data = "" 

with open(input_file, "r") as f:
    for i, line in enumerate(f.readlines()):
        #NOTE: i will start with 0 though linenumbers will start with 1!
        if i == 0: 
            if line.find("{") > -1: #check if header
                    #for now, skip header line
                    continue
        
        atom, x, y, z = line.split()
        x = float(x)
        y = float(y)
        z = float(z)
        
        for na in range(a):
            for nb in range(b):
                for nc in range(c):
                    #space delimited format
                    data += f"{atom} {(x + na)/a} {(y + nb)/b} {(z + nc)/c} \n"

#we'll be printing to stdout, user can decide if they want to redirect to file
print(data)