#2510010102 - M. Rizky Rinaldy
def is_palindrom(teks): 
    bersih = teks.replace(" ", "").lower() 
    return bersih == bersih[::-1] 

print("+==================================+")
print("|        Pengecek Palindrom        |")
print("+==================================+")
teks = input("   Masukkan kata/kalimat: ") 
if is_palindrom(teks): 
   print(f"  '{teks:11}' adalah PALINDROM") 
else: 
   print(f"| '{teks:11}' BUKAN palindrom |") 

print("+------------ Demo ----------------+")
contoh = ["tamat", "katak", "python", "malam", "saya"] 
for c in contoh: 
   status = "YA" if is_palindrom(c) else "BUKAN" 
   print(f"| '{c:11}' -> {status:5} palindrom |") 
print("+----------------------------------+")
print()
print("+==================================+")
print("| Dosen: Bpk. Yusri Ikhwani, M.Kom |")
print("|   2510010102 - M. Rizky Rinaldy  |")
print("+==================================+")

input() 