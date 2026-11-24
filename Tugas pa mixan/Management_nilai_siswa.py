
# Program Manajemen Siswa Sederhana

data_siswa = []

# Fungsi untuk menambah data siswa
def tambah_siswa():
    print("\n=== TAMBAH DATA SISWA ===")
    nama = input("Masukkan nama siswa: ")
    nilai = float(input("Masukkan nilai siswa: "))

    siswa = {
        "nama": nama,
        "nilai": nilai
    }

    data_siswa.append(siswa)
    print("Data siswa berhasil ditambahkan!")


# Fungsi untuk menampilkan data siswa
def tampilkan_siswa():
    print("\n=== DATA SISWA ===")

    if len(data_siswa) == 0:
        print("Belum ada data siswa.")
    else:
        for i, siswa in enumerate(data_siswa, start=1):
            print(f"{i}. Nama  : {siswa['nama']}")
            print(f"   Nilai : {siswa['nilai']}")


# Fungsi untuk menghitung rata-rata
def hitung_rata_rata():
    print("\n=== RATA-RATA NILAI ===")

    if len(data_siswa) == 0:
        print("Belum ada data siswa.")
    else:
        total = 0

        for siswa in data_siswa:
            total += siswa["nilai"]

        rata_rata = total / len(data_siswa)

        print(f"Jumlah siswa : {len(data_siswa)}")
        print(f"Rata-rata    : {rata_rata:.2f}")


# Fungsi mencari nilai tertinggi
def nilai_tertinggi():
    print("\n=== NILAI TERTINGGI ===")

    if len(data_siswa) == 0:
        print("Belum ada data siswa.")
    else:
        tertinggi = data_siswa[0]

        for siswa in data_siswa:
            if siswa["nilai"] > tertinggi["nilai"]:
                tertinggi = siswa

        print(f"Nama  : {tertinggi['nama']}")
        print(f"Nilai : {tertinggi['nilai']}")


# Program utama
def menu():
    while True:
        print("\n================================")
        print("   PROGRAM MANAJEMEN NILAI")
        print("================================")
        print("1. Tambah Data Siswa")
        print("2. Tampilkan Data Siswa")
        print("3. Hitung Rata-rata")
        print("4. Cari Nilai Tertinggi")
        print("5. Keluar")
        print("================================")

        pilihan = input("Pilih menu (1-5): ")

        if pilihan == "1":
            tambah_siswa()

        elif pilihan == "2":
            tampilkan_siswa()

        elif pilihan == "3":
            hitung_rata_rata()

        elif pilihan == "4":
            nilai_tertinggi()

        elif pilihan == "5":
            print("Terima kasih telah menggunakan program!")
            break

        else:
            print("Pilihan tidak valid! Silakan coba lagi.")


# Menjalankan program
menu()
