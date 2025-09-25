#latihan python
print(f"{"Latihan data list".center(40,"=")}")
print(f"{"input data buku".center(40,"-")}")
listbuku=[]
while True :
    print(f"{"masukkan data buku".center(40)}")
    nama=input("masukkan nama buku :")
    pengarang =input ("masukkan nama pengarang :")
    data_buku = [nama,pengarang]
    listbuku.append(data_buku)
    print(f"\n\r{"databuku".center(40,"-")}")
    for index,buku in enumerate(listbuku):
        print(f"{index+1}|{buku[0]}|{buku[1]}")
    selesai=input("apakah selesai?(y/n) :")
    if selesai == "y" :
        break
print(f"{"selesai".center(40,"-")}")
