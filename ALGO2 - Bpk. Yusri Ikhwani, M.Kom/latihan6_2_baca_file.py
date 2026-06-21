#2510010102 - M. Rizky Rinaldy
print("+==================================+")
print("|       Membaca File Biodata       |")
print("+==================================+")
  
try: 
    with open("biodata.txt", "r") as f: 
        isi = f.read() 
    print(isi) 
  
    print("+-----------Per Baris--------------+")
    with open("biodata.txt", "r") as f: 
        for nomor, baris in enumerate(f, 1): 
            print(f"Baris {nomor}: {baris.rstrip()}") 
except FileNotFoundError: 
    print("File tidak ditemukan! Jalankan latihan 6.1 terlebih dahulu.") 
print("+----------------------------------+")
print()
print("+==================================+")
print("| Dosen: Bpk. Yusri Ikhwani, M.Kom |")
print("|   2510010102 - M. Rizky Rinaldy  |")
print("+==================================+")

input() 