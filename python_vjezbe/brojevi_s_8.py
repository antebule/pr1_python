dat = open("brojevi.txt", 'r')
brojac = 0
for broj in dat:
    for zn in broj:
        if zn == '8':
            brojac = brojac + 1
print(brojac)
dat.close()
