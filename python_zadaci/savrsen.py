najveci = 0
for i in range(1,10000):
    suma = 0
    for j in range(1,i):
        if (i%j == 0):
            suma = suma + j
    if (suma == i):
        najveci = i
najmanja = najveci % 10
while(najveci > 0):
    zn = najveci % 10
    if (najmanja > zn):
        najmanja = zn
    najveci // 10
print (najmanja)
    
