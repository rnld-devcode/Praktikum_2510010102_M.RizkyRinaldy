#2510010102 - M. Rizky Rinaldy
print("+==================================+")
print("|          Validasi Input          |")
print("+==================================+")
  
while True: 
    try: 
        angka = float(input(" ==> Masukkan angka: ")) 
        break 
    except ValueError: 
        print("+----------------------------------+")
        print("| ❌ Input bukan angka, coba lagi! |") 
        print("+----------------------------------+")
 
print("+----------------------------------+")
print(f"| ✓ Anda memasukkan : {angka:<10}   |") 
print(f"|  Kuadratnya       : {angka ** 2:<10}   |") 
print("+----------------------------------+")
print()
print("+==================================+")
print("| Dosen: Bpk. Yusri Ikhwani, M.Kom |")
print("|   2510010102 - M. Rizky Rinaldy  |")
print("+==================================+")

input() 