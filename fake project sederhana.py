## proyek kasir sederhana
print(f"{"Proyek sederhana Riyan".center(40,"-")}")
ussername = "riyan"
sandi ="12345678"
while True :
    nama =input("ussername :")
    password =input("password  :")
    if nama == ussername and password == sandi :
        break
    elif nama == ussername and password != sandi :
        print("mohon masukkan password dengan benar!!!")
    elif nama != ussername and password == sandi :
        print("mohon masukkan ussername dengan benar!!!")
    else :
        print(f"mohon masukkan ussername dan sandi dengan benar!!!")
print("------------------------------------------")
daftar_pesanan=[]
while True:
    print("""\tCAFE BANGKOK MENU
          \n1.Coffe
          \n2.Breakfast Breads and Snacks
          \n3.Deserts Cakes and Donuts
          \n----------------------------------------""")
    menu=int(input("Masukkan nomor menu :"))
    while menu >3 and menu <0 :
        print("masukkan angka dengan benar!!!")
        menu=int(input("Masukkan nomor menu :"))
    match menu :
        case 1:
            print("""----Coffe Menu----
                  \n1.Americano\t\tRp.10,000
                  \n2.Iced Cafe Latte\tRp.15,000
                  \n3.Macha Coffe\t\tRp.12,000
                  \n4.Iced Milk Capucino\tRp.15,000
                  \n------------------------------------------""")
            coffe_menu=int(input("masukkan nomor menu :"))
            while coffe_menu >4 and coffe_menu <0 :
                print("masukkan angka dengan benar!!!")
                coffe_menu=int(input("Masukkan nomor menu :"))
            match coffe_menu :
                case 1 :
                    nama ="Americano"
                    harga = 10000
                    jumlah = int(input("Masukkan jumlah yang dipesan :"))
                    data_beli =[nama,harga,jumlah]
                    daftar_pesanan.append(data_beli)
                    for index,pesanan in enumerate(daftar_pesanan):
                        print(f"No.{index+1}|{pesanan[0]}|{pesanan[1]}|{pesanan[2]}")
                    nambah=input("Apakah tambah pesanan?(y/n) :")
                    while nambah != "y" and nambah != "n" :
                        print("Input huruf dengan benar !!!")
                        nambah=input("Apakah tambah pesanan?(y/n) :")
                    if nambah == "y":
                        print("------------------------------------------")
                        continue
                    elif nambah == "n":
                        break
                case 2 :
                    nama ="Iced Cafe Latte"
                    harga =15000
                    jumlah = int(input("Masukkan jumlah yang dipesan :"))
                    data_beli =[nama,harga,jumlah]
                    daftar_pesanan.append(data_beli)
                    for index,pesanan in enumerate(daftar_pesanan):
                        print(f"No.{index+1}|{pesanan[0]}|{pesanan[1]}|{pesanan[2]}")
                    nambah=input("Apakah tambah pesanan?(y/n) :")
                    while nambah != "y" and nambah != "n" :
                        print("Input huruf dengan benar !!!")
                        nambah=input("Apakah tambah pesanan?(y/n) :")
                    if nambah == "y":
                        print("------------------------------------------")
                        continue
                    elif nambah == "n":
                        break
                case 3 :
                    nama ="Macha Coffe"
                    harga =12000
                    jumlah = int(input("Masukkan jumlah yang dipesan :"))
                    data_beli =[nama,harga,jumlah]
                    daftar_pesanan.append(data_beli)
                    for index,pesanan in enumerate(daftar_pesanan):
                        print(f"No.{index+1}|{pesanan[0]}|{pesanan[1]}|{pesanan[2]}")
                    nambah=input("Apakah tambah pesanan?(y/n) :")
                    while nambah != "y" and nambah != "n" :
                        print("Input huruf dengan benar !!!")
                        nambah=input("Apakah tambah pesanan?(y/n) :")
                    if nambah == "y":
                        print("------------------------------------------")
                        continue
                    elif nambah == "n":
                        break
                case 4 :
                    nama = "Iced Milk Capucino"
                    harga =15000
                    jumlah = int(input("Masukkan jumlah yang dipesan :"))
                    data_beli =[nama,harga,jumlah]
                    daftar_pesanan.append(data_beli)
                    for index,pesanan in enumerate(daftar_pesanan):
                        print(f"No.{index+1}|{pesanan[0]}|{pesanan[1]}|{pesanan[2]}")
                    nambah=input("Apakah tambah pesanan?(y/n) :")
                    while nambah != "y" and nambah != "n" :
                        print("Input huruf dengan benar !!!")
                        nambah=input("Apakah tambah pesanan?(y/n) :")
                    if nambah == "y":
                        print("------------------------------------------")
                        continue
                    elif nambah == "n":
                        break
        case 2:
            print("""----Breakfast Menu----
                  \n1.Plain Bread\tRp.10,000
                  \n2.Chicken Bread\tRp.12,000
                  \n3.Beef Bread\tRp.12,000
                  \n4.French Fries\tRp.13,000
                  \n5.Chiken Stick\tRp.13,000
                  \n6.Spicy Nachos\tRp.13,000
                  \n------------------------------------------""")
            Breakfast=int(input("masukkan nomor menu :"))
            while Breakfast >6 and Breakfast <0 :
                print("masukkan angka dengan benar!!!")
                Breakfast=int(input("Masukkan nomor menu :"))
            match Breakfast :
                case 1 :
                    nama="Plain Bread"
                    harga = 10000
                    jumlah = int(input("Masukkan jumlah yang dipesan :"))
                    data_beli =[nama,harga,jumlah]
                    daftar_pesanan.append(data_beli)
                    for index,pesanan in enumerate(daftar_pesanan):
                        print(f"No.{index+1}|{pesanan[0]}|{pesanan[1]}|{pesanan[2]}")
                    nambah=input("Apakah tambah pesanan?(y/n) :")
                    while nambah != "y" and nambah != "n" :
                        print("Input huruf dengan benar !!!")
                        nambah=input("Apakah tambah pesanan?(y/n) :")
                    if nambah == "y":
                        print("------------------------------------------")
                        continue
                    elif nambah == "n":
                        break
                case 2 :
                    nama="Chicken Bread"
                    harga = 12000
                    jumlah = int(input("Masukkan jumlah yang dipesan :"))
                    data_beli =[nama,harga,jumlah]
                    daftar_pesanan.append(data_beli)
                    for index,pesanan in enumerate(daftar_pesanan):
                        print(f"No.{index+1}|{pesanan[0]}|{pesanan[1]}|{pesanan[2]}")
                    nambah=input("Apakah tambah pesanan?(y/n) :")
                    while nambah != "y" and nambah != "n" :
                        print("Input huruf dengan benar !!!")
                        nambah=input("Apakah tambah pesanan?(y/n) :")
                    if nambah == "y":
                        print("------------------------------------------")
                        continue
                    elif nambah == "n":
                        break
                case 3 :
                    nama= "Beef Bread"
                    harga = 12000
                    jumlah = int(input("Masukkan jumlah yang dipesan :"))
                    data_beli =[nama,harga,jumlah]
                    daftar_pesanan.append(data_beli)
                    for index,pesanan in enumerate(daftar_pesanan):
                        print(f"No.{index+1}|{pesanan[0]}|{pesanan[1]}|{pesanan[2]}")
                    nambah=input("Apakah tambah pesanan?(y/n) :")
                    while nambah != "y" and nambah != "n" :
                        print("Input huruf dengan benar !!!")
                        nambah=input("Apakah tambah pesanan?(y/n) :")
                    if nambah == "y":
                        print("------------------------------------------")
                        continue
                    elif nambah == "n":
                        break
                case 4 :
                    nama = "French Fries"
                    harga = 13000
                    jumlah = int(input("Masukkan jumlah yang dipesan :"))
                    data_beli =[nama,harga,jumlah]
                    daftar_pesanan.append(data_beli)
                    for index,pesanan in enumerate(daftar_pesanan):
                        print(f"No.{index+1}|{pesanan[0]}|{pesanan[1]}|{pesanan[2]}")
                    nambah=input("Apakah tambah pesanan?(y/n) :")
                    while nambah != "y" and nambah != "n" :
                        print("Input huruf dengan benar !!!")
                        nambah=input("Apakah tambah pesanan?(y/n) :")
                    if nambah == "y":
                        print("------------------------------------------")
                        continue
                    elif nambah == "n":
                        break
                case 5 :
                    nama = "Chiken Stick"
                    harga = 13000
                    jumlah = int(input("Masukkan jumlah yang dipesan :"))
                    data_beli =[nama,harga,jumlah]
                    daftar_pesanan.append(data_beli)
                    for index,pesanan in enumerate(daftar_pesanan):
                        print(f"No.{index+1}|{pesanan[0]}|{pesanan[1]}|{pesanan[2]}")
                    nambah=input("Apakah tambah pesanan?(y/n) :")
                    while nambah != "y" and nambah != "n" :
                        print("Input huruf dengan benar !!!")
                        nambah=input("Apakah tambah pesanan?(y/n) :")
                    if nambah == "y":
                        print("------------------------------------------")
                        continue
                    elif nambah == "n":
                        break
                case 6 :
                    nama = "Spicy Nachos"
                    harga = 13000
                    jumlah = int(input("Masukkan jumlah yang dipesan :"))
                    data_beli =[nama,harga,jumlah]
                    daftar_pesanan.append(data_beli)
                    for index,pesanan in enumerate(daftar_pesanan):
                        print(f"No.{index+1}|{pesanan[0]}|{pesanan[1]}|{pesanan[2]}")
                    nambah=input("Apakah tambah pesanan?(y/n) :")
                    while nambah != "y" and nambah != "n" :
                        print("Input huruf dengan benar !!!")
                        nambah=input("Apakah tambah pesanan?(y/n) :")
                    if nambah == "y":
                        print("------------------------------------------")
                        continue
                    elif nambah == "n":
                        break
        case 3 :
            print("""----Desert Menu----
                  \n1.Tiramisu Cake\tRp.12,000
                  \n2.Strawberry Cake\tRp.12,000
                  \n3.Chocolate Cake\tRp.12,000
                  \n4.Sugar raised Donut\tRp.8,000
                  \n5.Choc ALmond Donut\tRp.12,000
                  \n6.Butterscoth Donut\tRp.12,000
                  \n------------------------------------------""")
            Desert_menu = int(input("Masukkan naomor pesanan :"))
            while Desert_menu >6 and Desert_menu <0 :
                print("masukkan angka dengan benar!!!")
                Desert_menu=int(input("Masukkan nomor menu :"))
            match Desert_menu :
                case 1 :
                    nama = "Tiramisu Cake"
                    harga = 12000
                    jumlah = int(input("Masukkan jumlah yang dipesan :"))
                    data_beli =[nama,harga,jumlah]
                    daftar_pesanan.append(data_beli)
                    for index,pesanan in enumerate(daftar_pesanan):
                        print(f"No.{index+1}|{pesanan[0]}|{pesanan[1]}|{pesanan[2]}")
                    nambah=input("Apakah tambah pesanan?(y/n) :")
                    while nambah != "y" and nambah != "n" :
                        print("Input huruf dengan benar !!!")
                        nambah=input("Apakah tambah pesanan?(y/n) :")
                    if nambah == "y":
                        print("------------------------------------------")
                        continue
                    elif nambah == "n":
                        break
                case 2 :
                    nama = "Strawberry Cake"
                    harga = 12000
                    jumlah = int(input("Masukkan jumlah yang dipesan :"))
                    data_beli =[nama,harga,jumlah]
                    daftar_pesanan.append(data_beli)
                    for index,pesanan in enumerate(daftar_pesanan):
                        print(f"No.{index+1}|{pesanan[0]}|{pesanan[1]}|{pesanan[2]}")
                    nambah=input("Apakah tambah pesanan?(y/n) :")
                    while nambah != "y" and nambah != "n" :
                        print("Input huruf dengan benar !!!")
                        nambah=input("Apakah tambah pesanan?(y/n) :")
                    if nambah == "y":
                        print("------------------------------------------")
                        continue
                    elif nambah == "n":
                        break
                case 3 :
                    nama = "Chocolate Cake"
                    harga = 12000
                    jumlah = int(input("Masukkan jumlah yang dipesan :"))
                    data_beli =[nama,harga,jumlah]
                    daftar_pesanan.append(data_beli)
                    for index,pesanan in enumerate(daftar_pesanan):
                        print(f"No.{index+1}|{pesanan[0]}|{pesanan[1]}|{pesanan[2]}")
                    nambah=input("Apakah tambah pesanan?(y/n) :")
                    while nambah != "y" and nambah != "n" :
                        print("Input huruf dengan benar !!!")
                        nambah=input("Apakah tambah pesanan?(y/n) :")
                    if nambah == "y":
                        print("------------------------------------------")
                        continue
                    elif nambah == "n":
                        break
                case 4 :
                    nama = "Sugar raised Donut"
                    harga = 8000
                    jumlah = int(input("Masukkan jumlah yang dipesan :"))
                    data_beli =[nama,harga,jumlah]
                    daftar_pesanan.append(data_beli)
                    for index,pesanan in enumerate(daftar_pesanan):
                        print(f"No.{index+1}|{pesanan[0]}|{pesanan[1]}|{pesanan[2]}")
                    nambah=input("Apakah tambah pesanan?(y/n) :")
                    while nambah != "y" and nambah != "n" :
                        print("Input huruf dengan benar !!!")
                        nambah=input("Apakah tambah pesanan?(y/n) :")
                    if nambah == "y":
                        print("------------------------------------------")
                        continue
                    elif nambah == "n":
                        break
                case 5 :
                    nama = "Choc ALmond Donut"
                    harga = 12000
                    jumlah = int(input("Masukkan jumlah yang dipesan :"))
                    data_beli =[nama,harga,jumlah]
                    daftar_pesanan.append(data_beli)
                    for index,pesanan in enumerate(daftar_pesanan):
                        print(f"No.{index+1}|{pesanan[0]}|{pesanan[1]}|{pesanan[2]}")
                    nambah=input("Apakah tambah pesanan?(y/n) :")
                    while nambah != "y" and nambah != "n" :
                        print("Input huruf dengan benar !!!")
                        nambah=input("Apakah tambah pesanan?(y/n) :")
                    if nambah == "y":
                        print("------------------------------------------")
                        continue
                    elif nambah == "n":
                        break
                case 6 :
                    nama = "Butterscoth Donut"
                    harga = 12000
                    jumlah = int(input("Masukkan jumlah yang dipesan :"))
                    data_beli =[nama,harga,jumlah]
                    daftar_pesanan.append(data_beli)
                    for index,pesanan in enumerate(daftar_pesanan):
                        print(f"No.{index+1}|{pesanan[0]}|{pesanan[1]}|{pesanan[2]}")
                    nambah=input("Apakah tambah pesanan?(y/n) :")
                    while nambah != "y" and nambah != "n" :
                        print("Input huruf dengan benar !!!")
                        nambah=input("Apakah tambah pesanan?(y/n) :")
                    if nambah == "y":
                        print("------------------------------------------")
                        continue
                    elif nambah == "n":
                        break
total_biaya = 0
for pesan in daftar_pesanan :
    hargapesan = pesan[1]
    jumlahpesan =pesan[2]
    total_biaya += hargapesan*jumlahpesan
print("------------------------------------------")
member=input("Apakah anda member?(y/n) :")
while member != "y" and member != "n" :
    print("Input huruf dengan benar !!!")
    member=input("Apakah anda member?(y/n) :")
if member == "y":
    diskon=0.05*total_biaya
elif member == "n":
    diskon=0
print(f"Total item :{total_biaya:,}")
total_bayar=(float(total_biaya)-diskon)//1
total_bayar=int(total_bayar)
print(f"Total Diskon :{diskon}")
print(f"Total bayar :{total_bayar:,}")
print(f"{"selesai".center(40,"=")}")
