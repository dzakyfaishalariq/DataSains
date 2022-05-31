from tkinter import *
from tkinter import ttk
# membuat tampilan GUI dengan ukuran 800x600
root = Tk()
root.title("Aplikasi CRUD")
root.geometry("800x600")

# membuat navigasi
nav = Frame(root, bg="blue", height=50, relief=SUNKEN)
nav.pack(side=TOP, fill=X)
# membuat tombol
btn_add = Button(nav, text="Tambah")
btn_add.pack(side=LEFT)
btn_edit = Button(nav, text="Edit")
btn_edit.pack(side=LEFT)
btn_delete = Button(nav, text="Hapus")
btn_delete.pack(side=LEFT)
btn_read = Button(nav, text="Lihat")
btn_read.pack(side=LEFT)

# membuat tabel
tabel = ttk.Treeview(root, height=10, columns=("#nama", "#alamat", "#telp"))
tabel.column("#nama", width=100)
tabel.column("#alamat", width=200)
tabel.column("#telp", width=300)
tabel.heading("#nama", text="Nama")
tabel.heading("#alamat", text="Alamat")
tabel.heading("#telp", text="Telp")
for i in range(1, 11):
    tabel.insert("", "end", text=i, values=(
        "Nama " + str(i), "Alamat " + str(i), "Telp " + str(i)))
tabel.pack()

# jalankan aplikasi
root.mainloop()
