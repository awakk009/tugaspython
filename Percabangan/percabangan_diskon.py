print("===PROGRAM KASIR SEDERHANA===")
harga = int(input("Masukkan Harga Barang: Rp"))
jumlah = int(input("Masukkan Jumlah Barang:"))

total = harga*jumlah

#percabangan diskon
if total >=100000:
    diskon = total*10/100
elif total >=50000:
    diskon = total*5/100
else:
    diskon = 0

total_bayar = total - diskon
print("\n===STRUK BELANJA===")
print("Total Harga: Rp", total)
print("diskon: Rp", int(diskon))
print("Total Pembayaran Rp", int(total_bayar))

# PERCABANGAN KEMBALIAN
uang = int(input("Masukkan Uang Pembayaran: Rp"))
if uang >= total_bayar:
    kembalian = uang -total_bayar
    print("Uang Pembayaran: Rp",uang)
    print("Kembalian: Rp", int(kembalian))
else:
    kekurangan = total_bayar - uang
    print("Uang Tidak Cukup!")
    print("Kekurangan Rp", int(kekurangan))
    
    
kembalian = uang - total_bayar
print("Uang Pembayaran: Rp", uang)
print("Kembalian: Rp", int(kembalian))



