import sqlite3

# Fungsi untuk membuat tabel mahasiswa jika belum ada
def create_table():
    connection = sqlite3.connect("mahasiswa.db")
    cursor = connection.cursor()

    # Membuat tabel mahasiswa
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS mahasiswa (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nama TEXT NOT NULL,
            nim TEXT NOT NULL,
            jurusan TEXT NOT NULL
        )
    ''')

    connection.commit()
    connection.close()

# Fungsi untuk menambahkan mahasiswa baru
def tambah_mahasiswa(nama, nim, jurusan):
    connection = sqlite.connect("mahasiswa.db")
    cursor = connection.cursor()

    # Menambahkan mahasiswa baru
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS mahasiswa (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        nama TEXT NOT NULL,
        nim TEXT NOT NULL,
        jurusan TEXT NOT NULL
    )
''')

connection.commit()
connection.close()

    # Perintah SQL untuk menambahkan mahasiswa baru
  

# Fungsi untuk menampilkan semua mahasiswa
def tampilkan_semua_mahasiswa():
    connection = ###
    cursor = ###

    # Menampilkan semua mahasiswa
    cursor.execute("SELECT * FROM mahasiswa")
rows = cursor.fetchall()

for row in rows:
    print(f"ID: {row[0]}, Nama: {row[1]}, NIM: {row[2]}, Jurusan: {row[3]}")

connection.close()

# Fungsi untuk mengupdate data mahasiswa
def update_mahasiswa(nim, new_nama, new_jurusan):
    connection = sqlite.connect ("mahasiswa.db")
    cursor = connection.cursor

    cursor.execute("UPDATE mahasiswa SET nama = ?, jurusan = ? WHERE nim = ?", (new_nama, new_jurusan, nim))

connection.commit()
connection.close()

# DELETE!!!!!!!!!!!!!!!
def hapus_mahasiswa(nim):
    connection = sqlite.connect ("mahasiswa.db")
    cursor = connection.cursor

    cursor.execute("DELETE FROM mahasiswa WHERE problem = ?;", (target_problem,))

    connection.commit()
    connection.close()

# Membuat tabel jika belum ada
create_table()

# Menambahkan beberapa mahasiswa
tambah_mahasiswa()

# Menampilkan semua mahasiswa
print("Daftar Mahasiswa:")
tampilkan_semua_mahasiswa()

# Mengupdate data mahasiswa
update_mahasiswa()

# Menampilkan semua mahasiswa setelah diupdate
print("\nDaftar Mahasiswa setelah Update:")
tampilkan_semua_mahasiswa()

# Menghapus mahasiswa berdasarkan NIM
hapus_mahasiswa()

# Menampilkan semua mahasiswa setelah dihapus
print("\nDaftar Mahasiswa setelah Hapus:")
tampilkan_semua_mahasiswa()