#2510010102 - M. Rizky Rinaldy
from datetime import datetime 
print("+=================================================+")
print("|              Buku Catatan Harian                |")
print("+=================================================+")
  
while True: 
    print("Tulis catatan (ketik 'selesai' untuk berhenti):")
    catatan = input("\n --> Tulis: ") 
    if catatan.lower() == "selesai": 
        break 
  
    waktu = datetime.now().strftime("%Y-%m-%d %H:%M") 
  
    with open("catatan.txt", "a") as f: 
        f.write(f"[{waktu}] {catatan}\n") 

    print("+-------------------------------------------------+")
    print("|              >>> ✓ Tersimpan  <<<               |")
    print("+-------------------------------------------------+")


print()
print("+==============  Isi catatan.txt  ================+")

try: 
    with open("catatan.txt", "r") as f: 
        print(f.read()) 
except FileNotFoundError: 
    print("(belum ada catatan)")

print("+-------------------------------------------------+")
print()
print("+=================================================+")
print("|        Dosen: Bpk. Yusri Ikhwani, M.Kom         |")
print("|          2510010102 - M. Rizky Rinaldy          |")
print("+=================================================+")

input() 