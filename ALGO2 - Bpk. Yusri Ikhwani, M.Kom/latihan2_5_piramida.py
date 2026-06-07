# M. Rizky Rinaldy - 2510010102
print("+============================================+")
print("|             Pola Piramida Angka            |")
print("+============================================+")
tinggi = int(input("          Masukkan tinggi piramida: ")) 
print("+============================================+")
print(f"|    Piramida Angka dengan Tinggi {tinggi} baris   |")
print("+--------------------------------------------+") 
for i in range(1, tinggi + 1): 

    print(" " * (tinggi - i) * 2, end="")   

    for j in range(1, i + 1): 
        print(f"{j:<2}", end="") 
        
    for j in range(i - 1, 0, -1): 
        print(f"{j:<2}", end="") 
    
    print()
print("+============================================+")
print()
print("+============================================+")
print("|      Dosen: Bpk. Yusri Ikhwani, M.Kom      |")
print("|        2510010102 - M. Rizky Rinaldy       |")
print("+============================================+")

input()