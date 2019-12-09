dat = open("rijeci.txt", 'r')
niz = []
br_ponavljanja = 0
najvise_ponavljanja = 0
najcesca_rijec = ''
for rijec in dat:
    niz.append(rijec[:-1])   # rijec[:-1] cita liniju do znaka \n

for rijec in niz:
    broj_ponavljanja = niz.count(rijec)
    if (broj_ponavljanja > najvise_ponavljanja and rijec != rijec[::-1]):     #rijec[::-1] rijec naopako
        najcesca_rijec = rijec
        najvise_ponavljanja = broj_ponavljanja

print(najcesca_rijec)
dat.close()
