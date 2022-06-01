# menyambungkan ke database xampp
import pymysql as sql
# conek database


class Databases:
    def __init__(self, host, user, passwd, db):
        self.host = host
        self.user = user
        self.passwd = passwd
        self.db = db

    def connect(self):
        self.conn = sql.connect(
            host=self.host, user=self.user, passwd=self.passwd, db=self.db)
        self.c = self.conn.cursor()
    # fungsi untuk melihat data

    def read(self, query):
        self.c.execute(query)
        return self.c.fetchall()
    # fungsi untuk menambah data

    def create(self, query):
        self.c.execute(query)
        self.conn.commit()
    # fungsi untuk mengupdate data

    def update(self, query):
        self.c.execute(query)
        self.conn.commit()
    # fungsi untuk menghapus data

    def delete(self, query):
        self.c.execute(query)
        self.conn.commit()


if __name__ == "__main__":
    db = Databases("localhost", "root", "", "crud_portal")
    db.connect()
    # tambah data
    db.create("INSERT INTO data VALUES(3,'Alfian','Jl.Kaliurang','0812121212')")
    for i in db.read("SELECT * FROM tb_mahasiswa"):
        print(i)
