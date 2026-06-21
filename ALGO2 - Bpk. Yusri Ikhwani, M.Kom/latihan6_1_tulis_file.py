#2510010102 - M. Rizky Rinaldy
print("+==================================+")
print("|       Menulis File Biodata       |")
print("+==================================+")
nama    = input(" --> Nama    : ") 
umur    = input(" --> Umur    : ") 
alamat  = input(" --> Alamat  : ") 
hobi    = input(" --> Hobi    : ") 
  
with open("biodata.txt", "w") as f: 
    f.write("========== BIODATA ==========\n") 

    f.write(f"Nama   : {nama}\n") 
    f.write(f"Umur   : {umur}\n") 
    f.write(f"Alamat : {alamat}\n") 
    f.write(f"Hobi   : {hobi}\n") 

print("+----------------------------------+")
print("|File 'biodata.txt' berhasil dibuat!")
print("+----------------------------------+")
print()
print("+==================================+")
print("| Dosen: Bpk. Yusri Ikhwani, M.Kom |")
print("|   2510010102 - M. Rizky Rinaldy  |")
print("+==================================+")

input() 