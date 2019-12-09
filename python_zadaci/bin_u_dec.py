digits = []
br = 0
dec = 0

while(br == 0 or br==1):
    br = int(input("Unesi binarnu znamenku: "))
    digits.append(br)

digits.pop()
pos = len(digits)-1
for i in digits:
    print(i, end="")
    dec += i * pow(2,pos)
    pos -= 1

print(" U decimalnom je: ", dec)
