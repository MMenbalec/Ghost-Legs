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
nomColonne = []
resultColonne = []

positionColonne=0
for i in range(h):
    for line in ligne[i]:
        #print(line)
        if i == 0:
            debutColonne = 0
            for j in range(w):
                nomColonne.append(line[j+debutColonne])
                debutColonne += 2
            break
        if i == h:
            debutColonne = 0
            for j in range(w):
                resultColonne.append(line[j+debutColonne])
                debutColonne += 2
            break
        if positionColonne < h:
            if line[positionColonne+1] == '  ':
                break
            if line[positionColonne+1] == '-':
                positionColonne += 3
                print(line)
                print(line[positionColonne])
                break
            if positionColonne > 0:
                if line[positionColonne-1] == '-':
                    positionColonne -= 3
                    print(line[positionColonne])
                    break

    print(nomColonne)
    print(resultColonne)
    print(positionColonne)
    #print("position",nomColonne[positionColonne-1]+resultColonne[positionColonne-1])
    
# Write an answer using print
# To debug: print("Debug messages...", file=sys.stderr, flush=True)

print("answer")
