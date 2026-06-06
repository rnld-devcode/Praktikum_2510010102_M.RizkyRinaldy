#Penggunaan Percabangan (seleksi) if-else

#if (kondisi) :
#   Perintah yang dijalankan jika kondisi benar
#else
#   Perintah yang dijalankan jika kondisi salah

#"Case Voucher Belanja"
totalbelanja =float(input("Masukkan total belanja anda: "))
if totalbelanja >= 1000000:
    potongan = 0.1 * totalbelanja
    print("Anda mendapat potongan sebesar : ", potongan)
else:
    potongan = 0
    print("Tidak dapat potongan")

totalbayar = totalbelanja - potongan
print("Total bayar anda adalah : ", int(totalbayar))