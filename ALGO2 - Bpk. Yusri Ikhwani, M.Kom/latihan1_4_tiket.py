# M. Rizky Rinaldy - 2510010102
print("+====================================+")
print("|        Loket Tiket Bioskop         |")
print("+====================================+")
harga_normal = 50000 
umur         = int(input("  Masukkan umur (Tahun): "))
pelajar      =     input("  Apakah pelajar (Y/T) : ").upper() 

if umur < 12 or umur > 60: 
     diskon = 0.5 
     ket = "Diskon Anak/Lansia (50%)" 
elif pelajar == "Y": 
    diskon = 0.2 
    ket = "Diskon Pelajar (20%)" 
else: 
    diskon = 0 
    ket = "Harga Normal" 
   
potongan = harga_normal * diskon 
bayar    = harga_normal - potongan 

print("+====================================+")
print(f"| Harga Normal : Rp, {harga_normal:<16}|") 
print(f"| Keterangan   : {ket:<20}|") 
print(f"| Potongan     : Rp, {int(potongan):<16}|") 
print(f"| Total Bayar  : Rp, {int(bayar):<16}|") 
print("+====================================+")
print()
print("+====================================+")
print("|  Dosen: Bpk. Yusri Ikhwani, M.Kom  |")
print("|    2510010102 - M. Rizky Rinaldy   |")
print("+====================================+")

input()