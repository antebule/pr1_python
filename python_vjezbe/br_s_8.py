br_s_1_osmicom = 0
brojac = 0
for i in range(100,110):
    broj = i
    while (broj > 0):
        zn = broj%10
        if (zn == 8):
            brojac = brojac + 1
            print(brojac)
        broj = broj // 10
    if (brojac == 1):
        print(broj)
        br_s_1_osmicom = br_s_1_osmicom + 1
        brojac = 0

print(br_s_1_osmicom)
    
