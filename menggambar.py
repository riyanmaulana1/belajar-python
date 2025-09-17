#latihan perulangan menggambar segitiga
sisi = int(input("masukkan panjang sisi"))
lbr = 1
#for in
print("="*10+"FOR IN"+"="*5)
for i in range(sisi):
    print("*"*lbr)
    lbr +=1

#while
#1
print("="*10+"WHILE"+"="*5)
lbr = 1
while True:
    print("*"*lbr)
    lbr +=1
    if lbr>sisi :
        break
#2 menampilkan yang ganjil saja
print("="*10+"WHILE"+"="*5)
lbr = 1
while True:
    if lbr%2:
        print("*"*lbr)
        lbr +=1
    else :
        lbr +=1
        continue
        
    if lbr>sisi :
        break
#3 segitiga sama kaki
print("="*10+"WHILE"+"="*5)
lbr = 1
spasi = sisi//2
while True:
    if lbr%2:
        print(spasi*" "+"*"*lbr)
        lbr +=1
        spasi -=1

    else :
        lbr +=1
        continue
        
    if lbr>sisi :
        break
#belah ketupat

print("="*10+"WHILE"+"="*5)
lbr = 1
spasi = sisi//2
while True:
    if lbr%2:
        print(spasi*" "+"*"*lbr)
        lbr +=1
        spasi -=1

    else :
        lbr +=1
        continue
    if spasi ==0:
       break
lbr-=2
spasi+=2
while True :
    if lbr%2:
        print(spasi*" "+"*"*lbr)
        lbr -=1
        spasi += 1
    else :
        lbr -=1
        continue
    if lbr == 0:
        break
