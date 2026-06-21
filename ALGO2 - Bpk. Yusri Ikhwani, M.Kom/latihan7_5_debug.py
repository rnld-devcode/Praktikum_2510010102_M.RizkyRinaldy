#2510010102 - M. Rizky Rinaldy
def rata_rata(data): 
    print(f" >-< [DEBUG] Data masuk : {data}") 
    print(f" >-< [DEBUG] Jumlah item: {len(data)}") 
  
    total = 0 
    for i, angka in enumerate(data): 
        total += angka 
        print(f" >-< [DEBUG] Iterasi {i}: total = {total}") 
  
    if len(data) == 0: 
        print(">-< [DEBUG] Data kosong, return 0") 
        return 0 
  
    hasil = total / len(data) 
    print(f" >-< [DEBUG] Total akhir: {total}") 
    print(f" >-< [DEBUG] Rata-rata : {hasil}") 
    return hasil 

print("+====================================================+")
print("|            Program Rata-rata (with debug)          |")
print("+====================================================+")
  
data1 = [80, 75, 90, 85, 70] 
print(f"|  ==> Data: {data1}") 
print("+----------------------------------------------------+")

r = rata_rata(data1) 
print("+----------------------------------------------------+")
print(f"|           ==> Rata-rata = {r:<25}|")
print("+----------------------------------------------------+")

print()
print("+====================================================+")
print("|          Dosen: Bpk. Yusri Ikhwani, M.Kom          |")
print("|            2510010102 - M. Rizky Rinaldy           |")
print("+====================================================+")

input() 