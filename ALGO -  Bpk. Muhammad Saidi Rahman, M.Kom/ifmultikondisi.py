nilai = int(input("Masukkan Nilai Mahasiswa: "))

if nilai >= 90:
    huruf = "A"
elif nilai >= 80:
    huruf = "B"
elif nilai >= 70:
    huruf = "C"
else:
    huruf = "D/E"

print("Nilai Anda adalah: ", nilai)
print("Grade Anda Adalah ", huruf)