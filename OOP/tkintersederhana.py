import tkinter

#membuat aksi(command)
def nama():
    nama = entry1.get()
    label_hasil.config(text=f"selamat datang {nama}")#mengganti setelah tombol panggil diklik


main_window = tkinter.Tk()

Label1 = tkinter.Label(main_window, text = "selamat datang")
Label2 = tkinter.Label(main_window, text = "Terimakasih")


entry1 = tkinter.Entry(main_window)

#method positionning
Label1.pack()
entry1.pack()
# membuat tombol yang memiliki aksi dibaliknya (command)
tkinter.Button(main_window, text="panggil", command=nama).pack()

label_hasil = tkinter.Label(main_window, text="")
label_hasil.pack()
Label2.pack()
