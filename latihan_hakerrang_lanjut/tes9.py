# memeriksa apakah string terdiri dari alfabet, alfanumerik, ataupun karakter spesial dll
if __name__ == '__main__':
    s = input()
    print(s.isalnum())
    print(s.isalpha())
    print(s.isdigit())
    print(s.islower())
    print(s.isupper())

