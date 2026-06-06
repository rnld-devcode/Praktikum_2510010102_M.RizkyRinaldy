#program perhitungan gaji karyawan

#Input
nama_karyawan = input("Masukkan Nama: ")
gaji_pokok = int(input("Masukkan Gaji Pokok Karyawan: "))
status = input("Status Perkawinan (M=Menikah, B=Belum Menikah): ")
jumlah_anak = input("Jumlah Anak Karyawan: ")

#Menentukan Jumlah Tunjangan Status
if status == "M" or status == "m":
    tunjangan_status = 0.1 * gaji_pokok
elif status == "B" or status == "b":
    tunjangan = 0
else:
    print("Status Tidak Valid")

#Menentukan Jumlah Tunjangan Anak
if jumlah_anak <= 2:
    tunjangan_anak = jumlah_anak * (0.05 * gaji_pokok)
else:
    tunjangan_anak = 2 * (0.05 * gaji_pokok)

total_tunjangan = tunjangan_status + tunjangan_anak

#Menentukan Jumlah Potongan Pajak Penghasilan
if gaji_pokok >= 5000000:
    pph = 0.05 * (gaji_pokok + total_tunjangan)
else:
    pph = 0.025 * (gaji_pokok + total_tunjangan)

gaji_bersih = gaji_pokok + total_tunjangan - pph

#Output
print("Nama Karyawan    : ", nama_karyawan)
print("Gaji Pokok       : ", gaji_pokok)
print("Total Tunjangan  : ", total_tunjangan)
print("Total Potongan   : ", pph)
print("Gaji Bersih      : ", gaji_bersih)
