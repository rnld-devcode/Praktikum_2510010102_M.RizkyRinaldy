#Penggunaan Percabangan multiply kondisi if-elif-else 

#Data Valid
username_valid = str("dosen")
password_valid = str("dosen123")
#Data Input
username_input = str(input("Masukkan Username Anda: "))
password_input = str(input("Masukkan Password Anda: "))
print("\n")

#Login
if username_valid == username_input and password_valid == password_input:
    #Input Nilai Tugas, Kehadiran, UTS, dan UAS.
    print(f"Maukkan Hasil Penilaian Selama Satu Semester(0-100): ")
    nilai_tugas = float(input("Nilai Tugas: "))
    nilai_hadir = float(input("Nilai Kehadiran: "))
    nilai_uts = float(input("Nilai UTS: "))
    nilai_uas = float(input("Nilai UAS: "))
    print("\n")
    
    #Perhitungan Nilai Akhir
    nilai_akhir = float((nilai_tugas * 0.3) + (nilai_hadir * 0.1) + (nilai_uts * 0.25) + (nilai_uas * 0.35))
    print(f"Nilai Akhir Mahasiswa adalah: {nilai_akhir}")
    print("\n")

    #Menentukan Kelulusan dengan Nilai Akhirr
    if nilai_akhir >= 80 and nilai_akhir <= 100:
        predikat_huruf = "A"
    elif nilai_akhir >= 75 and nilai_akhir <= 79:
        predikat_huruf = "B+"
    elif nilai_akhir >= 70 and nilai_akhir <= 74:
        predikat_huruf = "B"
    elif nilai_akhir >= 65 and nilai_akhir <= 69:
        predikat_huruf = "C+"
    elif nilai_akhir >= 60 and nilai_akhir <= 64:
        predikat_huruf = "C"
    elif nilai_akhir >= 50 and nilai_akhir <= 59:
        predikat_huruf = "D"
    elif nilai_akhir >= 0 and nilai_akhir <= 49:
        predikat_huruf = "E"
    else:
        print(f"Nilai Akhir Tidak Valid")

    print("Nilai Akhir Mahasiswa :", nilai_akhir)
    print("Predikat Huruf:", predikat_huruf)

    if nilai_akhir >= 60 and nilai_akhir <= 100:
        print("Selamat Anda Lulus")
    else:
        print("Anda Tidak Lulus")
else:
    print("Username dan Password tidak sesuai")
    
#Jika Program Berhasil akan Tampil
print("\n")
print("<===Selamat Programnya Berhasil===>")
print("\n")