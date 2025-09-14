#latihan kalkulator sederhana
print("="*30)
print("KALKULATOR SEDERHANA")
print("="*30)
#imput
angka_1 = float(input("masukkan angka 1:"))
operasi = input("masukkan operasi (+,-,x,/):")
angka_2 = float(input("masukkan angka 2:"))
#operasi
if operasi == "*" or operasi == "x": 
    hasil = angka_1*angka_2
    print(f"hasilnya yaitu {hasil}")
elif operasi == "+" :
    hasil = angka_1+angka_2
    print(f"hasilnya yaitu {hasil}")
elif operasi == "-" :
    hasil = angka_1 - angka_2
    print(f"hasilnya yaitu {hasil}")
elif operasi == "/" :
    hasil = angka_1 / angka_2
    print(f"hasilnya yaitu {hasil}")
else : print("lu ngapain woy!!!")
print("="*10+"selesai"+"="*10)
