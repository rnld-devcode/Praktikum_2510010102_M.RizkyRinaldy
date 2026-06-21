#2510010102 - M. Rizky Rinaldy
import os 
  
FILE = "mahasiswa.csv" 
  
def tambah_data(): 
    nim     = input(" --> NIM      : ") 
    nama    = input(" --> Nama     : ") 
    jurusan = input(" --> Jurusan  : ") 
    ipk     = input(" --> IPK      : ") 
 
    header = not os.path.exists(FILE) 
    with open(FILE, "a") as f: 
        if header: 
            f.write("NIM,Nama,Jurusan,IPK\n") 
        f.write(f"{nim},{nama},{jurusan},{ipk}\n") 
    print("+-----------------------------------------------------------+")
    print("|                 >>> ✓ Data tersimpan <<<                  |") 
    print("+-----------------------------------------------------------+")

  
def tampil_data(): 
    if not os.path.exists(FILE): 
        print("Belum ada data.") 
        return 
    with open(FILE, "r") as f: 
        print("+-----------------------------------------------------------+")
        for i, baris in enumerate(f): 
            data = baris.strip().split(",") 
            if i == 0: 
                print(f"{data[0]:12s} {data[1]:20s} {data[2]:20s} {data[3]:>5s}") 
                print("+-----------------------------------------------------------+")

            else: 
                print(f"{data[0]:12s} {data[1]:20s} {data[2]:20s} {data[3]:>5s}") 
        print("+-----------------------------------------------------------+")  

print("+===========================================================+")
print("|                 Datbase Sederhana (CSV)                   |")
print("+===========================================================+")
print("| >>> 1. Tambah Data") 
print("| >>> 2. Lihat Data") 
print("| >>> 3. Keluar") 
print("+-----------------------------------------------------------+")
while True: 
    p = input(" ==> Pilihan: ") 
    if   p == "1": tambah_data() 
    elif p == "2": tampil_data() 
    elif p == "3": break 
print()
print("+===========================================================+")
print("|             Dosen: Bpk. Yusri Ikhwani, M.Kom              |")
print("|               2510010102 - M. Rizky Rinaldy               |")
print("+===========================================================+")

input() 