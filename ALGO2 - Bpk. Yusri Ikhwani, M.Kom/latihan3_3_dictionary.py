#2510010102 - M. Rizky Rinaldy
print("+==================================+")
print("|       Input Data Mahasiswa       |")
print("+==================================+")
mahasiswa = { 
 "nim"    : input("| NIM       : "), 
 "nama"   : input("| Nama      : "), 
 "jurusan": input("| Jurusan   : "), 
 "ipk"    : float(input("| IPK       : ")) 
} 
print("+==================================+")
print()
print("+----------------------------------+")
print("|          DATA MAHASISWA          |") 
print("+----------------------------------+")

for key, value in mahasiswa.items(): 
    print(f"| {key.capitalize():10s}: {value:<20} |") 

if mahasiswa["ipk"] >= 3.5: 
     predikat = "Cumlaude" 
elif mahasiswa["ipk"] >= 3.0: 
    predikat = "Sangat Memuaskan" 
elif mahasiswa["ipk"] >= 2.5: 
    predikat = "Memuaskan" 
else: 
    predikat = "Cukup" 


print(f"| {'Predikat':10s}: {predikat:<20} |") 
print("+==================================+")
print()
print("+==================================+")
print("| Dosen: Bpk. Yusri Ikhwani, M.Kom |")
print("|   2510010102 - M. Rizky Rinaldy  |")
print("+==================================+")

input()