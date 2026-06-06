#Operator Logika
#and,   Bernilai Benar jika kedua pernyataan Benar
#or,    Bernilai Benar jika salah satu pernyataan Benar
#not,   Membalikan hasil dari sebuah pernyataan

#tabel kebenaran
#p     q     p^q    pvq     !p     !q
#T     T      T      T      F      F
#T     F      F      T      F      T
#F     T      F      T      T      F
#F     F      F      F      T      T

print("Materi Pertemuan02 - Contoh 3: Operator Logika")

hasil1 = 10 > 6 and 7 < 5         #False
hasil2 = 15 < 7 or 7 > 4          #True
hasil3 = not(25==24) and 14 < 19  #True

print("Hasil dari 10 > 6 and 7 < 5 : ", hasil1)
print("Hasil dari 15 < 7 and 7 > 4 : ", hasil2)
print("Hasil dari not(25==24) and 14 < 19 : ", hasil3)

#Case Login menggunakan operator and
username = "rizky"
password = "060702"
hasil4 = username == "rinaldy" and password == "060702"
print("Hasil pengecekan login : ", hasil4)