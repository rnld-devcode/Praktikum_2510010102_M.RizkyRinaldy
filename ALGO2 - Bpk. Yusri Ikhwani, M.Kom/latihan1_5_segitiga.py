# M. Rizky Rinaldy - 2510010102
print("+====================================+")
print("|      Penentu Jenis Segitiga        |")
print("+====================================+")
a = float(input("     Masukkan panjang sisi a : ")) 
b = float(input("     Masukkan panjang sisi b : ")) 
c = float(input("     Masukkan panjang sisi c : ")) 

# Validasi segitiga 
if (a + b) <= c or (a + c) <= b or (b + c) <= a: 
    print("Ketiga sisi TIDAK membentuk segitiga!") 
else: 
    if (a**2 + b**2 == c**2) or (a**2 + c**2 == b**2) or (b**2 + c**2 == a**2):
        jenis = "Segitiga Siku-Siku"
    elif a == b == c:
        jenis = "Segitiga Sama Sisi"
    elif a == b or a == c or b == c:
        jenis = "Segitiga Sama Kaki"
    else:
        jenis = "Segitiga Sembarang"

print("+====================================+")
print(f"|Jenis Segitiga : {jenis:<19}|") 
print("+====================================+")
if jenis == "Segitiga Siku-Siku":
    print("|               |\\                   |")
    print("|               | \\                  |")
    print("|               |  \\                 |")
    print("|               |___\\                |")
elif jenis == "Segitiga Sama Sisi":
    print("|                /\\                  |")
    print("|               /  \\                 |")
    print("|              /____\\                |")
elif jenis == "Segitiga Sama Kaki":
    print("|                /\\                  |")
    print("|               /  \\                 |")
    print("|              /    \\                |")
    print("|             /______\\               |")
elif jenis == "Segitiga Sembarang":
    print("|                /\\                  |")
    print("|               /  \\                 |")
    print("|             /     \\                |")
    print("|            /_______\\               |")
print("+====================================+")
print()
print("+====================================+")
print("|  Dosen: Bpk. Yusri Ikhwani, M.Kom  |")
print("|    2510010102 - M. Rizky Rinaldy   |")
print("+====================================+")

input()