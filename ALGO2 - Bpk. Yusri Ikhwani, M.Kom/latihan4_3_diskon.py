#2510010102 - M. Rizky Rinaldy
def hitung_harga(harga_awal, diskon=10, pajak=11): 
    potongan = harga_awal * diskon / 100 
    setelah_diskon = harga_awal - potongan 
    nilai_pajak = setelah_diskon * pajak / 100 
    total = setelah_diskon + nilai_pajak 
    return total, potongan, nilai_pajak 

print("+==================================+")
print("|         Kalkulator Harga         |")
print("+==================================+")

harga = float(input("   Harga barang   : ")) 
d     = float(input("   Diskon (%)     : ")) 
  
total, pot, pjk = hitung_harga(harga, d) 

print("+==================================+")
print("|        Hasil Perhitungan         |")
print("+==================================+")
print(f"| Harga Awal      : Rp {harga:11,.0f} |") 
print(f"| Potongan        : Rp {pot:11,.0f} |") 
print(f"| Pajak (11%)     : Rp {pjk:11,.0f} |") 
print(f"| Total Bayar     : Rp {total:11,.0f} |") 
print("+----------------------------------+")
print()
print("+==================================+")
print("| Dosen: Bpk. Yusri Ikhwani, M.Kom |")
print("|   2510010102 - M. Rizky Rinaldy  |")
print("+==================================+")

input()