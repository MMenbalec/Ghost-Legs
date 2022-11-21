import sys
import math

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.
#ligne = [
#        ["A"," "," ","B"," "," ","C"," "," ","0  "],
#        ["|"," "," ","|"," "," ","|"," "," ","1  "],
#        ["|","-","-","|"," "," ","|"," "," ","2  "],
#        ["|"," "," ","|","-","-","|"," "," ","3  "],
#        ["|"," "," ","|","-","-","|"," "," ","4  "],
#        ["|"," "," ","|"," "," ","|"," "," ","5  "],
#        ["1"," "," ","2"," "," ","3"," "," ","6  "],
#        ]
ligne = [
        ["A  B  C "],
        ["|  |  | "],
        ["|--|  | "],
        ["|  |--| "],
        ["|  |--| "],
        ["|  |  | "],
        ["1  2  3 "],
        ]
#w, h = [int(i) for i in input().split()]
h = 7
w = 3
debutColonne = 0
positionColonne=0
for i in range(h):
    for line in ligne[i]:
        print(line)
        if i == 0:
            for j in range(w):
                print(" colonnes "+line[j+debutColonne]+" "+str(j))
                debutColonne += 2
            break
        if positionColonne < h:
            positionColonne +=1
            if line[positionColonne] == '  ':
                positionColonne -=1
                break
            if line[positionColonne] == '-':
                positionColonne += 2
                break
            if line[positionColonne-2] == '-':
                positionColonne -= 3
                break


    print("position",str(positionColonne)," ")
    
# Write an answer using print
# To debug: print("Debug messages...", file=sys.stderr, flush=True)

print("answer")
