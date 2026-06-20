#2510010102 - M. Rizky Rinaldy
def faktorial(n): 
    if n <= 1: 
        return 1 
    return n * faktorial(n - 1) 
  
def pangkat(basis, eksponen): 
    if eksponen == 0: 
        return 1 
    return basis * pangkat(basis, eksponen - 1) 

print("+==================================+")
print("|          Fungsi Rekursif         |")
print("+==================================+")
n = int(input("     Hitung faktorial dari: ")) 
b = int(input("     Basis pangkat        : ")) 
e = int(input("     Eksponen pangkat     : ")) 
  
print("+==================================+")
print("|        Hasil Perhitungan         |")
print("+==================================+")
print(f"|      {n:>6}!  = {faktorial(n):<10}       |") 
print(f"|       {b:3}^{e:<3} = {pangkat(b, e):<10}       |") 
print("+----------------------------------+")
print()
print("+==================================+")
print("| Dosen: Bpk. Yusri Ikhwani, M.Kom |")
print("|   2510010102 - M. Rizky Rinaldy  |")
print("+==================================+")

input()