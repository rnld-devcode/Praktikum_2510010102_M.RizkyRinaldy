# M. Rizky Rinaldy - 2510010102
print("+===============================================+")
print("|              Kalkulator Faktorial             |")
print("+===============================================+")
n = int(input("         Masukkan bilangan bulat positif: ")) 
print("+===============================================+")
print(f"|            Hasil Faktorial dari {n:<8}      |")
print("+-----------------------------------------------+")
if n < 0: 
    print("|  Faktorial hanya untuk bilangan non-negatif!  |") 
else: 
    hasil = 1 
    proses = "" 
    for i in range(1, n + 1): 
       hasil *= i 
       proses += f"{i}" 
       if i < n: 
            proses += " x " 
    if n == 0: 
         print(f"0! = 1") 
    else: 
        print(f"|{n}! = {proses} = {hasil:<5}|")
print("+===============================================+")
print()
print("+===============================================+")
print("|        Dosen: Bpk. Yusri Ikhwani, M.Kom       |")
print("|          2510010102 - M. Rizky Rinaldy        |")
print("+===============================================+")

input()