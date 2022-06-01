from library.model import Databases as db
from tkinter import *
from tkinter import ttk
# membuat tampilan GUI dengan ukuran 800x600
root = Tk()
root.title("Aplikasi CRUD")
root.geometry("800x600")
db = db("localhost", "root", "", "crud_portal")
db.connect()
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
# membuat fungsi tombol tambah untuk berpindah frame tambah


def tambah():
    global add_frame
    add_frame = Frame(root, bg="white", height=400, width=400, relief=SUNKEN)
    add_frame.pack(side=BOTTOM)
    # membuat label
    lbl_id = Label(add_frame, text="ID")
    lbl_id.grid(row=0, column=0, padx=10, pady=10)
    lbl_nama = Label(add_frame, text="Nama")
    lbl_nama.grid(row=1, column=0, padx=10, pady=10)
    lbl_alamat = Label(add_frame, text="Alamat")
    lbl_alamat.grid(row=2, column=0, padx=10, pady=10)
    lbl_telpon = Label(add_frame, text="Telpon")
    lbl_telpon.grid(row=3, column=0, padx=10, pady=10)
    # membuat entry
    ent_id = Entry(add_frame, width=10)
    ent_id.grid(row=0, column=1, padx=10, pady=10)
    ent_nama = Entry(add_frame, width=10)
    ent_nama.grid(row=1, column=1, padx=10, pady=10)
    ent_alamat = Entry(add_frame, width=10)
    ent_alamat.grid(row=2, column=1, padx=10, pady=10)
    ent_telpon = Entry(add_frame, width=10)
    ent_telpon.grid(row=3, column=1, padx=10, pady=10)
    # membuat tombol
    btn_save = Button(add_frame, text="Simpan")
    btn_save.config(command=db.create("INSERT INTO data VALUES({},'{}','{}','{}')".format(
        int(ent_id.get()), ent_nama.get(), ent_alamat.get(), ent_telpon.get())))
    btn_save.grid(row=4, column=0, padx=10, pady=10)


# fungsi simpan
# aksi tombol tambah
btn_add.config(command=tambah)
# membuat tabel
tabel = ttk.Treeview(root, height=10, columns=("#nama", "#alamat", "#telp"))
tabel.column("#nama", width=100)
tabel.column("#alamat", width=200)
tabel.column("#telp", width=300)
tabel.heading("#nama", text="Nama")
tabel.heading("#alamat", text="Alamat")
tabel.heading("#telp", text="Telp")
# nampilkan isi database ke tabel
for i in db.read("SELECT * FROM tb_mahasiswa"):
    tabel.insert('', 'end', text=str(i[0]), values=(i[1], i[2], i[3]))
tabel.pack()

# jalankan aplikasi
root.mainloop()
