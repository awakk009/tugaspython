def hitung_diskon(harga, persen_diskon):
    return harga - (harga * persen_diskon / 100)

def info_produk(nama, harga):
    if harga > 100000:
        harga_diskon = hitung_diskon(harga, 10)
    else:
        harga_diskon = hitung_diskon(harga, 5)
        print(f"{nama} | Harga asli: {harga} | Setelah Diskon: {harga_diskon}")
        
info_produk("Kemeja", 120000)
info_produk("Kaos", 80000)