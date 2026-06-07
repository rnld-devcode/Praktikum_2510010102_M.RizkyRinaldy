# M. Rizky Rinaldy - 2510010102
print("+==================================+")
print("|         Kalkulator BMI           |")
print("+==================================+")
berat  = float(input("  Masukkan berat badan (kg) : ")) 
tinggi = float(input("  Masukkan tinggi badan (cm): ")) 
  
bmi = berat / ((tinggi / 100) ** 2) 

if bmi < 18.5: 
    kategori = "Kurus" 
elif bmi < 25: 
    kategori = "Normal" 
elif bmi < 30: 
    kategori = "Gemuk" 
else: 
    kategori = "Obesitas"   

print("+==================================+")
print(f"| Nilai BMI Anda: {bmi:<16.1f}|")
print(f"| Kategori      : {kategori:<16}|")
print("+==================================+")
print()
print("+==================================+")
print("| Dosen: Bpk. Yusri Ikhwani, M.Kom |")
print("|   2510010102 - M. Rizky Rinaldy  |")
print("+==================================+")