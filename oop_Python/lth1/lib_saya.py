class aritmatika:
    a, b = 0, 0
    hasil = 0

    def __init__(self, a, b, clazz=None):
        self.a = a
        self.b = b
        self.clazz = clazz

    def tambah(self):
        self.hasil = self.a+self.b+self.clazz.a
        return self.hasil
