#2510010102 - M. Rizky Rinaldy
daftar_belanja = [] 

while True: 
    print()
    print("+==================================+")
    print("|        MENU DAFTAR BELANJA       |")
    print("+==================================+")
    print("| 1. Tambah Item                   |") 
    print("| 2. Lihat Daftar                  |") 
    print("| 3. Hapus Item                    |") 
    print("| 4. Keluar                        |") 
    print("+==================================+")
    pilih = input("            Pilihan: ") 
    print("+----------------------------------+")
    if pilih == "1": 
        item = input("| Nama item: ") 
        daftar_belanja.append(item) 
        print("+----------------------------------+")
        print(f"|'{item:>11}' ditambahkan         |") 
        print("+----------------------------------+")
    elif pilih == "2": 
        if len(daftar_belanja) == 0: 
            print("|       Daftar masih kosong        |")
        else: 
            print("|            Isi daftar:           |") 
            print("+----------------------------------+")
        for i, item in enumerate(daftar_belanja, 1): 
            print(f"|  {i}. {item:<29}|") 
        print("+----------------------------------+")
    elif pilih == "3": 
        item = input("| Item yang ingin dihapus: ") 
        if item in daftar_belanja: 
            daftar_belanja.remove(item) 
            print("+----------------------------------+")
            print(f"|'{item:>11}' dihapus             |") 
            print("+----------------------------------+")
        else: 
            print("+----------------------------------+")
            print("|       Item tidak ditemukan       |")
            print("+----------------------------------+")
    elif pilih == "4":
        break 
print()
print("+==================================+")
print("| Dosen: Bpk. Yusri Ikhwani, M.Kom |")
print("|   2510010102 - M. Rizky Rinaldy  |")
print("+==================================+")

input()