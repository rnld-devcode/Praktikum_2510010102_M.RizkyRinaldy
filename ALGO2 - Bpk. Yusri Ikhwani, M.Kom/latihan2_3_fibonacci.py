# M. Rizky Rinaldy - 2510010102
print("+===============================================+")
print("|                Deret Fibonacci                |")
print("+===============================================+")
n = int(input("             Masukkan jumlah suku: ")) 
print("+===============================================+")
print(f"|     Deret Fibonacci dari suku 1 hingga {n:<7}|")
print("+-----------------------------------------------+") 
a, b = 0, 1 
print("|", end=" ")
for i in range(n): 
   print(a, end=" ") 
   a, b = b, a + b 
print("|")
print("+===============================================+")
print()
print("+===============================================+")
print("|        Dosen: Bpk. Yusri Ikhwani, M.Kom       |")
print("|          2510010102 - M. Rizky Rinaldy        |")
print("+===============================================+")

input()