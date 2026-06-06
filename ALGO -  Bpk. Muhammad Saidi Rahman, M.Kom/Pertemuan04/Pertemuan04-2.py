#Perulangan dengan Fungsi While

import random

#Program Tebak Angka dengan sistem skor dan komentar
print("Program Tebak Angka Berhadiah!!!")

#Pilih angka acak antara 0-10
angka =  random.randint(0, 10)

#kontrol loop
lanjut = "y"

#jumlah percobaan yang sudah
percobaan = 1

#sistem skor: Mulai 100, berkurang setiap kesalahan
score = 100 #awal
penalty = 10 #Pengurang skor

while lanjut == "y" or lanjut == "Y":
    #Nomor Percobaan
    print(f"\nPercobaan ke-{percobaan}")

    #Input Tebakan
    tebak = int(input(f"Tebak Angka 0-10: "))

    #cek tebakan
    if tebak == angka:
        print("Tebakan anda benar!!!\n")
        #Menampilkan Skor Akhir
        print(f"Skor Anda: {score}")
        break
    elif tebak > angka:
        print("Nilai Tebakan anda terlalu tinggi")
    elif tebak < angka:
        print("Nilai Tebakan anda terlalu rendah")
    else:
        print(f"Inputan tidak Valid")

    #Pengurangan Skor
    score = max(0, score - penalty)

    #Pertanyaan untuk Looping
    percobaan = percobaan + 1
    lanjut = input("Mau Coba Lagi (y/t): ")

#tampilkan ringkasan permainan
print(f"Anda menebak angka dalam {percobaan} percobaan")

print(f"\nProgram Selesai")