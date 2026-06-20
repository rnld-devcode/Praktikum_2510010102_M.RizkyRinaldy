#2510010102 - M. Rizky Rinaldy
def linear_search(data, target): 
    for i in range(len(data)): 
        if data[i] == target: 
            return i 
    return -1 

print("+==================================+")
print("|     Algoritma Linear Search      |")
print("+==================================+")
data =  [15, 27, 8, 42, 33, 19, 5, 66, 21] 
print(f"|             Data                |") 
print(f"|{data}|") 
print("+----------------------------------+")
target = int(input("            Cari angka: ")) 
posisi = linear_search(data, target) 

print("+----------------------------------+")
if posisi != -1: 
    print(f"|Angka {target:2} ditemukan pd indeks ke-{posisi:2}|") 
else: 
    print(f"| Angka {target} TIDAK ditemukan dalam data|")
print("+----------------------------------+")
print()
print("+==================================+")
print("| Dosen: Bpk. Yusri Ikhwani, M.Kom |")
print("|   2510010102 - M. Rizky Rinaldy  |")
print("+==================================+")

input()