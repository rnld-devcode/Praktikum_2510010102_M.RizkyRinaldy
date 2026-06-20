#2510010102 - M. Rizky Rinaldy
def bubble_sort(data): 
    n = len(data) 
    langkah = 1 
    for i in range(n): 
        swap = False 
        for j in range(0, n - i - 1): 
            if data[j] > data[j + 1]: 
                data[j], data[j + 1] = data[j + 1], data[j] 
                swap = True 
        print(f"|Iterasi {langkah:2}: {data}|") 
        langkah += 1 
        if not swap: 
            break 
    return data 

print("+==============================================+")
print("|             Algoritma Bubble Sort            |")
print("+==============================================+")
data =  [15, 27, 8, 42, 33, 19, 5, 66, 21] 
print(f"|                   Data Awal                  |") 
print(f"|      {data}      |") 
print("+----------------------------------------------+")

hasil = bubble_sort(data.copy()) 

print("+----------------------------------------------+")
print(f"|                  Data Akhir                  |") 
print(f"|      {hasil}      |")
print("+----------------------------------------------+")
print()
print("+==============================================+")
print("|       Dosen: Bpk. Yusri Ikhwani, M.Kom       |")
print("|         2510010102 - M. Rizky Rinaldy        |")
print("+==============================================+")

input()