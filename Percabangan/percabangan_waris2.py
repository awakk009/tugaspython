#Ketentuan

#1. Istri mendapatkan 1/8 bagian
#2. Sisa harta setelah bagian istri diberikan kepada anak
#3. Anak laki-laki dapat 2 bagian
#4. Anak perempuan dapat 1 bagian
#program input jumlah anak laki-laki dan jumlah anak perempuan

print("===Program Pembagian Waris Sederhana===")
warisan = int(input("Masukkan Jumlah Harta Warisan: Rp"))
lk = int(input("Jumlah Anak Laki - laki:"))
pr = int(input("Jumlah Anak Perempuan:"))

#menghitung jumlah bagian 
bagian_istri = 1/8 * warisan
bagian_lk = lk * 2
bagian_pr = pr * 1
nilai_bagian = bagian_lk + bagian_pr
sisa_warisan = warisan - bagian_istri

#percabangan waris 
print("\n=== HASIL PEMBAGIAN ===")
print("Istri Mendapatkan Rp: ", int(bagian_istri))
print("Sisa Harta Warisan", int(sisa_warisan))

if nilai_bagian > 0:
    sisa_bagian = sisa_warisan / nilai_bagian
    
if lk > 0:
    print("Setiap anak laki-laki mendapatkan Rp: ", int(sisa_bagian*2))

if pr > 0:
    print("Setiap anak perempuan mendapatkan Rp: ", int(sisa_bagian*1))

else:
    print("Tidak Ada ahli Waris")

