#data dictionary
import datetime
import os
import string
import random
mahasiswa_template ={
    'nama': 'nama',
    'nim':'00000000000',
    'sks_lulus':0,
    'lahir':datetime.datetime(1111,1,11)
}

data_mahasiswa = {}
while True :
    os.system("cls")
    print(f"{'SELAMAT DATANG':^20}")
    print(f"{'DATA MAHASISWA':^20}")
    print("-"*20)
    #mengambil key dari template saja
    mahasiswa=dict.fromkeys(mahasiswa_template.keys())
    #print(mahasiswa)#kosong
    mahasiswa['nama'] = input("Nama mahasiswa :")
    mahasiswa['nim'] = input("Nim mahasiswa :")
    mahasiswa['sks_lulus'] = int(input("Sks Lulus :"))
    TAHUN_LAHIR =int(input("Tahun lahir(yyyy) :"))
    BULAN_LAHIR =int(input("Bulan lahir(1-12) :"))
    TANGGAL_LAHIR =int(input("TANGGAL lahir(1-31) :"))
    mahasiswa['lahir'] =datetime.datetime(TAHUN_LAHIR,BULAN_LAHIR,TANGGAL_LAHIR)
    #print(mahasiswa)#bagian bagiannya di isi oleh input
    #membuat random string agar tidak menimpa key data sebelumnya ketika di loop
    KEY = ''.join((random.choice(string.ascii_uppercase) for i in range(6)))
    data_mahasiswa.update({KEY:mahasiswa})

    print(f"\n{'KEY':<6} {'Nama':<17} {'NIM':<11} {'SKS':<3} {'Lahir':<10}")
    print("-"*50)

    for mahasiswa in data_mahasiswa:
        KEY = mahasiswa

        NAMA = data_mahasiswa[KEY]['nama']
        NIM = data_mahasiswa[KEY]['nim']
        SKS = data_mahasiswa[KEY]['sks_lulus']
        LAHIR = data_mahasiswa[KEY]['lahir'].strftime("%x")
        
        print(f"{KEY:<6} {NAMA:<17} {NIM:<11} {SKS:<3} {LAHIR:<10}")

    print("\n")
    is_done = input("Mau melanjutkan (y/n)?")
    if is_done == "n":
        break
print("Akhir dari program terima kasih")
