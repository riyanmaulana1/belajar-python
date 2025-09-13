import datetime as dt
hari_ini = dt.date.today()
print(hari_ini)
print(f"Hari ini adalah hari = {hari_ini:%A}")
tanggal = dt.date(2006,5,11)
print(tanggal)
 #latihan date and time
print("latihan".center(15,"="))
print("Silahkan masukkan tanggal, bulan, tahun kelahiran anda")
tanggal =int(input("Tanggal \t:"))
bulan =int(input("Bulan \t\t:"))
tahun =int(input("tahun \t\t:"))
tanggal_lahir = dt.date(tahun,bulan,tanggal)
print(f"tanggal lahir anda:{tanggal_lahir}")
print(f"hari lahir anda:{tanggal_lahir:%A}")
#membuat umur
hari_ini = dt.date.today()
print(f"hari ini tanggal :{hari_ini}{hari_ini:%A}")
umur_hari = hari_ini - tanggal_lahir
umur_hari1 = ((umur_hari.days % 365) % 30)
umur_bulan = (umur_hari.days % 365) // 30
umur_tahun = umur_hari.days // 365 #.days agar diambil angkanya saja
print(f"umur anda {umur_tahun} tahun, {umur_bulan} bulan,{umur_hari1} hari")
