#Menghitung Luas dan Keliling Lingkaran
#dengan rumus: luas = phi * r * r dan keliling = + 2 * phi * r
print("\n")
print("Program Perhitungan Luas dan Keliling Lingaran")
print("<======(l=phi*r*r)======(k=2*phi*r)======>")
print("<=========By_M.RizkyRinaldy=========>")
print("\n")

#nilai phi berdasarkan modul matematika di python
import math
phi = math.pi 
print("Nilai Phi pada perhitungan berikut adalah:", math.pi)

#User menginput panjang jari-jari
r = float(input("Masukkkan Panjang Jari-jari dalam (cm): "))

#Proses Perhitungan menggunakan operator Matematika (+, -, *, /)
luas = phi * r * r
keliling = 2 * phi * r

#Hasil Inputan Panjang Jari-jari
print("Panjang Jari-jari:", r, "cm")
print("\n")

#Hasil Perhitungan Luas Lingkaran
print("Luas Lingkaran:", luas, "cm")
print("Pembulatan:", round(luas), "cm")
print("\n")

#Hasil Perhitungan Keliling Lingkaran
print("Keliling Lingkaran:", keliling, "cm")
print("Pembulatan:", round(keliling), "cm")
print("\n")

#Jika Program Berhasil akan Tampil
print("<===Selamat Programnya Berhasil===>")