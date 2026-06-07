#2510010102 - M. Rizky Rinaldy
print("+==================================+")
print("|    Statistika Nilai Mahasiswa    |")
print("+==================================+")
n = int(input("| Jumlah data      : ")) 
print("+----------------------------------+")
nilai = [] 
for i in range(n): 
    x = float(input(f"| Nilai ke-{i+1}       : ")) 
    nilai.append(x) 
print("+----------------------------------+")

total    = sum(nilai) 
rata     = total / n 
tertinggi = max(nilai) 
terendah  = min(nilai) 

print("+==================================+")
print(f"| Jumlah Nilai     : {total:<14}|") 
print(f"| Rata-rata        : {rata:<14.2f}|") 
print(f"| Nilai Tertinggi  : {tertinggi:<14}|") 
print(f"| Nilai Terendah   : {terendah:<14}|") 
print("+==================================+")
print()
print("+==================================+")
print("| Dosen: Bpk. Yusri Ikhwani, M.Kom |")
print("|   2510010102 - M. Rizky Rinaldy  |")
print("+==================================+")

input()
