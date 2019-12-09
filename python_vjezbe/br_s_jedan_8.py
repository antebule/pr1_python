
for i in range(100,10000):
    brojac = 0
    br = i
    while br > 0:
        zn = br % 10
        if zn==8:
            brojac = brojac + 1
        br = br//10
    if brojac == 1:
        print(i)

