#2510010102 - M. Rizky Rinaldy
def celcius_to_fahrenheit(c): 
    return (c * 9/5) + 32 
def celcius_to_reamur(c): 
    return c * 4/5 
def celcius_to_kelvin(c): 
    return c + 273.15 

print("+==================================+")
print("|           Konversi Suhu          |")
print("|    (Celcius, Reamur, Kelvin)     |")
print("+==================================+")
c = float(input(" Masukkan suhu dalam Celcius: ")) 
  
print("+==================================+")
print("|          HasilKonversi           |")
print("+==================================+")
print(f"|        {c}°C = {celcius_to_fahrenheit(c):6.2f}°F         |") 
print(f"|        {c}°C = {celcius_to_reamur(c):6.2f}°R         |") 
print(f"|        {c}°C = {celcius_to_kelvin(c):6.2f} K         |") 
print("+----------------------------------+")
print()
print("+==================================+")
print("| Dosen: Bpk. Yusri Ikhwani, M.Kom |")
print("|   2510010102 - M. Rizky Rinaldy  |")
print("+==================================+")

input()