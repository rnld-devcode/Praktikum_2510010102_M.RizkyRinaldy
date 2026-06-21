#2510010102 - M. Rizky Rinaldy
print("+====================================================+")
print("|                     Pembaca File                   |")
print("+====================================================+")
nama_file = input(" ==> Nama file: ") 
  
try: 
    with open(nama_file, "r") as f: 
        isi = f.read() 
    print("+----------------------------------------------------+")
    print("|             --- >>> Isi File <<< ---               |") 
    print("+----------------------------------------------------+")
    print(isi) 
except FileNotFoundError: 
    print("+----------------------------------------------------+")
    print(f"| ❌ File '{nama_file:<23}' tidak ditemukan. |") 
    print("+----------------------------------------------------+")
    pilih = input(" ==> Buat file baru? (Y/T): ").upper() 
    if pilih == "Y": 
        konten = input(" --> Tulis isi file: ") 
        with open(nama_file, "w") as f: 
            f.write(konten) 
        print("+----------------------------------------------------+")
        print(f"| ✓ File '{nama_file:<31}' dibuat. |") 
        print("+----------------------------------------------------+")

except PermissionError: 
    print("+----------------------------------------------------+")
    print(f"❌ Tidak punya izin akses ke '{nama_file}'.") 
    print("+----------------------------------------------------+")

except Exception as e: 
    print("+----------------------------------------------------+")
    print(f"❌ Error tak terduga: {type(e).__name__}: {e}") 
    print("+----------------------------------------------------+")

print()
print("+====================================================+")
print("|          Dosen: Bpk. Yusri Ikhwani, M.Kom          |")
print("|            2510010102 - M. Rizky Rinaldy           |")
print("+====================================================+")

input() 