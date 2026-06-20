#2510010102 - M. Rizky Rinaldy
def is_prima(n): 
    if n < 2: 
        return False 
    for i in range(2, int(n ** 0.5) + 1): 
          if n % i == 0: 
                return False 
    return True 

print("+=====================================+")
print("|        Daftar Bilangan Prima        |")
print("+=====================================+")
batas = int(input("     Masukkan batas atas: ")) 

print("+=====================================+")
print(f"|Bilangan prima dari 1 sampai {batas:7}:|")
print("+=====================================+")

hasil = [] 
for i in range(1, batas + 1): 
     if is_prima(i): 
         hasil.append(i) 

print(f"| {hasil} |") 
print("+-------------------------------------+")
print(f"|       Total: {len(hasil):2} bilangan prima      |") 
print("+-------------------------------------+")
print()
print("+=====================================+")
print("|  Dosen: Bpk. Yusri Ikhwani, M.Kom   |")
print("|    2510010102 - M. Rizky Rinaldy    |")
print("+=====================================+")

input()