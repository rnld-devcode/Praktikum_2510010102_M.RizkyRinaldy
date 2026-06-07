# M. Rizky Rinaldy - 2510010102
print("+==================================+")
print("|  Konversi Nilai Angka ke Huruf   |")
print("+==================================+")
nilai = float(input("  Masukkan nilai angka (0-100): ")) 
 
if nilai >= 85: 
   huruf = "A" 
   ket = "Sangat Baik" 
elif nilai >= 70: 
   huruf = "B" 
   ket = "Baik" 
elif nilai >= 55: 
   huruf = "C" 
   ket = "Cukup" 
elif nilai >= 40: 
   huruf = "D" 
   ket = "Kurang" 
else: 
   huruf = "E" 
   ket = "Sangat Kurang" 

print("+==================================+")
print(f"| Nilai Angka    : {nilai:<16.1f}|")
print(f"| Nilai Huruf    : {huruf:<16}|")
print(f"| Keterangan     : {ket:<16}|")
print("+==================================+")
print()
print("+==================================+")
print("| Dosen: Bpk. Yusri Ikhwani, M.Kom |")
print("|   2510010102 - M. Rizky Rinaldy  |")
print("+==================================+")

input()