#Dictionary Penyimpanan Data
data_mhs = {
    "2510010102": {
        "nama": "M. Rizky Rinaldy",
        "npm": "2510010102",
        "prodi": "Teknik Informatika",
        "semester": "2"
    },
    "2510010499": {
        "nama": "Madhiyah",
        "npm": "2510010499",
        "prodi": "Teknik Informatika",
        "semester": "2",
    },
    "2510010032": {
        "nama": "Abdul Haiyi",
        "npm": "2510010032",
        "prodi": "Teknik Informatika",
        "semester": "2",
    },
    "2510020134": {
        "nama": "Rizky Putra Nugraha",
        "npm": "2510020134",
        "prodi": "Sistem Informasi",
        "semester": "2",
    },
}

#Output Data
search = input("Masukkan NPM Mahasiswa: ")
print(f"Data Mahasiswa: \n{data_mhs[search]}") #Akses nilai dengan key 'nama'