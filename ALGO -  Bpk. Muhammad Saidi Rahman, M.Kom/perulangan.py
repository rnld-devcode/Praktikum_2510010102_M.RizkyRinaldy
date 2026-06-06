#Contoh  menggunakan range, (angka pertama, batas angka berhenti looping)
#for i in range(1, 4):
    #print(f"Juara ke-{i}")


#Mengambil Data dari sebuah Variabel dan melakukan For Looping
#mataKuliah = ["Algoritma Pemprograman", "Sistem Basis Data", "Logika Matematika", "Pengantar Teknologi Informasi"]

#for m in mataKuliah:
    #print(f"{m} Merupakan Mata Kuliah wajib pada jurusan Teknik Informatika")

#while looping

angka = int(input(f"Anda Mau Menampilkan Perkalian Berapa (1-100): "))
batas = int(input(f"Perkalian sampai berapa kali: "))

pengali = 1
hasil = angka * pengali
while angka != 0:
    print(f"{angka} x {pengali} = {hasil}")
    pengali = pengali + 1
    hasil = angka * pengali
    if pengali > batas:
        break