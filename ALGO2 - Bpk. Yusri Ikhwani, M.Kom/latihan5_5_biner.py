#2510010102 - M. Rizky Rinaldy
def desimal_to_biner(n): 
    if n == 0: 
        return "0" 
    biner = "" 
    proses = [] 
    while n > 0: 
        sisa = n % 2 
        proses.append(f"{n:8} / 2 = {n//2:<8} sisa {sisa:<1}  |") 
        biner = str(sisa) + biner 
        n = n // 2 
    return biner, proses 
  
print("+==================================+")
print("|    Konversi Desimal ke Biner     |")
print("+==================================+")
n = int(input("   Masukkan bilangan desimal: ")) 
  
biner, proses = desimal_to_biner(n) 

print("+----------------------------------+") 
print("|         Proses konversi:         |") 
print("+----------------------------------+")
for p in proses: 
    print(f"|  {p}") 
print("+----------------------------------+")
print(f"| Hasil     : {biner:12} (biner) |") 
print(f"| Verifikasi: {int(biner, 2):<10} (desimal) |") 
print("+----------------------------------+")
print()
print("+==================================+")
print("| Dosen: Bpk. Yusri Ikhwani, M.Kom |")
print("|   2510010102 - M. Rizky Rinaldy  |")
print("+==================================+")

input() 