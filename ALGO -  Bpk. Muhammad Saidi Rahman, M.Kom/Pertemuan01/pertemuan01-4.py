#operator aritmatika digunakan untuk melakukan sebuah proses seperti perhitungan
#simbolnya: +, -, *, /, mod

#Luas Persegi Panjang --> luas = p * l
#Keliling Persegi Panjang --> keliling = 2 * (p + l)
panjang = float(input("Masukkan nilai panjang: "))
lebar = float(input("Masukkan nilai Lebar: "))
luas = panjang * lebar #operator perkalian(*)
keliling = 2 * (panjang + lebar) #operator perkalian(*) dan penjumlahan(+)

print("Hasil perhitungan luas persegi panjang: ")
print("Panjang : ", panjang)
print("Lebar : ", lebar)
print("Luas Persegi Panjang : ", luas)
print("Keliling Persegi Panjang : ", keliling)
