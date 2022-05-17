# membuat pogram memnentukan rataan dari kata
"""
Diberikan sebuah kalimat sebagai input, hitung dan output rata-rata panjang kata dari kalimat itu.
Untuk menghitung panjang kata rata-rata, Anda perlu membagi jumlah semua panjang kata dengan jumlah kata dalam kalimat.

Contoh Masukan:
ini beberapa teks

Contoh Keluaran:
3.5

Penjelasan: Ada 4 kata di input yang diberikan, dengan total 14 huruf, jadi panjang rata-ratanya adalah: 14/4 = 3,5
String memiliki metode split(), yang mengembalikan pemisahan string ke dalam daftar, dengan pemisah yang diberikan. Secara default, pemisah adalah spasi, jadi memanggil split() akan mengembalikan daftar yang berisi kata-kata dari string sebagai item.
"""
text = input()
panjang = 0
n_kata = len(text.split())
for i in text:
    if i == ' ':
        continue
    panjang += 1
print(panjang/n_kata)
