#2510010102 - M. Rizky Rinaldy
print("+==========================================+")
print("|           Kalkulator Pembagian           |")
print("+==========================================+")
  
try: 
    a = float(input(" --> Pembilang : ")) 
    b = float(input(" --> Penyebut  : ")) 
    hasil = a / b 
except ZeroDivisionError: 
    print("+------------------------------------------+")
    print("| ❌ Error: Tidak bisa dibagi dengan nol!  |") 
    print("+------------------------------------------+")
except ValueError: 
    print("+------------------------------------------+")
    print("| ❌ Error: Input harus berupa angka!      |") 
    print("+------------------------------------------+")

else: 
    print("+------------------------------------------+")
    print(f"| ✓ {a:>6} / {b:<6} = {hasil:<20.4f} |") 
    print("+------------------------------------------+")

finally: 
    print("+------------------------------------------+")
    print("|         >>> (Proses selesai) <<<         |")
print("+------------------------------------------+")
print()
print("+==========================================+")
print("|     Dosen: Bpk. Yusri Ikhwani, M.Kom     |")
print("|       2510010102 - M. Rizky Rinaldy      |")
print("+==========================================+")

input() 