niz = []
for i in range(5):
        n = 0
        while (n<3 or n > 500):
                n = int(input("Unesi neki broj "))
        niz.append(n);

def najveciprosti(niz):
    najveci = 0
    for broj in niz:
        prosti = 1
        for i in range(2,broj):
            if (broj%i == 0):
                prosti = 0
                break
        if prosti:
            while(broj > 0):
                zn = broj % 10
                if (najveci < zn):
                    najveci = zn
                broj = broj // 10
    print(najveci)
    
