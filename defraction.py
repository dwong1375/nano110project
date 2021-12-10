#!/usr/bin/python

#this python utility script turns fractional coords into angstroms

import sys


#define arguments
if len(sys.argv) != 5:
    print("ERROR: Incorrect number of arguments.", file=sys.stderr)
    print("Use the following format:", file=sys.stderr)
    print("     defraction.py input_file a b c ", file=sys.stderr)
    sys.exit(2)
    
a, b, c = sys.argv[2:5] #the cell dimensions
a = float(a)
b = float(b)
c = float(c)
input_file = sys.argv[1] #the filename to read for atom coords


# atomic coord data should be formatted like this
'''
Au       0.0000000000      0.0000000000      0.0000000000                 
Au       0.0000000000      0.5000000000      0.5000000000                 
Au       0.5000000000      0.0000000000      0.5000000000                 
Au       0.5000000000      0.5000000000      0.0000000000
'''

data = "" 

with open(input_file, "r") as f:
    for i, line in enumerate(f.readlines()):
        try:
            atom, x, y, z = line.split()
        except ValueError:
            continue
        x = float(x)
        y = float(y)
        z = float(z)

        data += f"{atom} {x*a:.6f} {y*b:.6f} {z*c:.6f} \n"

#we'll be printing to stdout, user can decide if they want to redirect to file
print(data)
