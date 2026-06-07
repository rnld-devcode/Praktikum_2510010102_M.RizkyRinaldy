import random 
# M. Rizky Rinaldy - 2510010102
print("+===============================================+")
print("|               Game Tebak Angka                |")
print("+===============================================+") 
print("|       Saya memikirkan angka 1 sampai 20       |") 

angka_rahasia = random.randint(1, 20) 
percobaan = 0 
  
while True: 
   print("+-----------------------------------------------+")
   print(f"|                 Percobaan Ke-{percobaan}                |")
   print("|                                               |")
   tebakan = int(input("| Tebakan Anda: ")) 
   print("|                                               |")
   percobaan += 1 
    
   if tebakan == angka_rahasia: 
        print(f"|     Benar! Anda menebak dalam {percobaan} percobaan.    |") 
        break 
   elif tebakan < angka_rahasia: 
        print(f"|           Terlalu kecil, coba lagi!           |") 
   else: 
        print(f"|           Terlalu besar, coba lagi!           |") 
print("+===============================================+")
print()
print("+===============================================+")
print("|        Dosen: Bpk. Yusri Ikhwani, M.Kom       |")
print("|          2510010102 - M. Rizky Rinaldy        |")
print("+===============================================+")

input()