#2510010102 - M. Rizky Rinaldy
def fpb(a, b): 
    while b != 0: 
        a, b = b, a % b 
    return a 
  
def kpk(a, b): 
    return (a * b) // fpb(a, b) 

print("+==================================+")
print("|      Kalkulator FPB dan KPK      |")
print("+==================================+")
x = int(input("     Bilangan pertama: ")) 
y = int(input("     Bilangan kedua  : ")) 
  
print("+----------------------------------+")
print(f"|     FPB({x:3}, {y:<3}) =  {fpb(x, y):<6}      |") 
print(f"|     KPK({x:3}, {y:<3}) =  {kpk(x, y):<6}      |")
print("+----------------------------------+")
print()
print("+==================================+")
print("| Dosen: Bpk. Yusri Ikhwani, M.Kom |")
print("|   2510010102 - M. Rizky Rinaldy  |")
print("+==================================+")

input() 