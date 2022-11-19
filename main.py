import sys
import math

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.
line = [["A"," "," ","B"," "," ","C"," "," ","0  "],
        ["|"," "," ","|"," "," ","|"," "," ","1  "],
        ["|","-","-","|"," "," ","|"," "," ","2  "],
        ["|"," "," ","|","-","-","|"," "," ","3  "],
        ["|"," "," ","|","-","-","|"," "," ","4  "],
        ["|"," "," ","|"," "," ","|"," "," ","5  "],
        ["1"," "," ","2"," "," ","3"," "," ","6  "],

w, h = [int(i) for i in input().split()]
for i in range(h):
    line = input()
    print("Debug messages...",line[4]," ", i, file=sys.stderr, flush=True)
    print("Debug messages...",line," ", i, file=sys.stderr, flush=True)
    
# Write an answer using print
# To debug: print("Debug messages...", file=sys.stderr, flush=True)

print("answer")
