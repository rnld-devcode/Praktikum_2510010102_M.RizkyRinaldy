#Penggunaan Percabangan (seleksi) if-else

#if (kondisi) :
#   Perintah yang dijalankan jika kondisi benar
#else
#   Perintah yang dijalankan jika kondisi salah

#"Case Nilai Akhir"
nilaiakhir =float(input("Masukkan nilai akhir anda: "))
if nilaiakhir >= 60 and nilaiakhir <=100: #menggunakan operator and
    print("Selamat, anda Lulus!!! Teruslah berkembang menjadi lebih baik")
else:
    print("Sementara ini Anda belum lulus, tetap semangat!!!")

print("Program Selesai")