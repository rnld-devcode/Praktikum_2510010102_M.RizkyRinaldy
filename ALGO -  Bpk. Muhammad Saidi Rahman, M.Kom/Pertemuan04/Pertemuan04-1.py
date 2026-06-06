#Perulangan dengan Impor Random

import random #Import fungsi bilangan random
print("Program Tebak Angka Sederhana")
print("Pilih level tebak angka:")
print(". 1.Mudah (0-10) \n. 2.Standar (0-20) \n. 3.Sulit (0-30) \n. 4.Mustahil(0-1000) \n")

#user input level
level = int(input("Pilih Tingkat Kesulitan (1-3): "))

#Penggunaan Fungsi IF selection
if level == 1:
    nilaiMaks = 10
    angka = random.randint(0, 10)
if level == 2:
    nilaiMaks = 20
    angka = random.randint(0, 20)
if level == 3:
    nilaiMaks = 30
    angka = random.randint(0, 30)
if level == 4:
    nilaiMaks = 1000
    angka = random.randint(0, 1000)

#Penggunaan Fungsi Perulangan (For)
print(f"Anda hanya punya 3 kesempatan \nGunakan sebaik mungkin \n")
for ulang in range(1, 4):
    print("Kesempatan ke-", ulang, "untuk menebak angka!")
    tebak = int(input(f"Input nilai acak dari 0-{nilaiMaks}: "))
    if tebak > nilaiMaks or tebak < 0:
        print(f"Mohon Masukkan Angka Antara (0-{nilaiMaks})\n")
    elif tebak == angka:
        print("Tebakan anda benar!!!\n")
        break #Keluar dari Perulangan
    elif tebak > angka:
        print("Nilai Tebakan anda terlalu tinggi\n")
    elif tebak < angka:
        print("Nilai Tebakan anda terlalu rendah\n")
    else:
        print(f"Inputan tidak Valid")

print(f"Program Selesai")