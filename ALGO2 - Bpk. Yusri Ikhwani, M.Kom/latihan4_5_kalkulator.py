#2510010102 - M. Rizky Rinaldy
def tambah(a, b):    return a + b
def kurang(a, b):    return a - b 
def kali(a, b):      return a * b 
def bagi(a, b): 
    if b == 0: 
        return None 
    return a / b 
  
def tampilkan_menu(): 
    print("+==================================+")
    print("|       Kalkulator Sederhana       |")
    print("+==================================+")
    print("| 1. Tambah                        |") 
    print("| 2. Kurang                        |") 
    print("| 3. Kali                          |") 
    print("| 4. Bagi                          |") 
    print("| 5. Keluar                        |") 
    print("+----------------------------------+")
  
while True: 
    tampilkan_menu() 
    pilih = input("             Pilihan : ") 
    if pilih == "5": 
        print("+----------------------------------+")
        print("|          Terima kasih!           |")
        print("+----------------------------------+")
        break 
    if pilih not in "1234": 
        print("+----------------------------------+")
        print("|      Pilihan tidak valid!        |") 
        print("+----------------------------------+")
        continue 
  
    a = float(input("       Angka pertama : ")) 
    b = float(input("       Angka kedua   : ")) 
  
    if pilih == "1":   hasil = tambah(a, b); op = "+" 
    elif pilih == "2": hasil = kurang(a, b); op = "-" 
    elif pilih == "3": hasil = kali(a, b);   op = "x" 
    else:              hasil = bagi(a, b);   op = "/" 
    
    print("+==================================+")
    print("|        Hasil Perhitungan         |")
    print("+==================================+")
    if hasil is None: 
         print("| Error: Pembagian dengan nol! |") 
    else: 
         print(f"|Hasil:{a:6} {op} {b:<6} = {hasil:10}|") 
print("+----------------------------------+")
print()
print("+==================================+")
print("| Dosen: Bpk. Yusri Ikhwani, M.Kom |")
print("|   2510010102 - M. Rizky Rinaldy  |")
print("+==================================+")

input()