dat = open("brojevi.txt", 'r')
niz = []
suma = 0
brojac = 0
brojmanjih = 0
for linija in dat:
    broj = int(linija)
    niz.append(broj)
    brojac = brojac + 1
    suma = suma + broj

aritsr = suma / brojac
print('Aritmeticka sredina: ' + str(aritsr))

for i in niz:
    if i < aritsr:
        brojmanjih = brojmanjih + 1
        
print('Broj manjih od aritmeticke sredine: ' + str(brojmanjih))
dat.close()
