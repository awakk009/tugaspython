#Studi Kasus - Hukum Waris Sederhana
# Sebuah keluarga meninggalkan warisan sebesar Rp 120.000.000

#Aturan Hukum waris Sederhana menggunakan pemrograman python
#1. Jika Ahli Waris Adalah Laki-laki, Mendapat 2 Bagian
#2. Jika Ahli Waris Adalah Perempuan, Mendapat 1 bagian
#3. Program Meminta Jumlah Anak Laki-laki Dan Jumlah Anak Perempuan
#4. Program menghitung bagian masing-masing ahli waris

print("===Program Pembagian Waris Sederhana===")
warisan = int(input("Masukkan Jumlah Harta Warisan: Rp"))
lk = int(input("Jumlah Anak Laki - laki:"))
pr = int(input("Jumlah Anak Perempuan:"))

#menghitung jumlah bagian 

bagian_lk = lk * 2
bagian_pr = pr * 1
total_bagian = bagian_lk + bagian_pr

#percabangan waris
if total_bagian > 0:
    nilai_bagian = warisan / total_bagian
    
    print("\n=== HASIL PEMBAGIAN")
if lk > 0:
    print("Setiap Anak Laki - laki mendapatkan Rp", int(nilai_bagian*2))
    
if pr > 0:
    print("Setiap Anak Perempuan mendapatkan Rp", int(nilai_bagian*1))
    
else:
    print("Tidak ada ahli waris")
    
