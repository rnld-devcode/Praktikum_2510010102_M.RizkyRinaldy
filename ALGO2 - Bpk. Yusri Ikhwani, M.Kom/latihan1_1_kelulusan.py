# M. Rizky Rinaldy - 2510010102
print("===== Program Cek Kelulusan =====")
nama = input("Masukkan nama mahasiswa : ")
nilai = float(input("Masukkan nilai akhir : "))

if nilai >= 60:
    status = "LULUS"
else:
    status = "TIDAK LULUS"

print("-" * 35)
print(f"Nama: {nama}")
print(f"Nilai: {nilai}")
print(f"Status: {status}")