rijec = input("Unesi neku rijec: ")
niz = []
while (rijec != 'kraj'):
    niz.append(rijec)
    rijec = input("Unesi neku rijec: ")

''' recenica = ''
for j in niz:
    recenica = recenica + ' ' + j
print(recenica) '''

for j in range(len(niz)):
    print(niz[j], end=' ')     #ispis niza kao recenicu

for i in range(len(niz)):
    print('Broj slova u ' + str(i+1) + '. rijeci: ' + str(len(niz[i])))
    
def palindromi():
    f = open("palindromi.txt", "w")
    for rijec in niz:
        if (rijec == rijec[::-1]):
            f.write(rijec)
    f.close()

palindromi()
