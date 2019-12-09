def trz_umn_np():
      brojac = 0
      for i in range(100,1000):
            zn1 = i // 100
            zn2 = (i // 10) % 10
            zn3 = i % 10
            if ((zn1 * zn2 * zn3) % 2 != 0):
                  brojac = brojac + 1
      print(brojac)
