#Oerator Aritmatika
#+,   Penjumlahan       : Melakukan Operasi Penjumlahan
#-,   Pengurangan       : Melakukan Operasi Pengurangan
#*,   Perkalian         : Melakukan Operasi Perkalian
#/,   Pembagian,        : Melakukan Operasi Pembagian
#//,  Pembagian Bulat,  : Melakukan Operasi Pembagian Bulat
#%,   Modulus,          : Menghitung sisa hasil pembagian
#**,  Eksponen,         : Melakukan Operasi Perpangkatan

print("Materi Pertemuan02 - Contoh 1: Operator Aritmatika")
bil1 = float(input("Masukan bilangan pertama: "))
bil2 = float(input("Masukan bilangan kedua: "))

hasiltambah = bil1 + bil2
hasilkurang = bil1 - bil2
hasilkali   = bil1 * bil2
hasilbagi   = bil1 / bil2
hasilbagi2  = bil1 // bil2
hasilmod    = bil1 % bil2
hasilpangkat= bil1 ** bil2

print("Hasil Penjumlahan : ", hasiltambah)
print("Hasil Pengurangan : ", hasilkurang)
print("Hasil Perkalian : ", hasilkali)
print("Hasil Pembagian : ", hasilbagi)
print("Hasil Pembagian Bulat : ", hasilbagi2)
print("Hasil Sisa Bagi : ", hasilmod)
print("Hasil Pangkat : ", hasilpangkat)
