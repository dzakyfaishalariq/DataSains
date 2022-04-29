import library.area_library as lib1
import lib_saya as lib2
import os
os.system('cls')
obj1 = lib1.aritmatika2(10, 5)
obj2 = lib2.aritmatika(10, 5, obj1)
obj3 = lib2.aritmatika(20, 5, obj1)

print("kurang : ")
print(obj1.kurang())

print("Tambah : ")
print(obj2.tambah())

print("Kurang : ")
print(obj3.tambah())
