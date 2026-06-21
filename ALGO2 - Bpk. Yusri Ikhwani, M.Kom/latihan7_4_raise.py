#2510010102 - M. Rizky Rinaldy
def validasi_umur(umur): 
    if not isinstance(umur, (int, float)): 
        raise TypeError("Umur harus berupa angka") 
    if umur < 0: 
        raise ValueError("Umur tidak boleh negatif") 
    if umur > 120: 
        raise ValueError("Umur tidak realistis (>120)") 
    return True 

print("+==========================================+")
print("|              Validasi Umur               |")
print("+==========================================+") 
  
try: 
    umur = int(input(" ==> Umur Anda: ")) 
    validasi_umur(umur) 
    print("+------------------------------------------+")
    print(f"|         ✓ Umur {umur:<11} valid         |") 
    print("+------------------------------------------+")

  
    if umur < 17: 
        print("+------------------------------------------+")
        print("|    >>> Kategori: Anak-anak/Remaja <<<    |") 
    elif umur < 60: 
        print("+------------------------------------------+")
        print("|         >>> Kategori: Dewasa <<<         |") 
    else: 
        print("+------------------------------------------+")
        print("|         >>> Kategori: Lansia <<<         |") 
except ValueError as e: 
    print("+------------------------------------------+")
    print(f"|  ❌ Error:  {e}  |") 
except TypeError as e: 
    print("+------------------------------------------+")
    print(f"|  ❌ Error:  {e}  |")


print("+------------------------------------------+")
print()
print("+==========================================+")
print("|     Dosen: Bpk. Yusri Ikhwani, M.Kom     |")
print("|       2510010102 - M. Rizky Rinaldy      |")
print("+==========================================+")

input() 