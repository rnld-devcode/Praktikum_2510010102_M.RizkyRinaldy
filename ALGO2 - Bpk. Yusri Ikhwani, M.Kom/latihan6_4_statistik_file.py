#2510010102 - M. Rizky Rinaldy
print("+=================================================+")
print("|              Statistik File Teks                |")
print("+=================================================+")
nama_file = input(" --> Nama file: ") 
  
try: 
    with open(nama_file, "r") as f: 
        isi = f.read() 
  
    jumlah_baris    = isi.count("\n") + (0 if isi.endswith("\n") else 1) 
    jumlah_kata     = len(isi.split()) 
    jumlah_karakter = len(isi) 
    jumlah_huruf    = sum(1 for c in isi if c.isalpha()) 
   
    print("+-------------------------------------------------+")
    print(f" ==> File            : {nama_file}") 
    print(f" ==> Jumlah baris    : {jumlah_baris}") 
    print(f" ==> Jumlah kata     : {jumlah_kata}") 
    print(f" ==> Jumlah karakter : {jumlah_karakter}") 
    print(f" ==> Jumlah huruf    : {jumlah_huruf}") 
except FileNotFoundError: 
    print(f"File '{nama_file}' tidak ditemukan!")
print("+-------------------------------------------------+")
print()
print("+=================================================+")
print("|        Dosen: Bpk. Yusri Ikhwani, M.Kom         |")
print("|          2510010102 - M. Rizky Rinaldy          |")
print("+=================================================+")

input() 