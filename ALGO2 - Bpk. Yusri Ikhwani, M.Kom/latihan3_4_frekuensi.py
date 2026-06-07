#2510010102 - M. Rizky Rinaldy
print("+==================================+")
print("|         Frekuensi Huruf          |")
print("+==================================+")
kalimat = input("|Masukkan kalimat: ").lower() 
print("+----------------------------------+")
print()
frekuensi = {} 
for huruf in kalimat: 
    if huruf.isalpha(): 
        if huruf in frekuensi: 
            frekuensi[huruf] += 1 
        else: 
            frekuensi[huruf] = 1 
  
print("+==================================+")
print("|        Hasil Pengelompokan       |")
print("+==================================+")

for huruf in sorted(frekuensi.keys()): 
    print(f"|         '{huruf}' muncul {frekuensi[huruf]} kali        |")
print("+----------------------------------+")
print()
print("+==================================+")
print("| Dosen: Bpk. Yusri Ikhwani, M.Kom |")
print("|   2510010102 - M. Rizky Rinaldy  |")
print("+==================================+")

input()