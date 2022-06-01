import os
os.system('cls')

# algoritma pendeteksi karakter


class Karakter:
    def __init__(self, s):
        self.s = s

    def n_isalnum(self):
        hasil = False
        for i in self.s:
            if i.isalnum():
                hasil = True
            else:
                continue
        return hasil

    def n_isalpha(self):
        hasil = False
        for i in self.s:
            if i.isalpha():
                hasil = True
            else:
                continue
        return hasil

    def n_isdigit(self):
        hasil = False
        for i in self.s:
            if i.isdigit():
                hasil = True
            else:
                continue
        return hasil

    def n_islower(self):
        hasil = False
        for i in self.s:
            if i.islower():
                hasil = True
            else:
                continue
        return hasil

    def n_isupper(self):
        hasil = False
        for i in self.s:
            if i.isupper():
                hasil = True
            else:
                continue
        return hasil


if __name__ == "__main__":
    s = input()
    k = Karakter(s)
    print(k.n_isalnum())
    print(k.n_isalpha())
    print(k.n_isdigit())
    print(k.n_islower())
    print(k.n_isupper())
