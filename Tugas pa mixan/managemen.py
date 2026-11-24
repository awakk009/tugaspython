#Contoh Output :
    #Tambah Data Siswa
    #Tampilkan Data Siswa
    #Hitung Rata-rata
    #Cari Nilai Tertinggi
    #Keluar
# Program Manajemen Siswa Sederhana

#List untuk menyimpan data siswa
data_siswa = []

def tambah_data():
    print("\n=== Tambah Data Siswa ===")
    nama = input("Masukkan Nama Siswa: ")
    nilai = int(input("Masukkan Nilai Siswa: "))

    siswa = {
        "nama" : nama,
        "nilai": nilai
    }

    data_siswa.append(siswa)
    print("Data siswa berhasil di tambahan!")

#Fungsi untuk menampilkan data siswa 
def tampilkan_siswa():
    print("\n=== DATA SISWA ===")

    if len(data_siswa) == 0:
        print("Belum ada data siswa")
    else:
        for i, siswa in enumerate(data_siswa):
            print(f"{i}, Nama : {siswa['nama']}")
            print(f" , Nilai : {siswa['nilai']}")

#Fungsi untuk menghitung rata rata
def hitung_rata_rata():
    print("\n=== RATA RATA NILAI ===")

    if len(data_siswa) == 0:
        print("Belum ada data siswa")
    else:
        total = 0

        for siswa in data_siswa:
            total += siswa["nilai"]

        rata_rata = total / len(data_siswa)

        print(f"Jumlah Siswa  : {len(data_siswa)}")
        print(f"Rata-rata     : {rata_rata:.2f}")

#Mencari Nilai tertinggi
def nilai_tertinggi():
    print("\n=== NILAI TERTINGGI ===")

    if len(data_siswa) == 0:
        print("Belum ada data siswa")
    else:
        tertinggi = data_siswa[0]

        for siswa in data_siswa:
            if siswa["nilai"] > tertinggi["nilai"]:
                tertinggi = siswa

        print(f"Nama   : {tertinggi['nama']}")
        print(f"Nilai  : {tertinggi['nilai']}")

#Program Utama
def menu():
    while True:
        print("\n===============================")
        print("   ROGRAM MANAGEMENT NILAI")
        print("\n===============================")
        print("1. Tambahkan Data Siswa")
        print("2. Tampilkan Data Siswa")
        print("3. Hitung Rata-rata")
        print("4. Cari Nilai Tertinggi")
        print("5. Keluar")

        pilihan = input("Pilih menu (1-5): ")

        if pilihan == "1":
            tambah_data()

        elif pilihan == "2":
            tampilkan_siswa()

        elif pilihan == "3":
            hitung_rata_rata()

        elif pilihan == "4":
            nilai_tertinggi()

        elif pilihan == "5":
            print("Terimakasih bang, minimal ngisi lah wok")
            break

        else:
            print("Kan udah dikasih pilihan! pilih lah itu gk respek bngt wok")

#Menjalankan program 
menu()