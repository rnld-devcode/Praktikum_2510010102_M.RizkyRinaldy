#Membuat dictinary untuk menyimpan data mahasiswa
data_mhs ={}
jlh = int(input("Masukkan jumlah data yang akan diinput: "))
for i in range(1, jlh+1):
    #Input data
    nama = input("Masukkan Nama Mahasiswa: ")
    npm = input("Masukkan NPM Mahasiswa: ")
    prodi = input("Masukkan Prodi Mahasiswa: ")
    semester = int(input("Masukkan Semester Mahasiswa: "))

    #Memasukkan Data ke Dictionary
    data_mhs[i] = {
        "nama": nama,
        "npm": npm,
        "prodi": prodi,
        "semester": semester
    }

#Output Data
for i in range(1, jlh+1):
    print(f"\nData Mahasiswa ke-{i}")
    print(f"Nama Mahasiswa : {data_mhs[i]['nama']}")
    print(f"NPM            : {data_mhs[i]['npm']}")
    print(f"Prodi          : {data_mhs[i]['prodi']}")
    print(f"Semester       : {data_mhs[i]['semester']}")

print(f"\nSemua Data Telah Ditampilkan")