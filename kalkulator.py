import os

def header():
    '''Fungsi Header'''
    os.system("cls")
    print(f"{'PROGRAM MENGHITUNG LUAS DAN KELILING PERSEGI PANJANG':^40}")
    print(f"{'DAN KELILING PERSEGI PANJANG':^40}")
    print(f"{"-"*40:^40}")
def opsi():
    '''Fungsi Opsi'''
    print("1. Hitung Luas")
    print("2. Hitung Keliling")
    print("3. Hitung Luas dan Keliling")
    pilihan =input("Masukkan pilihan anda (1-3) :")
    return pilihan

def inputUser():
    '''Fungsi Input User'''
    lebar =int(input("Masukkan nilai lebar :"))
    panjang =int(input("Masukkan nilai panjang :"))
    return lebar,panjang

def hitungLuas(lebar,panjang):
    '''Fungsi perhitungan Luas'''
    return lebar*panjang

def hitungKeliling(lebar,panjang):
    '''Fungsi perhitungan Keliling'''
    return 2*(lebar+panjang)
def display(message,value):
    '''Fungsi menampilkan hasil'''
    print(f"Hasil perhitungan {message}= {value}")

#Program utama

while True:
    header()
    pilihan =opsi()
    if pilihan == "1":
        PANJANG,LEBAR = inputUser()
        LUAS= hitungLuas(LEBAR,PANJANG)
        display("Luas ",LUAS)

    elif pilihan == "2":
        PANJANG,LEBAR = inputUser()
        KELILING = hitungKeliling(LEBAR,PANJANG)
        display("Keliling ",KELILING)

    elif pilihan == "3":
        LEBAR,PANJANG = inputUser()
        LUAS= hitungLuas(LEBAR,PANJANG)
        KELILING = hitungKeliling(LEBAR,PANJANG)
        display("Luas ",LUAS)
        display("Keliling ",KELILING)
    else:
        print("Pilihan tidak tersedia")
    isContinue =input("Apakah lanjut(y/n)?")
    if isContinue == "n":
        break

print("program telah selesai")
