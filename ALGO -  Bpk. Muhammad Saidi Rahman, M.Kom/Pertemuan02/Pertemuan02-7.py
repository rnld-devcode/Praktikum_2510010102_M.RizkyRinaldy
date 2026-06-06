#Penggunaan Percabangan (seleksi) if-else bersarang (nested if)

#if (kondisi) :
#   Perintah yang dijalankan jika kondisi benar
#else
#   Perintah yang dijalankan jika kondisi salah

#"Case Voucher Belanja"
username = input("Masukkan Username Anda: ")
password = input("Masukkan Password Anda: ")
if username == "admin" and password == "admin123":
    totalbelanja =float(input("Masukkan total belanja anda: "))
    if totalbelanja >= 1000000:
        potongan = 0.1 * totalbelanja
        print("Anda mendapat potongan sebesar : ", potongan)
    else:
        potongan = 0
        print("Tidak dapat potongan")
    totalbayar = totalbelanja - potongan
    print("Total bayar anda adalah : ", int(totalbayar))
else:
    print("Username dan password tidak sesuai di sistem")


