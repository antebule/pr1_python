niz = []
n = -1
brojac = 0
suma = 0
uneseni = 0
while (n != 0 and n%7 != 0):
    n = int(input("Unesi prirodan broj "))
    niz.append(n)
    suma = suma + n
    uneseni = uneseni + 1
    for i in range(2,n):
        if (n%i == 0):
            brojac = brojac + 1
            break
print (brojac)

f = open("brojevi.txt", 'w')
for i in range(len(niz)):
    if (niz[i] > (suma/uneseni)):
        f.write(str(niz[i]))
f.close()
        

