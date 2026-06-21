# #️⃣ Repositori Praktikum ALGO - Bpk Yusri Ikhwani, M. Kom

<p align="left">
  <img src="https://img.shields.io/badge/Language-Python-blue" alt="Python">
  <img src="https://img.shields.io/badge/Database-MySQL-4479A1?style=flat&logo=mysql&logoColor=white" alt="MySQL">
  <img src="https://img.shields.io/badge/License-MIT-green" alt="License">
  <img src="https://img.shields.io/badge/OS-Windows-0078D4?style=flat&logo=windows&logoColor=white" alt="Windows">
  <img src="https://img.shields.io/badge/IDE-VS_Code-007ACC?style=flat&logo=visual-studio-code&logoColor=white" alt="VS Code">
  <img src="https://img.shields.io/badge/Status-Ongoing-yellow" alt="Status">
  <img src="https://img.shields.io/badge/Version-v1.0.0-blue" alt="Version">
</p>

---

> 💡 *"Code is like humor. When you have to explain it, it's bad."*  
> — **Cory House**

Repositori ini berisi kumpulan latihan praktikum pemrograman menggunakan bahasa **Python**, **Pascal**, dan **C++** (termasuk mata kuliah Algoritma Pemrograman dan Sistem Perancangan Basis Data). Semua kode di dalam repositori ini dibuat untuk memenuhi tugas akademik di program studi Informatika.

---

## 📝 Identitas Mahasiswa
* **Nama** : M. Rizky Rinaldy
* **NPM** : 2510010102
* **Program Studi** : Teknik Informatika

---

## 🗂️ Daftar Tugas Praktikum

Di bawah ini adalah daftar program yang telah digabungkan ke dalam repositori ini:

## BAB 1  PERCABANGAN (SELECTION) 
**Percabangan (Selection)** adalah struktur kontrol yang memungkinkan program mengambil keputusan berdasarkan kondisi tertentu. Dalam Python, percabangan diimplementasikan menggunakan kata kunci `if-elif-else`. Struktur ini sangat penting karena memberikan kemampuan pada program untuk bercabang sesuai logika yang diinginkan pemrogram. 
Bentuk umum percabangan `if-elif-else` adalah sebagai berikut:
```bash
if kondisi_1: 
    # blok kode jika kondisi_1 bernilai True 
elif kondisi_2: 
    # blok kode jika kondisi_2 bernilai True 
else: 
    # blok kode jika semua kondisi di atas bernilai False 
```

Operator relasi yang sering digunakan: == (sama dengan), != (tidak sama), > (lebih besar), < (lebih 
kecil),  >=  (lebih  besar  sama  dengan),  <=  (lebih  kecil  sama  dengan).  Sedangkan  operator  logika 
meliputi and, or, dan not. 
<table>
  <tr>
    <td width="60%">
      <h3>1.1  Program Penentu Kelulusan (<code>latihan1_1_kelulusan.py</code>)</h3>
      <ul>
        <li><b>Percabangan (Selection)</b></li>
        <li><b>Soal: </b> Buatlah program yang menentukan status kelulusan mahasiswa berdasarkan nilai akhir. Jika nilai >= 60 maka dinyatakan LULUS, selain itu TIDAK LULUS. </li>
        <li><details>
              <summary><b>🔍 Klik untuk melihat Source Code</b></summary> 
                <pre style="background: #f4f4f4; padding: 10px; border-radius: 5px; overflow-x: auto;"><code>
print("+==================================+")
print("|       Program Cek Kelulusan      |")
print("+==================================+")
nama =       input("  Masukkan nama mahasiswa : ")
nilai= float(input("  Masukkan nilai akhir    : "))

if nilai >= 60:
    status = "LULUS"
else:
    status = "TIDAK LULUS"
print("+==================================+")
print(f"| Nama      : {nama:<21}|")
print(f"| Nilai     : {nilai:<21.1f}|")
print(f"| Status    : {status:<21}|")
print("+==================================+")
print()
print("+==================================+")
print("| Dosen: Bpk. Yusri Ikhwani, M.Kom |")
print("|   2510010102 - M. Rizky Rinaldy  |")
print("+==================================+")

input()
              </code></pre>
            </details>
        </li>
      </ul>
    </td>
    <td width="40%">
      <img src="/ALGO2 - Bpk. Yusri Ikhwani, M.Kom/img/ProgramCekKelulusan.png" alt="Pratinjau_ProgramCekKelulusan">
      
  <a href="https://github.com/rnld-devcode/Praktikum_2510010102_M.RizkyRinaldy/blob/main/ALGO2%20-%20Bpk.%20Yusri%20Ikhwani%2C%20M.Kom/latihan1_1_kelulusan.py">
        <p align="center"><b>Program Pengecekan Kelulusan.</b></p>
  </a>
    </td>
  </tr>
  <tr>
    <td width="60%">
      <h3>1.2 Program Konversi Nilai ke Huruf (<code>latihan1_2_nilaihuruf.py</code>)</h3>
      <ul>
        <li><b>Percabangan (Selection)</b></li>
        <li><b>Soal: </b> Buatlah program yang mengkonversi nilai angka menjadi nilai huruf dengan ketentuan: A (>=85), B (70-84), C (55-69), D (40-54), E (<\40). </li>
        <li><details>
              <summary><b>🔍 Klik untuk melihat Source Code</b></summary>
                <pre style="background: #f4f4f4; padding: 10px; border-radius: 5px; overflow-x: auto;"><code>
print("+==================================+")
print("|  Konversi Nilai Angka ke Huruf   |")
print("+==================================+")
nilai = float(input("  Masukkan nilai angka (0-100): ")) 
 
if nilai >= 85: 
   huruf = "A" 
   ket   = "Sangat Baik" 
elif nilai >= 70: 
   huruf = "B" 
   ket   = "Baik" 
elif nilai >= 55: 
   huruf = "C" 
   ket   = "Cukup" 
elif nilai >= 40: 
   huruf = "D" 
   ket   = "Kurang" 
else: 
   huruf = "E" 
   ket = "Sangat Kurang" 

print("+==================================+")
print(f"| Nilai Angka    : {nilai:<16.1f}|")
print(f"| Nilai Huruf    : {huruf:<16}|")
print(f"| Keterangan     : {ket:<16}|")
print("+==================================+")
print()
print("+==================================+")
print("| Dosen: Bpk. Yusri Ikhwani, M.Kom |")
print("|   2510010102 - M. Rizky Rinaldy  |")
print("+==================================+")

input()
              </code></pre>
            </details>
        </li>
      </ul>
    </td>
    <td width="40%">
      <img src="/ALGO2 - Bpk. Yusri Ikhwani, M.Kom/img/ProgramKonversiNilaiHuruf.png" alt="Pratinjau_ProgramKonversiNilaiHuruf">
  <a href="https://github.com/rnld-devcode/Praktikum_2510010102_M.RizkyRinaldy/blob/main/ALGO2%20-%20Bpk.%20Yusri%20Ikhwani%2C%20M.Kom/latihan1_2_nilaihuruf.py">
        <p align="center"><b>Program Konversi Nilai Ke Huruf.</b></p>
  </a>
    </td>
  </tr>
  <tr>
    <td width="60%">
      <h3>1.3 Kalkulator BMI (<code>latihan1_3_bmi.py</code>)</h3>
      <ul>
        <li><b>Percabangan (Selection)</b></li>
        <li><b>Soal: </b> Buatlah  program  yang  menghitung  BMI dengan  rumus  BMI  =  berat  /  (tinggi**2).  Kategori:  Kurus (<\18.5), Normal (18.5-24.9), Gemuk (25-29.9), Obesitas (>=30).</li>
        <li><details>
              <summary><b>🔍 Klik untuk melihat Source Code</b></summary>
                <pre style="background: #f4f4f4; padding: 10px; border-radius: 5px; overflow-x: auto;"><code>
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

input()
              </code></pre>
            </details>
        </li>
      </ul>
    </td>
    <td width="40%">
      <img src="/ALGO2 - Bpk. Yusri Ikhwani, M.Kom/img/KalkulatorBMI.png" alt="Pratinjau_KalkulatorBMI">
  <a href="https://github.com/rnld-devcode/Praktikum_2510010102_M.RizkyRinaldy/blob/main/ALGO2%20-%20Bpk.%20Yusri%20Ikhwani%2C%20M.Kom/latihan1_3_bmi.py">
        <p align="center"><b>Kalkulator BMI (Body Mass Index).</b></p>
  </a>
    </td>
  </tr>
  <tr>
    <td width="60%">
      <h3>1.4 Program Tiket Bioskop dengan Diskon (<code>latihan1_4_tiket.py</code>)</h3>
      <ul>
        <li><b>Percabangan (Selection)</b></li>
        <li><b>Soal: </b>  Buatlah program harga tiket bioskop. Harga normal Rp. 50.000. Diskon 50% untuk umur <\12 atau >60 tahun. Diskon 20% untuk pelajar (input Y/T).</li>
        <li><details>
              <summary><b>🔍 Klik untuk melihat Source Code</b></summary> 
                <pre style="background: #f4f4f4; padding: 10px; border-radius: 5px; overflow-x: auto;"><code>
print("+====================================+")
print("|        Loket Tiket Bioskop         |")
print("+====================================+")
harga_normal = 50000 
umur         = int(input("  Masukkan umur (Tahun): "))
pelajar      =     input("  Apakah pelajar (Y/T) : ").upper() 

if umur < 12 or umur > 60: 
     diskon = 0.5 
     ket = "Diskon Anak/Lansia (50%)" 
elif pelajar == "Y": 
    diskon = 0.2 
    ket = "Diskon Pelajar (20%)" 
else: 
    diskon = 0 
    ket = "Harga Normal" 
   
potongan = harga_normal * diskon 
bayar    = harga_normal - potongan 

print("+====================================+")
print(f"| Harga Normal : Rp, {harga_normal:<16}|") 
print(f"| Keterangan   : {ket:<20}|") 
print(f"| Potongan     : Rp, {int(potongan):<16}|") 
print(f"| Total Bayar  : Rp, {int(bayar):<16}|") 
print("+====================================+")
print()
print("+====================================+")
print("|  Dosen: Bpk. Yusri Ikhwani, M.Kom  |")
print("|    2510010102 - M. Rizky Rinaldy   |")
print("+====================================+")

input()
              </code></pre>
            </details>
        </li>
      </ul>
    </td>
    <td width="40%">
      <img src="/ALGO2 - Bpk. Yusri Ikhwani, M.Kom/img/ProgramLoketTiket.png" alt="Pratinjau_LoketTiket">
  <a href="https://github.com/rnld-devcode/Praktikum_2510010102_M.RizkyRinaldy/blob/main/ALGO2%20-%20Bpk.%20Yusri%20Ikhwani%2C%20M.Kom/latihan1_4_tiket.py">
        <p align="center"><b>Program Tiket Bioskop dengan Diskon.</b></p>
  </a>
    </td>
  </tr>
  <tr>
  <td width="60%">
      <h3>1.5 Program Penentu Jenis Segitiga (<code>latihan1_5_segitiga.py</code>)</h3>
      <ul>
        <li><b>Percabangan (Selection)</b></li>
        <li><b>Soal: </b> Buatlah program yang menerima input tiga sisi segitiga kemudian menentukan jenisnya: sama sisi, sama kaki, atau sembarang. Program juga memvalidasi apakah ketiga sisi membentuk segitiga yang valid.</li>
        <li><details>
              <summary><b>🔍 Klik untuk melihat Source Code</b></summary>
                <pre style="background: #f4f4f4; padding: 10px; border-radius: 5px; overflow-x: auto;"><code>
print("+====================================+")
print("|      Penentu Jenis Segitiga        |")
print("+====================================+")
a = float(input("     Masukkan panjang sisi a : ")) 
b = float(input("     Masukkan panjang sisi b : ")) 
c = float(input("     Masukkan panjang sisi c : ")) 

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
              </code></pre>
            </details>
        </li>
      </ul>
    </td>
    <td width="40%">
      <img src="/ALGO2 - Bpk. Yusri Ikhwani, M.Kom/img/PenentuJenisSegitiga.png" alt="Pratinjau_PenentuJenisSegitiga">
  <a href="https://github.com/rnld-devcode/Praktikum_2510010102_M.RizkyRinaldy/blob/main/ALGO2%20-%20Bpk.%20Yusri%20Ikhwani%2C%20M.Kom/latihan1_5_segitiga.py">
        <p align="center"><b>Program Penentu Jenis Segitiga.</b></p>
  </a>
    </td>
  </tr>
</table>

---

## BAB 2 PERULANGAN (LOOPING)
**Perulangan  (Looping)**  merupakan  struktur  kontrol  yang  digunakan  untuk  menjalankan  satu  atau sekumpulan perintah secara berulang-ulang hingga suatu kondisi terpenuhi. Python menyediakan dua bentuk utama perulangan: for dan while. 
**Perulangan for:**
```bash
for variabel in iterable: 
    # blok kode yang akan diulang 
```
**Perulangan while:**
```bash
while kondisi: 
    # blok kode yang akan diulang selama kondisi bernilai True 
 ```
Fungsi range(start, stop, step) sering digunakan bersama for untuk menghasilkan urutan bilangan. Sementara itu, kata kunci break digunakan untuk menghentikan perulangan sebelum waktunya, dan continue untuk melewati iterasi saat ini dan lanjut ke iterasi berikutnya.
<table>
  <tr>
    <td width="60%">
      <h3>2.1  Tabel Perkalian (<code>latihan2_1_perkalian.py</code>)</h3>
      <ul>
        <li><b>Perulangan (Looping)</b></li>
        <li><b>Soal: </b> Buatlah program yang menampilkan tabel perkalian dari suatu angka yang diinput user, mulai dari 1 sampai 10.</li>
        <li><details>
              <summary><b>🔍 Klik untuk melihat Source Code</b></summary> 
                <pre style="background: #f4f4f4; padding: 10px; border-radius: 5px; overflow-x: auto;"><code>
print("+====================================+")
print("|          Kamus Perkalian           |")
print("+====================================+")
n = int(input("          Masukkan angka: ")) 
print("+====================================+")
print(f"|           Tabel Perkalian          |") 
print("+====================================+")
for i in range(1, 11): 
    hasil = n * i 
    print(f"|{n:>-14} x {i:2d} = {hasil:<14}|") 
print("+====================================+")
print()
print("+====================================+")
print("|  Dosen: Bpk. Yusri Ikhwani, M.Kom  |")
print("|    2510010102 - M. Rizky Rinaldy   |")
print("+====================================+")

input()
              </code></pre>
            </details>
        </li>
      </ul>
    </td>
    <td width="40%">
      <img src="/ALGO2 - Bpk. Yusri Ikhwani, M.Kom/img/KamusPerkalian.png" alt="Pratinjau_ProgramKamusPerkalian">
      
  <a href="https://github.com/rnld-devcode/Praktikum_2510010102_M.RizkyRinaldy/blob/main/ALGO2%20-%20Bpk.%20Yusri%20Ikhwani%2C%20M.Kom/latihan2_1_perkalian.py">
        <p align="center"><b>Program Tabel Perkalian.</b></p>
  </a>
    </td>
  </tr>
  <tr>
    <td width="60%">
      <h3>2.2 Program Menghitung Faktorial (<code>latihan2_2_faktorial.py</code>)</h3>
      <ul>
        <li><b>Perulangan (Looping)</b></li>
        <li><b>Soal: </b> Buatlah program yang menghitung faktorial dari bilangan bulat positif yang diinput. Faktorial n! = 1 × 2 × 3 × ... × n. </li>
        <li><details>
              <summary><b>🔍 Klik untuk melihat Source Code</b></summary> 
                <pre style="background: #f4f4f4; padding: 10px; border-radius: 5px; overflow-x: auto;"><code>
print("+===============================================+")
print("|              Kalkulator Faktorial             |")
print("+===============================================+")
n = int(input("         Masukkan bilangan bulat positif: ")) 
print("+===============================================+")
print(f"|            Hasil Faktorial dari {n:<8}      |")
print("+-----------------------------------------------+")
if n < 0: 
    print("|  Faktorial hanya untuk bilangan non-negatif!  |") 
else: 
    hasil = 1 
    proses = "" 
    for i in range(1, n + 1): 
       hasil *= i 
       proses += f"{i}" 
       if i < n: 
            proses += " x " 
    if n == 0: 
         print(f"0! = 1") 
    else: 
        print(f"|{n}! = {proses} = {hasil:<5}|")
print("+===============================================+")
print()
print("+===============================================+")
print("|        Dosen: Bpk. Yusri Ikhwani, M.Kom       |")
print("|          2510010102 - M. Rizky Rinaldy        |")
print("+===============================================+")

input()
              </code></pre>
            <li><details>
        </li>
      </ul>
    </td>
    <td width="40%">
      <img src="/ALGO2 - Bpk. Yusri Ikhwani, M.Kom/img/KalkulatorFaktorial.png" alt="Pratinjau_ProgramMenghitungFaktorial">
  <a href="https://github.com/rnld-devcode/Praktikum_2510010102_M.RizkyRinaldy/blob/main/ALGO2%20-%20Bpk.%20Yusri%20Ikhwani%2C%20M.Kom/latihan2_2_faktorial.py">
        <p align="center"><b>Program Menghitung Faktorial.</b></p>
  </a>
    </td>
  </tr>
  <tr>
    <td width="60%">
      <h3>2.3 Deret Fibonacci (<code>latihan2_3_fibonacci.py</code>)</h3>
      <ul>
        <li><b>Perulangan (Looping)</b></li>
        <li><b>Soal: </b> Buatlah program yang menampilkan deret Fibonacci sebanyak N suku. Deret Fibonacci: 0, 1, 1, 2, 3, 5, 8, 13, ... </li>
        <li><details>
              <summary><b>🔍 Klik untuk melihat Source Code</b></summary>
                <pre style="background: #f4f4f4; padding: 10px; border-radius: 5px; overflow-x: auto;"><code>
print("+===============================================+")
print("|                Deret Fibonacci                |")
print("+===============================================+")
n = int(input("             Masukkan jumlah suku: ")) 
print("+===============================================+")
print(f"|     Deret Fibonacci dari suku 1 hingga {n:<7}|")
print("+-----------------------------------------------+") 
a, b = 0, 1 
print("|", end=" ")
for i in range(n): 
   print(a, end=" ") 
   a, b = b, a + b 
print("|")
print("+===============================================+")
print()
print("+===============================================+")
print("|        Dosen: Bpk. Yusri Ikhwani, M.Kom       |")
print("|          2510010102 - M. Rizky Rinaldy        |")
print("+===============================================+")

input()
              </code></pre>
            </details>
        </li>
      </ul>
    </td>
    <td width="40%">
      <img src="/ALGO2 - Bpk. Yusri Ikhwani, M.Kom/img/DeretFibonacci.png" alt="Pratinjau_DeretFibonacci">
  <a href="https://github.com/rnld-devcode/Praktikum_2510010102_M.RizkyRinaldy/blob/main/ALGO2%20-%20Bpk.%20Yusri%20Ikhwani%2C%20M.Kom/latihan2_3_fibonacci.py">
        <p align="center"><b>Deret Fibonacci.</b></p>
  </a>
    </td>
  </tr>
  <tr>
    <td width="60%">
      <h3>2.4 Menebak Angka (While-break) (<code>latihan2_4_tebak_angka.py</code>)</h3>
      <ul>
        <li><b>Perulangan (Looping)</b></li>
        <li><b>Soal: </b>  Buatlah  game  sederhana:  komputer  memikirkan  angka  1-20,  user  menebak.  Program  memberi petunjuk 'Terlalu besar' atau 'Terlalu kecil' sampai tebakan benar.</li>
        <li><details>
              <summary><b>🔍 Klik untuk melihat Source Code</b></summary>
                <pre style="background: #f4f4f4; padding: 10px; border-radius: 5px; overflow-x: auto;"><code>
import random 
print("+===============================================+")
print("|               Game Tebak Angka                |")
print("+===============================================+") 
print("|       Saya memikirkan angka 1 sampai 20       |") 

angka_rahasia = random.randint(1, 20) 
percobaan = 0 
  
while True: 
   print("+-----------------------------------------------+")
   print(f"|                 Percobaan Ke-{percobaan}                |")
   print("|                                               |")
   tebakan = int(input("| Tebakan Anda: ")) 
   print("|                                               |")
   percobaan += 1 
    
   if tebakan == angka_rahasia: 
        print(f"|     Benar! Anda menebak dalam {percobaan} percobaan.    |") 
        break 
   elif tebakan < angka_rahasia: 
        print(f"|           Terlalu kecil, coba lagi!           |") 
   else: 
        print(f"|           Terlalu besar, coba lagi!           |") 
        
print("+===============================================+")
print()
print("+===============================================+")
print("|        Dosen: Bpk. Yusri Ikhwani, M.Kom       |")
print("|          2510010102 - M. Rizky Rinaldy        |")
print("+===============================================+")

input()
              </code></pre>
            </details>
        </li>
      </ul>
    </td>
    <td width="40%">
      <img src="/ALGO2 - Bpk. Yusri Ikhwani, M.Kom/img/GameTebakAngka.png" alt="Pratinjau_GameTebakAngka">
  <a href="https://github.com/rnld-devcode/Praktikum_2510010102_M.RizkyRinaldy/blob/main/ALGO2%20-%20Bpk.%20Yusri%20Ikhwani%2C%20M.Kom/latihan2_4_tebak_angka.py">
        <p align="center"><b>Game Tebak Angka Random</b></p>
  </a>
    </td>
  </tr>
  <tr>
  <td width="60%">
      <h3>2.5 Program Pola Piramida Angka (<code>latihan2_5_piramida.py</code>)</h3>
      <ul>
        <li><b>Perulangan (Looping)</b></li>
        <li><b>Soal: </b> Buatlah  program  yang  menampilkan  pola  piramida  angka  menggunakan  perulangan  bersarang (nested loop).</li>
        <li><details>
              <summary><b>🔍 Klik untuk melihat Source Code</b></summary>
                <pre style="background: #f4f4f4; padding: 10px; border-radius: 5px; overflow-x: auto;"><code>
print("+============================================+")
print("|             Pola Piramida Angka            |")
print("+============================================+")
tinggi = int(input("          Masukkan tinggi piramida: ")) 
print("+============================================+")
print(f"|    Piramida Angka dengan Tinggi {tinggi} baris   |")
print("+--------------------------------------------+") 
for i in range(1, tinggi + 1): 

    print(" " * (tinggi - i) * 2, end="")   

    for j in range(1, i + 1): 
        print(f"{j:<2}", end="") 
        
    for j in range(i - 1, 0, -1): 
        print(f"{j:<2}", end="") 
    
    print()
print("+============================================+")
print()
print("+============================================+")
print("|      Dosen: Bpk. Yusri Ikhwani, M.Kom      |")
print("|        2510010102 - M. Rizky Rinaldy       |")
print("+============================================+")

input()
              </code></pre>
            </details>
        </li>
      </ul>
    </td>
    <td width="40%">
      <img src="/ALGO2 - Bpk. Yusri Ikhwani, M.Kom/img/PiramidaAngka.png" alt="Pratinjau_PolaPiramidaAngka">
  <a href="https://github.com/rnld-devcode/Praktikum_2510010102_M.RizkyRinaldy/blob/main/ALGO2%20-%20Bpk.%20Yusri%20Ikhwani%2C%20M.Kom/latihan2_5_piramida.py">
        <p align="center"><b>Program Pola Piramida Angka.</b></p>
  </a>
    </td>
  </tr>
</table>

---

## BAB 3 STRUKTUR DATA DASAR
Python menyediakan beberapa **Struktur Data** built-in yang sangat powerful untuk mengelompokkan data. Masing-masing memiliki karakteristik dan penggunaan yang berbeda. 

**List:**
Struktur  data  terurut  (ordered)  dan  dapat  diubah  (mutable).  List ditulis  dengan  kurung  siku  []. Contoh: 
```bash
buah = ['apel', 'jeruk', 'mangga']
``` 

**Tuple:** 
Mirip  list  tetapi  tidak  dapat  diubah  (immutable).  Tuple  ditulis dengan  kurung  bulat  ().  Contoh: 
```bash
koordinat = (10, 20)
```

**Dictionary:**
Struktur data berupa pasangan key-value. Dictionary ditulis dengan kurung kurawal {}. Contoh: 
```bash
mhs = {'nama': 'Budi', 'nim': '2024001'}
```

**Set:**
Kumpulan elemen unik yang tidak terurut. Set ditulis dengan kurung kurawal {} tanpa pasangan key-value. Contoh: 
```bash
angka = {1, 2, 3, 4}
```
<table>
  <tr>
    <td width="60%">
      <h3>3.1  Manajemen Daftar Belanja (List)  (<code>latihan3_1_list_belanja.py</code>)</h3>
      <ul>
        <li><b>Struktur Data Dasar</b></li>
        <li><b>Soal: </b> Buatlah program untuk mengelola daftar belanja. User dapat menambah, melihat, dan menghapus item dari daftar. </li>
        <li><details>
              <summary><b>🔍 Klik untuk melihat Source Code</b></summary> 
                <pre style="background: #f4f4f4; padding: 10px; border-radius: 5px; overflow-x: auto;"><code>
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
              </code></pre>
            </details>
        </li>
      </ul>
    </td>
    <td width="40%">
      <img src="/ALGO2 - Bpk. Yusri Ikhwani, M.Kom/img/ListBelanja.png" alt="Pratinjau_ProgramDaftarBelanjaan">
      
  <a href="https://github.com/rnld-devcode/Praktikum_2510010102_M.RizkyRinaldy/blob/main/ALGO2%20-%20Bpk.%20Yusri%20Ikhwani%2C%20M.Kom/latihan3_1_list_belanja.py">
        <p align="center"><b>Program Daftar Belanjaan.</b></p>
  </a>
    </td>
  </tr>
  <tr>
    <td width="60%">
      <h3>3.2 Statistika Nilai Mahasiswa (List) (<code>latihan3_2_statistik.py</code>)</h3>
      <ul>
        <li><b>Struktur Data Dasar</b></li>
        <li><b>Soal: </b> Buatlah program yang menerima N nilai mahasiswa, lalu menampilkan nilai tertinggi, terendah, rata-rata, dan jumlah total.</li>
        <li><details>
              <summary><b>🔍 Klik untuk melihat Source Code</b></summary> 
                <pre style="background: #f4f4f4; padding: 10px; border-radius: 5px; overflow-x: auto;"><code>
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
              </code></pre>
            </details>
        </li>
      </ul>
    </td>
    <td width="40%">
      <img src="/ALGO2 - Bpk. Yusri Ikhwani, M.Kom/img/StatistikNilaiMahasiswa.png" alt="Pratinjau_ProgramStatistik">
  <a href="https://github.com/rnld-devcode/Praktikum_2510010102_M.RizkyRinaldy/blob/main/ALGO2%20-%20Bpk.%20Yusri%20Ikhwani%2C%20M.Kom/latihan3_2_statistik.py">
        <p align="center"><b>Program Statistika Nilai Mahasiswa.</b></p>
  </a>
    </td>
  </tr>
  <tr>
    <td width="60%">
      <h3>3.3 Data Mahasiswa (Dictionary) (<code>latihan3_3_dictionary.py</code>)</h3>
      <ul>
        <li><b>Struktur Data Dasar</b></li>
        <li><b>Soal: </b> Buatlah program yang menyimpan data mahasiswa menggunakan dictionary, kemudian menampilkannya dalam format rapi.</li>
        <li><details>
              <summary><b>🔍 Klik untuk melihat Source Code</b></summary>
                <pre style="background: #f4f4f4; padding: 10px; border-radius: 5px; overflow-x: auto;"><code>
print("+==================================+")
print("|       Input Data Mahasiswa       |")
print("+==================================+")
mahasiswa = { 
 "nim"    : input("| NIM       : "), 
 "nama"   : input("| Nama      : "), 
 "jurusan": input("| Jurusan   : "), 
 "ipk"    : float(input("| IPK       : ")) 
} 
print("+==================================+")
print()
print("+----------------------------------+")
print("|          DATA MAHASISWA          |") 
print("+----------------------------------+")

for key, value in mahasiswa.items(): 
    print(f"| {key.capitalize():10s}: {value:<20} |") 

if mahasiswa["ipk"] >= 3.5: 
     predikat = "Cumlaude" 
elif mahasiswa["ipk"] >= 3.0: 
    predikat = "Sangat Memuaskan" 
elif mahasiswa["ipk"] >= 2.5: 
    predikat = "Memuaskan" 
else: 
    predikat = "Cukup" 


print(f"| {'Predikat':10s}: {predikat:<20} |") 
print("+==================================+")
print()
print("+==================================+")
print("| Dosen: Bpk. Yusri Ikhwani, M.Kom |")
print("|   2510010102 - M. Rizky Rinaldy  |")
print("+==================================+")

input()
              </code></pre>
            </details>
        </li>
      </ul>
    </td>
    <td width="40%">
      <img src="/ALGO2 - Bpk. Yusri Ikhwani, M.Kom/img/DataMahasiswa.png" alt="Pratinjau_ProgramDataMahasiswa">
  <a href="https://github.com/rnld-devcode/Praktikum_2510010102_M.RizkyRinaldy/blob/main/ALGO2%20-%20Bpk.%20Yusri%20Ikhwani%2C%20M.Kom/latihan3_3_dictionary.py">
        <p align="center"><b>Program Data Mahasiswa</b></p>
  </a>
    </td>
  </tr>
  <tr>
    <td width="60%">
      <h3>3.4 Menghitung Frekuensi Huruf (Dictionary) (<code>latihan3_4_frekuensi.py</code>)</h3>
      <ul>
        <li><b>Struktur Data Dasar</b></li>
        <li><b>Soal: </b> Buatlah program yang menghitung berapa kali setiap huruf muncul dalam sebuah kalimat menggunakan dictionary.</li>
        <li><details>
              <summary><b>🔍 Klik untuk melihat Source Code</b></summary> 
                <pre style="background: #f4f4f4; padding: 10px; border-radius: 5px; overflow-x: auto;"><code>
print("+==================================+")
print("|         Frekuensi Huruf          |")
print("+==================================+")
kalimat = input("|Masukkan kalimat: ").lower() 
print("+----------------------------------+")
print()
frekuensi = {} 
for huruf in kalimat: 
    if huruf.isalpha(): 
        if huruf in frekuensi: 
            frekuensi[huruf] += 1 
        else: 
            frekuensi[huruf] = 1 
  
print("+==================================+")
print("|        Hasil Pengelompokan       |")
print("+==================================+")

for huruf in sorted(frekuensi.keys()): 
    print(f"|         '{huruf}' muncul {frekuensi[huruf]} kali        |")
print("+----------------------------------+")
print()
print("+==================================+")
print("| Dosen: Bpk. Yusri Ikhwani, M.Kom |")
print("|   2510010102 - M. Rizky Rinaldy  |")
print("+==================================+")

input()
              </code></pre>
            </details>
        </li>
      </ul>
    </td>
    <td width="40%">
      <img src="/ALGO2 - Bpk. Yusri Ikhwani, M.Kom/img/FrekuensiHuruf.png" alt="Pratinjau_FrekuensiHuruf">
  <a href="https://github.com/rnld-devcode/Praktikum_2510010102_M.RizkyRinaldy/blob/main/ALGO2%20-%20Bpk.%20Yusri%20Ikhwani%2C%20M.Kom/latihan3_4_frekuensi.py">
        <p align="center"><b>Menghitung Frekuensi Huruf</b></p>
  </a>
    </td>
  </tr>
  <tr>
  <td width="60%">
      <h3>3.5 Operasi Himpunan (Set) (<code>latihan3_5_set.py</code>)</h3>
      <ul>
        <li><b>Struktur Data Dasar</b></li>
        <li><b>Soal: </b> Buatlah  program  yang  menerima  dua  himpunan  bilangan,  kemudian  menampilkan  hasil  operasi gabungan (union), irisan (intersection), dan selisih (difference). </li>
        <li><details>
              <summary><b>🔍 Klik untuk melihat Source Code</b></summary>
                <pre style="background: #f4f4f4; padding: 10px; border-radius: 5px; overflow-x: auto;"><code>
print("+==================================+")
print("|      Input Anggota Himpunan      |")
print("|      (pisahkan dengan koma)      |")
print("+==================================+")
data_a = input("| Himpunan A : ") 
data_b = input("| Himpunan B : ") 
  
A = set(int(x.strip()) for x in data_a.split(",")) 
B = set(int(x.strip()) for x in data_b.split(",")) 

print("+==================================+")
print("|          Hasil Himpunan          |")
print("+==================================+")
print(f"| A           = {A}") 
print(f"| B           = {B}") 
print(f"| A U B       = {A | B}") 
print(f"| A ∩ B       = {A & B}") 
print(f"| A - B       = {A - B}") 
print(f"| B - A       = {B - A}") 
print(f"| Simetris    = {A ^ B}") 
print("+----------------------------------+")
print()
print("+==================================+")
print("| Dosen: Bpk. Yusri Ikhwani, M.Kom |")
print("|   2510010102 - M. Rizky Rinaldy  |")
print("+==================================+")

input()
              </code></pre>
            </details>
        </li>
      </ul>
    </td>
    <td width="40%">
      <img src="/ALGO2 - Bpk. Yusri Ikhwani, M.Kom/img/OperasiHimpunan.png" alt="Pratinjau_OperasiHimpunan">
  <a href="https://github.com/rnld-devcode/Praktikum_2510010102_M.RizkyRinaldy/blob/main/ALGO2%20-%20Bpk.%20Yusri%20Ikhwani%2C%20M.Kom/latihan3_5_set.py">
        <p align="center"><b>Operasi Himpunan.</b></p>
  </a>
    </td>
  </tr>
</table>

---

## BAB 4 FUNGSI (FUNCTION)
**Fungsi  (function)** adalah  blok  kode  yang dapat dipanggil berkali-kali untuk melakukan tugas tertentu. Fungsi membantu membuat kode lebih terstruktur, mudah dibaca, dan dapat digunakan ulang (reusable). Di Python, fungsi didefinisikan dengan kata kunci def.

**Bentuk umum fungsi:**
```bash
def nama_fungsi(parameter1, parameter2, ...): 
    # blok kode fungsi 
    return nilai_kembali  # opsional 
``` 
Fungsi dapat memiliki parameter (nilai masukan) dan return value (nilai keluaran). Jika fungsi tidak memiliki return, secara otomatis akan mengembalikan None. Parameter dapat diberi nilai default sehingga tidak wajib diisi saat pemanggilan.

<table>
  <tr>
    <td width="60%">
      <h3>4.1  Fungsi Konversi Suhu (<code>latihan4_1_suhu.py</code>)</h3>
      <ul>
        <li><b>Fungsi (Function)</b></li>
        <li><b>Soal: </b> Buatlah fungsi untuk mengkonversi suhu antara Celcius, Fahrenheit, dan Reamur menggunakan tiga fungsi terpisah.</li>
        <li><details>
              <summary><b>🔍 Klik untuk melihat Source Code</b></summary>
                <pre style="background: #f4f4f4; padding: 10px; border-radius: 5px; overflow-x: auto;"><code>
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
               </code></pre>
            </details>
        </li>
      </ul>
    </td>
    <td width="40%">
      <img src="/ALGO2 - Bpk. Yusri Ikhwani, M.Kom/img/KonversiSuhu.png" alt="Pratinjau_ProgramKonversiSuhu">
      
  <a href="https://github.com/rnld-devcode/Praktikum_2510010102_M.RizkyRinaldy/blob/main/ALGO2%20-%20Bpk.%20Yusri%20Ikhwani%2C%20M.Kom/latihan4_1_suhu.py">
        <p align="center"><b>Program Konversi Suhu.</b></p>
  </a>
    </td>
  </tr>
  <tr>
    <td width="60%">
      <h3>4.2 Fungsi Cek Bilangan Prima (<code>latihan4_2_prima.py</code>)</h3>
      <ul>
        <li><b>Fungsi (Function)</b></li>
        <li><b>Soal: </b> Buatlah fungsi yang mengembalikan True jika sebuah bilangan adalah prima, dan False jika bukan. Gunakan fungsi tersebut untuk mencetak bilangan prima dari 1 sampai N. </li>
        <li><details>
              <summary><b>🔍 Klik untuk melihat Source Code</b></summary> 
                <pre style="background: #f4f4f4; padding: 10px; border-radius: 5px; overflow-x: auto;"><code>
def is_prima(n): 
    if n < 2: 
        return False 
    for i in range(2, int(n ** 0.5) + 1): 
          if n % i == 0: 
                return False 
    return True 

print("+=====================================+")
print("|        Daftar Bilangan Prima        |")
print("+=====================================+")
batas = int(input("     Masukkan batas atas: ")) 

print("+=====================================+")
print(f"|Bilangan prima dari 1 sampai {batas:7}:|")
print("+=====================================+")

hasil = [] 
for i in range(1, batas + 1): 
     if is_prima(i): 
         hasil.append(i) 

print(f"| {hasil} |") 
print("+-------------------------------------+")
print(f"|       Total: {len(hasil):2} bilangan prima      |") 
print("+-------------------------------------+")
print()
print("+=====================================+")
print("|  Dosen: Bpk. Yusri Ikhwani, M.Kom   |")
print("|    2510010102 - M. Rizky Rinaldy    |")
print("+=====================================+")

input()
              </code></pre>
          </details>
        </li>
      </ul>
    </td>
    <td width="40%">
      <img src="/ALGO2 - Bpk. Yusri Ikhwani, M.Kom/img/BilanganPrima.png" alt="Pratinjau_ProgramBilanganPrima">
  <a href="https://github.com/rnld-devcode/Praktikum_2510010102_M.RizkyRinaldy/blob/main/ALGO2%20-%20Bpk.%20Yusri%20Ikhwani%2C%20M.Kom/latihan4_2_prima.py">
        <p align="center"><b>Program Pencari Bilangan Prima.</b></p>
  </a>
    </td>
  </tr>
  <tr>
    <td width="60%">
      <h3>4.3 Fungsi dengan Default Parameter (<code>latihan4_3_diskon.py</code>)</h3>
      <ul>
        <li><b>Fungsi (Function)</b></li>
        <li><b>Soal: </b> Buatlah  fungsi  penghitung  harga  setelah  diskon  dengan  parameter  default.  Diskon  default  10%, pajak default 11%.</li>
        <li><details>
              <summary><b>🔍 Klik untuk melihat Source Code</b></summary> 
                <pre style="background: #f4f4f4; padding: 10px; border-radius: 5px; overflow-x: auto;"><code>
def hitung_harga(harga_awal, diskon=10, pajak=11): 
    potongan = harga_awal * diskon / 100 
    setelah_diskon = harga_awal - potongan 
    nilai_pajak = setelah_diskon * pajak / 100 
    total = setelah_diskon + nilai_pajak 
    return total, potongan, nilai_pajak 

print("+==================================+")
print("|         Kalkulator Harga         |")
print("+==================================+")

harga = float(input("   Harga barang   : ")) 
d     = float(input("   Diskon (%)     : ")) 
  
total, pot, pjk = hitung_harga(harga, d) 

print("+==================================+")
print("|        Hasil Perhitungan         |")
print("+==================================+")
print(f"| Harga Awal      : Rp {harga:11,.0f} |") 
print(f"| Potongan        : Rp {pot:11,.0f} |") 
print(f"| Pajak (11%)     : Rp {pjk:11,.0f} |") 
print(f"| Total Bayar     : Rp {total:11,.0f} |") 
print("+----------------------------------+")
print()
print("+==================================+")
print("| Dosen: Bpk. Yusri Ikhwani, M.Kom |")
print("|   2510010102 - M. Rizky Rinaldy  |")
print("+==================================+")

input()
              </code></pre>
            </details>
        </li>
      </ul>
    </td>
    <td width="40%">
      <img src="/ALGO2 - Bpk. Yusri Ikhwani, M.Kom/img/KalkulatorHarga.png" alt="Pratinjau_ProgramKalkulatorHarga">
  <a href="https://github.com/rnld-devcode/Praktikum_2510010102_M.RizkyRinaldy/blob/main/ALGO2%20-%20Bpk.%20Yusri%20Ikhwani%2C%20M.Kom/latihan4_3_diskon.py">
        <p align="center"><b>Program Kalkulator Harga</b></p>
  </a>
    </td>
  </tr>
  <tr>
    <td width="60%">
      <h3>4.4 Fungsi Rekursif Faktorial (<code>latihan4_4_rekursif.py</code>)</h3>
      <ul>
        <li><b>Fungsi (Function)</b></li>
        <li><b>Soal: </b> Buatlah  fungsi  rekursif  untuk  menghitung  faktorial.  Fungsi  rekursif  adalah  fungsi  yang memanggil dirinya sendiri.</li>
        <li><details>
              <summary><b>🔍 Klik untuk melihat Source Code</b></summary>
                <pre style="background: #f4f4f4; padding: 10px; border-radius: 5px; overflow-x: auto;"><code>
def faktorial(n): 
    if n <= 1: 
        return 1 
    return n * faktorial(n - 1) 
  
def pangkat(basis, eksponen): 
    if eksponen == 0: 
        return 1 
    return basis * pangkat(basis, eksponen - 1) 

print("+==================================+")
print("|          Fungsi Rekursif         |")
print("+==================================+")
n = int(input("     Hitung faktorial dari: ")) 
b = int(input("     Basis pangkat        : ")) 
e = int(input("     Eksponen pangkat     : ")) 
  
print("+==================================+")
print("|        Hasil Perhitungan         |")
print("+==================================+")
print(f"|      {n:>6}!  = {faktorial(n):<10}       |") 
print(f"|       {b:3}^{e:<3} = {pangkat(b, e):<10}       |") 
print("+----------------------------------+")
print()
print("+==================================+")
print("| Dosen: Bpk. Yusri Ikhwani, M.Kom |")
print("|   2510010102 - M. Rizky Rinaldy  |")
print("+==================================+")

input()
              </code></pre>
            </details>
        </li>
      </ul>
    </td>
    <td width="40%">
      <img src="/ALGO2 - Bpk. Yusri Ikhwani, M.Kom/img/FungsiRekursif.png" alt="Pratinjau_FungsiRekursif">
  <a href="https://github.com/rnld-devcode/Praktikum_2510010102_M.RizkyRinaldy/blob/main/ALGO2%20-%20Bpk.%20Yusri%20Ikhwani%2C%20M.Kom/latihan4_4_rekursif.py">
        <p align="center"><b>Menghitung Fungsi Rekursif</b></p>
  </a>
    </td>
  </tr>
  <tr>
  <td width="60%">
      <h3>4.5 Kalkulator Fungsional (<code>latihan4_5_kalkulator.py</code>)</h3>
      <ul>
        <li><b>Fungsi (Function)</b></li>
        <li><b>Soal: </b> Buatlah kalkulator yang memanfaatkan beberapa fungsi untuk operasi matematika. Setiap operasi ditangani oleh fungsi terpisah.</li>
        <li><details>
              <summary><b>🔍 Klik untuk melihat Source Code</b></summary>
                <pre style="background: #f4f4f4; padding: 10px; border-radius: 5px; overflow-x: auto;"><code>

def tambah(a, b):    return a + b
def kurang(a, b):    return a - b 
def kali(a, b):      return a * b 
def bagi(a, b): 
    if b == 0: 
        return None 
    return a / b 
  
def tampilkan_menu(): 
    print("+==================================+")
    print("|       Kalkulator Sederhana       |")
    print("+==================================+")
    print("| 1. Tambah                        |") 
    print("| 2. Kurang                        |") 
    print("| 3. Kali                          |") 
    print("| 4. Bagi                          |") 
    print("| 5. Keluar                        |") 
    print("+----------------------------------+")
  
while True: 
    tampilkan_menu() 
    pilih = input("             Pilihan : ") 
    if pilih == "5": 
        print("+----------------------------------+")
        print("|          Terima kasih!           |")
        print("+----------------------------------+")
        break 
    if pilih not in "1234": 
        print("+----------------------------------+")
        print("|      Pilihan tidak valid!        |") 
        print("+----------------------------------+")
        continue 
        
a = float(input("       Angka pertama : ")) 
b = float(input("       Angka kedua   : ")) 

if pilih == "1":   hasil = tambah(a, b); op = "+" 
elif pilih == "2": hasil = kurang(a, b); op = "-" 
elif pilih == "3": hasil = kali(a, b);   op = "x" 
else:              hasil = bagi(a, b);   op = "/" 

print("+==================================+")
print("|        Hasil Perhitungan         |")
print("+==================================+")
if hasil is None: 
      print("| Error: Pembagian dengan nol! |") 
else: 
      print(f"|Hasil:{a:6} {op} {b:<6} = {hasil:10}|") 
print("+----------------------------------+")
print()
print("+==================================+")
print("| Dosen: Bpk. Yusri Ikhwani, M.Kom |")
print("|   2510010102 - M. Rizky Rinaldy  |")
print("+==================================+")

input()
              </code></pre>
            </details>
        </li>
      </ul>
    </td>
    <td width="40%">
      <img src="/ALGO2 - Bpk. Yusri Ikhwani, M.Kom/img/KalkulatorSederhana.png" alt="Pratinjau_KalkulatorSederhana">
  <a href="https://github.com/rnld-devcode/Praktikum_2510010102_M.RizkyRinaldy/blob/main/ALGO2%20-%20Bpk.%20Yusri%20Ikhwani%2C%20M.Kom/latihan4_5_kalkulator.py">
        <p align="center"><b>Kalkulator Sederhana.</b></p>
  </a>
    </td>
  </tr>
</table>

---

## BAB 5 ALGORITMA DAN LOGIKA PEMROGRAMAN
**Algoritma** adalah urutan langkah-langkah logis untuk menyelesaikan suatu masalah. Algoritma yang baik  harus  memenuhi  beberapa  kriteria:  memiliki  input  dan  output  yang  jelas,  efektif  (dapat dilaksanakan), terbatas (finite), dan tidak ambigu. Pada  bab  ini  akan  dibahas  beberapa  algoritma  klasik  yang  sering  digunakan,  yaitu  algoritma pencarian (searching) dan pengurutan (sorting). Linear Search mencari elemen satu per satu hingga ditemukan, sedangkan Bubble Sort mengurutkan data dengan membandingkan pasangan elemen 
yang berdekatan. 

<table>
  <tr>
    <td width="60%">
      <h3>5.1 Linear Search (<code>latihan5_1_linear_search.py</code>)</h3>
      <ul>
        <li><b>Algoritma dan Logika Pemrograman</b></li>
        <li><b>Soal: </b> Implementasikan algoritma Linear Search untuk mencari posisi sebuah elemen dalam sebuah list. </li>
        <li><details>
              <summary><b>🔍 Klik untuk melihat Source Code</b></summary>
                <pre style="background: #f4f4f4; padding: 10px; border-radius: 5px; overflow-x: auto;"><code>
print("+==================================+")
print("|     Algoritma Linear Search      |")
print("+==================================+")
data =  [15, 27, 8, 42, 33, 19, 5, 66, 21] 
print(f"|             Data                |") 
print(f"|{data}|") 
print("+----------------------------------+")
target = int(input("            Cari angka: ")) 
posisi = linear_search(data, target) 

print("+----------------------------------+")
if posisi != -1: 
    print(f"|Angka {target:2} ditemukan pd indeks ke-{posisi:2}|") 
else: 
    print(f"| Angka {target} TIDAK ditemukan dalam data|")
print("+----------------------------------+")
print()
print("+==================================+")
print("| Dosen: Bpk. Yusri Ikhwani, M.Kom |")
print("|   2510010102 - M. Rizky Rinaldy  |")
print("+==================================+")

input()
               </code></pre>
            </details>
        </li>
      </ul>
    </td>
    <td width="40%">
      <img src="/ALGO2 - Bpk. Yusri Ikhwani, M.Kom/img/AlgoritmaLinearSearch.png" alt="Pratinjau_AlgoritmaLinearSearch">
      
  <a href="https://github.com/rnld-devcode/Praktikum_2510010102_M.RizkyRinaldy/blob/main/ALGO2%20-%20Bpk.%20Yusri%20Ikhwani%2C%20M.Kom/latihan5_1_linear_search.py">
        <p align="center"><b>Algoritma Linear Search</b></p>
  </a>
    </td>
  </tr>
  <tr>
    <td width="60%">
      <h3>5.2 Bubble Sort (<code>latihan5_2_bubble_sort.py</code>)</h3>
      <ul>
        <li><b>Algoritma dan Logika Pemrograman</b></li>
        <li><b>Soal: </b> Implementasikan  algoritma  Bubble  Sort  untuk  mengurutkan  data  secara  ascending  (dari  kecil  ke besar). Program juga menampilkan tahapan pengurutan.</li>
        <li><details>
              <summary><b>🔍 Klik untuk melihat Source Code</b></summary> 
                <pre style="background: #f4f4f4; padding: 10px; border-radius: 5px; overflow-x: auto;"><code>
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
              </code></pre>
          </details>
        </li>
      </ul>
    </td>
    <td width="40%">
      <img src="/ALGO2 - Bpk. Yusri Ikhwani, M.Kom/img/AlgoritmaLinearBubbleSort.png" alt="Pratinjau_AlgoritmaBubbleSort">
  <a href="https://github.com/rnld-devcode/Praktikum_2510010102_M.RizkyRinaldy/blob/main/ALGO2%20-%20Bpk.%20Yusri%20Ikhwani%2C%20M.Kom/latihan5_2_bubble_sort.py">
        <p align="center"><b>Algoritma Bubble Sort</b></p>
  </a>
    </td>
  </tr>
  <tr>
    <td width="60%">
      <h3>5.3 FPB dan KPK (Algoritma Euclidean) (<code>latihan5_3_fpb_kpk.py</code>)</h3>
      <ul>
        <li><b>Algoritma dan Logika Pemrograman</b></li>
        <li><b>Soal: </b> Buatlah program yang mencari FPB (Faktor Persekutuan Terbesar) menggunakan algoritma Euclidean, lalu gunakan untuk menghitung KPK.</li>
        <li><details>
              <summary><b>🔍 Klik untuk melihat Source Code</b></summary> 
                <pre style="background: #f4f4f4; padding: 10px; border-radius: 5px; overflow-x: auto;"><code>
def fpb(a, b): 
    while b != 0: 
        a, b = b, a % b 
    return a 
  
def kpk(a, b): 
    return (a * b) // fpb(a, b) 

print("+==================================+")
print("|      Kalkulator FPB dan KPK      |")
print("+==================================+")
x = int(input("     Bilangan pertama: ")) 
y = int(input("     Bilangan kedua  : ")) 
  
print("+----------------------------------+")
print(f"|     FPB({x:3}, {y:<3}) =  {fpb(x, y):<6}      |") 
print(f"|     KPK({x:3}, {y:<3}) =  {kpk(x, y):<6}      |")
print("+----------------------------------+")
print()
print("+==================================+")
print("| Dosen: Bpk. Yusri Ikhwani, M.Kom |")
print("|   2510010102 - M. Rizky Rinaldy  |")
print("+==================================+")

input() 
              </code></pre>
            </details>
        </li>
      </ul>
    </td>
    <td width="40%">
      <img src="/ALGO2 - Bpk. Yusri Ikhwani, M.Kom/img/KalkulatorFPBdanKPK.png" alt="Pratinjau_KalkulatorFPB&KPK">
  <a href="https://github.com/rnld-devcode/Praktikum_2510010102_M.RizkyRinaldy/blob/main/ALGO2%20-%20Bpk.%20Yusri%20Ikhwani%2C%20M.Kom/latihan5_3_fpb_kpk.py">
        <p align="center"><b>Kalkulator FPB & KPK</b></p>
  </a>
    </td>
  </tr>
  <tr>
    <td width="60%">
      <h3>5.4 Palindrom (<code>latihan5_4_palindrom.py</code>)</h3>
      <ul>
        <li><b>Algoritma dan Logika Pemrograman</b></li>
        <li><b>Soal: </b> Buatlah program yang memeriksa apakah suatu kata atau kalimat adalah palindrom (dibaca sama dari depan maupun belakang).</li>
        <li><details>
              <summary><b>🔍 Klik untuk melihat Source Code</b></summary>
                <pre style="background: #f4f4f4; padding: 10px; border-radius: 5px; overflow-x: auto;"><code>
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
              </code></pre>
            </details>
        </li>
      </ul>
    </td>
    <td width="40%">
      <img src="/ALGO2 - Bpk. Yusri Ikhwani, M.Kom/img/PengecekanPalindrom.png" alt="Pratinjau_PengecekanPalindrom">
  <a href="https://github.com/rnld-devcode/Praktikum_2510010102_M.RizkyRinaldy/blob/main/ALGO2%20-%20Bpk.%20Yusri%20Ikhwani%2C%20M.Kom/latihan5_4_palindrom.py">
        <p align="center"><b>Pengecekan Palindrom</b></p>
  </a>
    </td>
  </tr>
  <tr>
  <td width="60%">
      <h3>5.5 Konversi Bilangan Desimal ke Biner (<code>latihan5_5_biner.py</code>)</h3>
      <ul>
        <li><b>Algoritma dan Logika Pemrograman</b></li>
        <li><b>Soal: </b> Buatlah program yang mengkonversi bilangan desimal menjadi biner menggunakan metode pembagian berturut-turut.</li>
        <li><details>
              <summary><b>🔍 Klik untuk melihat Source Code</b></summary>
                <pre style="background: #f4f4f4; padding: 10px; border-radius: 5px; overflow-x: auto;"><code>
def desimal_to_biner(n): 
    if n == 0: 
        return "0" 
    biner = "" 
    proses = [] 
    while n > 0: 
        sisa = n % 2 
        proses.append(f"{n:8} / 2 = {n//2:<8} sisa {sisa:<1}  |") 
        biner = str(sisa) + biner 
        n = n // 2 
    return biner, proses 
  
print("+==================================+")
print("|    Konversi Desimal ke Biner     |")
print("+==================================+")
n = int(input("   Masukkan bilangan desimal: ")) 
  
biner, proses = desimal_to_biner(n) 

print("+----------------------------------+") 
print("|         Proses konversi:         |") 
print("+----------------------------------+")
for p in proses: 
    print(f"|  {p}") 
print("+----------------------------------+")
print(f"| Hasil     : {biner:12} (biner) |") 
print(f"| Verifikasi: {int(biner, 2):<10} (desimal) |") 
print("+----------------------------------+")
print()
print("+==================================+")
print("| Dosen: Bpk. Yusri Ikhwani, M.Kom |")
print("|   2510010102 - M. Rizky Rinaldy  |")
print("+==================================+")

input() 
              </code></pre>
            </details>
        </li>
      </ul>
    </td>
    <td width="40%">
      <img src="/ALGO2 - Bpk. Yusri Ikhwani, M.Kom/img/KonversiDesimalKeBiner.png" alt="Pratinjau_KonversiDesimalkeBiner">
  <a href="https://github.com/rnld-devcode/Praktikum_2510010102_M.RizkyRinaldy/blob/main/ALGO2%20-%20Bpk.%20Yusri%20Ikhwani%2C%20M.Kom/latihan5_5_biner.py">
        <p align="center"><b>Konversi Desimal ke Biner.</b></p>
  </a>
    </td>
  </tr>
</table>

---

## BAB 6 PENGOLAHAN FILE SEDERHANA
**Pengolahan file** adalah cara program berinteraksi dengan penyimpanan permanen. Berbeda dengan variabel  yang  hanya  ada  selama  program  berjalan,  data  dalam  file  tetap  ada  setelah program ditutup. 
**Fungsi open() memiliki beberapa mode:**
Mode  'r'  untuk  membaca  (read,  default),  'w'  untuk  menulis  dan  menimpa  file  (write), 'a'  untuk menambahkan di akhir file (append), 'r+' untuk baca dan tulis. 
**Rekomendasi penggunaan with statement:**
```bash
with open("data.txt", "w") as f: 
    f.write("Hello, World!") 
# File otomatis tertutup setelah blok selesai
```
Menggunakan  with  membuat  file  otomatis  ditutup  meskipun  terjadi  error,  sehingga  lebih aman daripada pemanggilan open() dan close() manual.

<table>
  <tr>
    <td width="60%">
      <h3>6.1 Menulis File Teks (<code>latihan6_1_tulis_file.py</code>)</h3>
      <ul>
        <li><b>Pengolahan File Sederhana</b></li>
        <li><b>Soal: </b> Buatlah program yang menulis beberapa baris data ke dalam file teks. Data bisa berupa biodata atau catatan sederhana.</li>
        <li><details>
              <summary><b>🔍 Klik untuk melihat Source Code</b></summary>
                <pre style="background: #f4f4f4; padding: 10px; border-radius: 5px; overflow-x: auto;"><code>
print("+==================================+")
print("|       Menulis File Biodata       |")
print("+==================================+")
nama    = input(" --> Nama    : ") 
umur    = input(" --> Umur    : ") 
alamat  = input(" --> Alamat  : ") 
hobi    = input(" --> Hobi    : ") 
  
with open("biodata.txt", "w") as f: 
    f.write("========== BIODATA ==========\n") 

    f.write(f"Nama   : {nama}\n") 
    f.write(f"Umur   : {umur}\n") 
    f.write(f"Alamat : {alamat}\n") 
    f.write(f"Hobi   : {hobi}\n") 

print("+----------------------------------+")
print("|File 'biodata.txt' berhasil dibuat!")
print("+----------------------------------+")
print()
print("+==================================+")
print("| Dosen: Bpk. Yusri Ikhwani, M.Kom |")
print("|   2510010102 - M. Rizky Rinaldy  |")
print("+==================================+")

input() 
               </code></pre>
            </details>
        </li>
      </ul>
    </td>
    <td width="40%">
      <img src="/ALGO2 - Bpk. Yusri Ikhwani, M.Kom/img/MenulisFile.png" alt="Pratinjau_ProgramMenulisFile">
      
  <a href="https://github.com/rnld-devcode/Praktikum_2510010102_M.RizkyRinaldy/blob/main/ALGO2%20-%20Bpk.%20Yusri%20Ikhwani%2C%20M.Kom/latihan6_1_tulis_file.py">
        <p align="center"><b>Program Menulis File</b></p>
  </a>
    </td>
  </tr>
  <tr>
    <td width="60%">
      <h3>6.2 Membaca File Teks (<code>latihan6_2_baca_file.py</code>)</h3>
      <ul>
        <li><b>Pengolahan File Sederhana</b></li>
        <li><b>Soal: </b> Buatlah program yang membaca file teks yang telah dibuat sebelumnya dan menampilkan seluruh isinya.</li>
        <li><details>
              <summary><b>🔍 Klik untuk melihat Source Code</b></summary> 
                <pre style="background: #f4f4f4; padding: 10px; border-radius: 5px; overflow-x: auto;"><code>
print("+==================================+")
print("|       Membaca File Biodata       |")
print("+==================================+")
  
try: 
    with open("biodata.txt", "r") as f: 
        isi = f.read() 
    print(isi) 
  
    print("+-----------Per Baris--------------+")
    with open("biodata.txt", "r") as f: 
        for nomor, baris in enumerate(f, 1): 
            print(f"Baris {nomor}: {baris.rstrip()}") 
except FileNotFoundError: 
    print("File tidak ditemukan! Jalankan latihan 6.1 terlebih dahulu.") 
print("+----------------------------------+")
print()
print("+==================================+")
print("| Dosen: Bpk. Yusri Ikhwani, M.Kom |")
print("|   2510010102 - M. Rizky Rinaldy  |")
print("+==================================+")

input() 
              </code></pre>
          </details>
        </li>
      </ul>
    </td>
    <td width="40%">
      <img src="/ALGO2 - Bpk. Yusri Ikhwani, M.Kom/img/MembacaFile.png" alt="Pratinjau_ProgramMembacaFile">
  <a href="https://github.com/rnld-devcode/Praktikum_2510010102_M.RizkyRinaldy/blob/main/ALGO2%20-%20Bpk.%20Yusri%20Ikhwani%2C%20M.Kom/latihan6_2_baca_file.py">
        <p align="center"><b>Program Pembaca File</b></p>
  </a>
    </td>
  </tr>
  <tr>
    <td width="60%">
      <h3>6.3 Append Data (Catatan Harian) (<code>latihan6_3_catatan.py</code>)</h3>
      <ul>
        <li><b>Pengolahan File Sederhana</b></li>
        <li><b>Soal: </b> Buatlah program catatan harian yang menambahkan catatan baru ke file tanpa menghapus catatan lama. Gunakan mode 'a' (append).</li>
        <li><details>
              <summary><b>🔍 Klik untuk melihat Source Code</b></summary> 
                <pre style="background: #f4f4f4; padding: 10px; border-radius: 5px; overflow-x: auto;"><code>
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
              </code></pre>
            </details>
        </li>
      </ul>
    </td>
    <td width="40%">
      <img src="/ALGO2 - Bpk. Yusri Ikhwani, M.Kom/img/CatatanHarian.png" alt="Pratinjau_ProgramCatatanHarian">
  <a href="https://github.com/rnld-devcode/Praktikum_2510010102_M.RizkyRinaldy/blob/main/ALGO2%20-%20Bpk.%20Yusri%20Ikhwani%2C%20M.Kom/latihan6_3_catatan.py">
        <p align="center"><b>Program Catatan Harian</b></p>
  </a>
    </td>
  </tr>
  <tr>
    <td width="60%">
      <h3>6.4 Menghitung Statistik File (<code>latihan6_4_statistik_file.py</code>)</h3>
      <ul>
        <li><b>Pengolahan File Sederhana</b></li>
        <li><b>Soal: </b> Buatlah  program  yang  membaca  file  teks  lalu  menghitung  jumlah baris,  jumlah  kata,  dan  jumlah karakter.</li>
        <li><details>
              <summary><b>🔍 Klik untuk melihat Source Code</b></summary>
                <pre style="background: #f4f4f4; padding: 10px; border-radius: 5px; overflow-x: auto;"><code>
print("+=================================================+")
print("|              Statistik File Teks                |")
print("+=================================================+")
nama_file = input(" --> Nama file: ") 
  
try: 
    with open(nama_file, "r") as f: 
        isi = f.read() 

    jumlah_baris    = isi.count("\n") + (0 if isi.endswith("\n") else 1) 
    jumlah_kata     = len(isi.split()) 
    jumlah_karakter = len(isi) 
    jumlah_huruf    = sum(1 for c in isi if c.isalpha()) 
   
    print("+-------------------------------------------------+")
    print(f" ==> File            : {nama_file}") 
    print(f" ==> Jumlah baris    : {jumlah_baris}") 
    print(f" ==> Jumlah kata     : {jumlah_kata}") 
    print(f" ==> Jumlah karakter : {jumlah_karakter}") 
    print(f" ==> Jumlah huruf    : {jumlah_huruf}") 
except FileNotFoundError: 
    print(f"File '{nama_file}' tidak ditemukan!")
print("+-------------------------------------------------+")
print()
print("+=================================================+")
print("|        Dosen: Bpk. Yusri Ikhwani, M.Kom         |")
print("|          2510010102 - M. Rizky Rinaldy          |")
print("+=================================================+")

input() 
              </code></pre>
            </details>
        </li>
      </ul>
    </td>
    <td width="40%">
      <img src="/ALGO2 - Bpk. Yusri Ikhwani, M.Kom/img/StatistikFile.png" alt="Pratinjau_StatistikFile">
  <a href="https://github.com/rnld-devcode/Praktikum_2510010102_M.RizkyRinaldy/blob/main/ALGO2%20-%20Bpk.%20Yusri%20Ikhwani%2C%20M.Kom/latihan6_4_statistik_file.py">
        <p align="center"><b>Program Statistik File</b></p>
  </a>
    </td>
  </tr>
  <tr>
  <td width="60%">
      <h3>6.5 Database Sederhana dengan CSV (<code>latihan6_5_csv.py</code>)</h3>
      <ul>
        <li><b>Pengolahan File Sederhana</b></li>
        <li><b>Soal: </b> Buatlah aplikasi sederhana yang menyimpan data mahasiswa dalam format CSV (comma-separated values). Program dapat menambah dan menampilkan semua data.</li>
        <li><details>
              <summary><b>🔍 Klik untuk melihat Source Code</b></summary>
                <pre style="background: #f4f4f4; padding: 10px; border-radius: 5px; overflow-x: auto;"><code>
import os 
  
FILE = "mahasiswa.csv" 
  
def tambah_data(): 
    nim     = input(" --> NIM      : ") 
    nama    = input(" --> Nama     : ") 
    jurusan = input(" --> Jurusan  : ") 
    ipk     = input(" --> IPK      : ") 
    header = not os.path.exists(FILE) 
    with open(FILE, "a") as f: 
        if header: 
            f.write("NIM,Nama,Jurusan,IPK\n") 
        f.write(f"{nim},{nama},{jurusan},{ipk}\n") 

    print("+-----------------------------------------------------------+")
    print("|                 >>> ✓ Data tersimpan <<<                  |") 
    print("+-----------------------------------------------------------+")

def tampil_data(): 
    if not os.path.exists(FILE): 
        print("Belum ada data.") 
        return 
    with open(FILE, "r") as f: 
        print("+-----------------------------------------------------------+")
        for i, baris in enumerate(f): 
            data = baris.strip().split(",") 
            if i == 0: 
                print(f"{data[0]:12s} {data[1]:20s} {data[2]:20s} {data[3]:>5s}") 
                print("+-----------------------------------------------------------+")
            else: 
                print(f"{data[0]:12s} {data[1]:20s} {data[2]:20s} {data[3]:>5s}") 
        print("+-----------------------------------------------------------+")  

print("+===========================================================+")
print("|                 Datbase Sederhana (CSV)                   |")
print("+===========================================================+")
print("| >>> 1. Tambah Data") 
print("| >>> 2. Lihat Data") 
print("| >>> 3. Keluar") 
print("+-----------------------------------------------------------+")
while True: 
    p = input(" ==> Pilihan: ") 
    if   p == "1": tambah_data() 
    elif p == "2": tampil_data() 
    elif p == "3": break 
print()
print("+===========================================================+")
print("|             Dosen: Bpk. Yusri Ikhwani, M.Kom              |")
print("|               2510010102 - M. Rizky Rinaldy               |")
print("+===========================================================+")

input() 
              </code></pre>
            </details>
        </li>
      </ul>
    </td>
    <td width="40%">
      <img src="/ALGO2 - Bpk. Yusri Ikhwani, M.Kom/img/DatabaseSederhanaCSV.png" alt="Pratinjau_DatabaseSederhanaCSV">
  <a href="https://github.com/rnld-devcode/Praktikum_2510010102_M.RizkyRinaldy/blob/main/ALGO2%20-%20Bpk.%20Yusri%20Ikhwani%2C%20M.Kom/latihan6_5_csv.py">
        <p align="center"><b>Database Sederhana dengan CSV</b></p>
  </a>
    </td>
  </tr>
</table>

---

## BAB 7 DEBUGGING DAN ERROR HANDLING
Dalam  pemrograman,  error  (kesalahan)  adalah  hal  yang  wajar  terjadi.  Terdapat  tiga  jenis  error utama di Python: 
**1. Syntax Error** 
Kesalahan  penulisan  kode  yang  tidak  sesuai  aturan  bahasa  Python.  Program  tidak  akan  berjalan sama sekali sebelum syntax diperbaiki. 
**2. Runtime Error (Exception)**
Error yang terjadi saat program berjalan. Contoh: ZeroDivisionError, ValueError, FileNotFoundError,TypeError. 
**3. Logic Error**
Program berjalan tanpa error tapi memberikan hasil yang salah. Ini biasanya paling sulit ditemukan karena butuh pengecekan logika program. 
**Struktur try-except:** 
```bash
try: 
    # kode yang mungkin menimbulkan error 
except JenisError as e: 
    # penanganan error 
else: 
    # dijalankan jika tidak ada error 
finally: 
    # selalu dijalankan
```

<table>
  <tr>
    <td width="60%">
      <h3>7.1 Validasi Input Numerik (<code>latihan7_1_validasi.py</code>)</h3>
      <ul>
        <li><b>Debugging dan Error Handling</b></li>
        <li><b>Soal: </b> Buatlah program yang meminta input angka dari user. Jika user memasukkan bukan angka, program tidak crash tapi meminta ulang.</li>
        <li><details>
              <summary><b>🔍 Klik untuk melihat Source Code</b></summary>
                <pre style="background: #f4f4f4; padding: 10px; border-radius: 5px; overflow-x: auto;"><code>
print("+==================================+")
print("|          Validasi Input          |")
print("+==================================+")
  
while True: 
    try: 
        angka = float(input(" ==> Masukkan angka: ")) 
        break 
    except ValueError: 
        print("+----------------------------------+")
        print("| ❌ Input bukan angka, coba lagi! |") 
        print("+----------------------------------+")
 
print("+----------------------------------+")
print(f"| ✓ Anda memasukkan : {angka:<10}   |") 
print(f"|  Kuadratnya       : {angka ** 2:<10}   |") 
print("+----------------------------------+")
print()
print("+==================================+")
print("| Dosen: Bpk. Yusri Ikhwani, M.Kom |")
print("|   2510010102 - M. Rizky Rinaldy  |")
print("+==================================+")

input() 
               </code></pre>
            </details>
        </li>
      </ul>
    </td>
    <td width="40%">
      <img src="/ALGO2 - Bpk. Yusri Ikhwani, M.Kom/img/ValidasiInput.png" alt="Pratinjau_ValidasiInput">
      
  <a href="https://github.com/rnld-devcode/Praktikum_2510010102_M.RizkyRinaldy/blob/main/ALGO2%20-%20Bpk.%20Yusri%20Ikhwani%2C%20M.Kom/latihan7_1_validasi.py">
        <p align="center"><b>Program Validasi Input</b></p>
  </a>
    </td>
  </tr>
  <tr>
    <td width="60%">
      <h3>7.2 Menangani Pembagian Nol (<code>latihan7_2_bagi_nol.py</code>)</h3>
      <ul>
        <li><b>Debugging dan Error Handling</b></li>
        <li><b>Soal: </b> Buatlah program kalkulator pembagian yang dapat menangani pembagian dengan nol (ZeroDivisionError).</li>
        <li><details>
              <summary><b>🔍 Klik untuk melihat Source Code</b></summary> 
                <pre style="background: #f4f4f4; padding: 10px; border-radius: 5px; overflow-x: auto;"><code>
print("+==========================================+")
print("|           Kalkulator Pembagian           |")
print("+==========================================+")
  
try: 
    a = float(input(" --> Pembilang : ")) 
    b = float(input(" --> Penyebut  : ")) 
    hasil = a / b 
except ZeroDivisionError: 
    print("+------------------------------------------+")
    print("| ❌ Error: Tidak bisa dibagi dengan nol!  |") 
    print("+------------------------------------------+")
except ValueError: 
    print("+------------------------------------------+")
    print("| ❌ Error: Input harus berupa angka!      |") 
    print("+------------------------------------------+")

else: 
    print("+------------------------------------------+")
    print(f"| ✓ {a:>6} / {b:<6} = {hasil:<20.4f} |") 
    print("+------------------------------------------+")

finally: 
    print("+------------------------------------------+")
    print("|         >>> (Proses selesai) <<<         |")
print("+------------------------------------------+")
print()
print("+==========================================+")
print("|     Dosen: Bpk. Yusri Ikhwani, M.Kom     |")
print("|       2510010102 - M. Rizky Rinaldy      |")
print("+==========================================+")

input() 
              </code></pre>
          </details>
        </li>
      </ul>
    </td>
    <td width="40%">
      <img src="/ALGO2 - Bpk. Yusri Ikhwani, M.Kom/img/KalkulatorPembagian.png" alt="Pratinjau_KalkulatorPembagian">
  <a href="https://github.com/rnld-devcode/Praktikum_2510010102_M.RizkyRinaldy/blob/main/ALGO2%20-%20Bpk.%20Yusri%20Ikhwani%2C%20M.Kom/latihan7_2_bagi_nol.py">
        <p align="center"><b>Kalkulator Pembagian</b></p>
  </a>
    </td>
  </tr>
  <tr>
    <td width="60%">
      <h3>7.3 Menangani File Tidak Ditemukan (<code>latihan7_3_file_error.py</code>)</h3>
      <ul>
        <li><b>Debugging dan Error Handling</b></li>
        <li><b>Soal: </b> BBuatlah  program  yang  mencoba  membaca  sebuah  file.  Jika  file  tidak  ada,  tampilkan  pesan  yang informatif tanpa crash.</li>
        <li><details>
              <summary><b>🔍 Klik untuk melihat Source Code</b></summary> 
                <pre style="background: #f4f4f4; padding: 10px; border-radius: 5px; overflow-x: auto;"><code>
print("+====================================================+")
print("|                     Pembaca File                   |")
print("+====================================================+")
nama_file = input(" ==> Nama file: ") 
  
try: 
    with open(nama_file, "r") as f: 
        isi = f.read() 
    print("+----------------------------------------------------+")
    print("|             --- >>> Isi File <<< ---               |") 
    print("+----------------------------------------------------+")
    print(isi) 
except FileNotFoundError: 
    print("+----------------------------------------------------+")
    print(f"| ❌ File '{nama_file:<23}' tidak ditemukan. |") 
    print("+----------------------------------------------------+")
    pilih = input(" ==> Buat file baru? (Y/T): ").upper() 
    if pilih == "Y": 
        konten = input(" --> Tulis isi file: ") 
        with open(nama_file, "w") as f: 
            f.write(konten) 
        print("+----------------------------------------------------+")
        print(f"| ✓ File '{nama_file:<31}' dibuat. |") 
        print("+----------------------------------------------------+")

except PermissionError: 
    print("+----------------------------------------------------+")
    print(f"❌ Tidak punya izin akses ke '{nama_file}'.") 
    print("+----------------------------------------------------+")

except Exception as e: 
    print("+----------------------------------------------------+")
    print(f"❌ Error tak terduga: {type(e).__name__}: {e}") 
    print("+----------------------------------------------------+")

print()
print("+====================================================+")
print("|          Dosen: Bpk. Yusri Ikhwani, M.Kom          |")
print("|            2510010102 - M. Rizky Rinaldy           |")
print("+====================================================+")

input() 
              </code></pre>
            </details>
        </li>
      </ul>
    </td>
    <td width="40%">
      <img src="/ALGO2 - Bpk. Yusri Ikhwani, M.Kom/img/PembacaFile.png" alt="Pratinjau_ProgramPembacaFile">
  <a href="https://github.com/rnld-devcode/Praktikum_2510010102_M.RizkyRinaldy/blob/main/ALGO2%20-%20Bpk.%20Yusri%20Ikhwani%2C%20M.Kom/latihan7_3_file_error.py">
        <p align="center"><b>Program Pembaca File</b></p>
  </a>
    </td>
  </tr>
  <tr>
    <td width="60%">
      <h3>7.4 Custom Exception dengan raise (<code>latihan7_4_raise.py</code>)</h3>
      <ul>
        <li><b>Debugging dan Error Handling</b></li>
        <li><b>Soal: </b> Buatlah program validasi umur dengan aturan: umur harus 0-120. Gunakan raise untuk melempar exception jika tidak valid.</li>
        <li><details>
              <summary><b>🔍 Klik untuk melihat Source Code</b></summary>
                <pre style="background: #f4f4f4; padding: 10px; border-radius: 5px; overflow-x: auto;"><code>
def validasi_umur(umur): 
    if not isinstance(umur, (int, float)): 
        raise TypeError("Umur harus berupa angka") 
    if umur < 0: 
        raise ValueError("Umur tidak boleh negatif") 
    if umur > 120: 
        raise ValueError("Umur tidak realistis (>120)") 
    return True 

print("+==========================================+")
print("|              Validasi Umur               |")
print("+==========================================+") 
  
try: 
    umur = int(input(" ==> Umur Anda: ")) 
    validasi_umur(umur) 
    print("+------------------------------------------+")
    print(f"|         ✓ Umur {umur:<11} valid         |") 
    print("+------------------------------------------+")
    if umur < 17: 
        print("+------------------------------------------+")
        print("|    >>> Kategori: Anak-anak/Remaja <<<    |") 
    elif umur < 60: 
        print("+------------------------------------------+")
        print("|         >>> Kategori: Dewasa <<<         |") 
    else: 
        print("+------------------------------------------+")
        print("|         >>> Kategori: Lansia <<<         |") 

except ValueError as e: 
    print("+------------------------------------------+")
    print(f"|  ❌ Error:  {e}  |") 
except TypeError as e: 
    print("+------------------------------------------+")
    print(f"|  ❌ Error:  {e}  |")


print("+------------------------------------------+")
print()
print("+==========================================+")
print("|     Dosen: Bpk. Yusri Ikhwani, M.Kom     |")
print("|       2510010102 - M. Rizky Rinaldy      |")
print("+==========================================+")

input() 
              </code></pre>
            </details>
        </li>
      </ul>
    </td>
    <td width="40%">
      <img src="/ALGO2 - Bpk. Yusri Ikhwani, M.Kom/img/ValidasiUmur.png" alt="Pratinjau_ValidasiUmur">
  <a href="https://github.com/rnld-devcode/Praktikum_2510010102_M.RizkyRinaldy/blob/main/ALGO2%20-%20Bpk.%20Yusri%20Ikhwani%2C%20M.Kom/latihan7_4_raise.py">
        <p align="center"><b>Program Validasi Umur</b></p>
  </a>
    </td>
  </tr>
  <tr>
  <td width="60%">
      <h3>7.5 Debugging dengan Print Statement (<code>latihan7_5_debug.py</code>)</h3>
      <ul>
        <li><b>Debugging dan Error Handling</b></li>
        <li><b>Soal: </b> Program berikut memiliki logic error. Gunakan print statement untuk men-debug dan menemukan kesalahannya. Program seharusnya menghitung rata-rata.</li>
        <li><details>
              <summary><b>🔍 Klik untuk melihat Source Code</b></summary>
                <pre style="background: #f4f4f4; padding: 10px; border-radius: 5px; overflow-x: auto;"><code>
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
              </code></pre>
            </details>
        </li>
      </ul>
    </td>
    <td width="40%">
      <img src="/ALGO2 - Bpk. Yusri Ikhwani, M.Kom/img/DebugRata-rata.png" alt="Pratinjau_DebugRataRata">
  <a href="https://github.com/rnld-devcode/Praktikum_2510010102_M.RizkyRinaldy/blob/main/ALGO2%20-%20Bpk.%20Yusri%20Ikhwani%2C%20M.Kom/latihan6_5_csv.py">
        <p align="center"><b>Program Data Rata-rata</b></p>
  </a>
    </td>
  </tr>
</table>

---

## BAB 8  MINI PROJECT (STUDI KASUS)
**Aplikasi Kasir Toko Sederhana**

Pada bagian ini, kita akan membuat sebuah aplikasi kasir sederhana untuk sebuah toko kelontong. 
Aplikasi  ini  menggabungkan  seluruh  konsep  yang  sudah  dipelajari:  percabangan, perulangan, struktur data, fungsi, pengolahan file, serta error handling. Aplikasi juga dilengkapi fitur cetak struk belanja yang disimpan dalam file teks. 

**Fitur yang tersedia:** 
1. Tambah barang ke daftar produk. 
2. Lihat daftar produk. 
3. Mulai transaksi pembelian (keranjang). 
4. Hitung  total  dan  proses  pembayaran.  
5. Cetak  struk  ke  file  teks  dan  layar.  
6. Lihat  riwayat transaksi. 

<div align="center">
  <img src="/ALGO2 - Bpk. Yusri Ikhwani, M.Kom/img/TampilanMenu.png" width="600" style="border-radius: 16px; box-shadow: 0 4px 8px rgba(0,0,0,0.2);">
  <p><b>Menu Utama Aplikasi</b></p>
</div>
<div align="center">
  <img src="/ALGO2 - Bpk. Yusri Ikhwani, M.Kom/img/MenuTambahProduk.png" width="600" style="border-radius: 16px; box-shadow: 0 4px 8px rgba(0,0,0,0.2);">
  <p><b>Menu Tambah Produk</b></p>
</div>
<div align="center">
  <img src="/ALGO2 - Bpk. Yusri Ikhwani, M.Kom/img/MenuDaftarProduk.png" width="600" style="border-radius: 16px; box-shadow: 0 4px 8px rgba(0,0,0,0.2);">
  <p><b>Menu Daftar Produk</b></p>
</div>
<div align="center">
  <img src="/ALGO2 - Bpk. Yusri Ikhwani, M.Kom/img/MenuTransaksi.png" width="600" style="border-radius: 16px; box-shadow: 0 4px 8px rgba(0,0,0,0.2);">
  <p><b>Menu Transaki Produk</b></p>
</div>
</div>
<div align="center">
  <img src="/ALGO2 - Bpk. Yusri Ikhwani, M.Kom/img/TampilanStruk.png" width="600" style="border-radius: 16px; box-shadow: 0 4px 8px rgba(0,0,0,0.2);">
  <p><b>Struk Transaki</b></p>
</div>
<div align="center">
  <img src="/ALGO2 - Bpk. Yusri Ikhwani, M.Kom/img/LaporanRiwayatTransaksi.png" width="600" style="border-radius: 16px; box-shadow: 0 4px 8px rgba(0,0,0,0.2);">
  <p><b>Laporan Riwayat Transaki</b></p>
</div>

<a href="https://github.com/rnld-devcode/Praktikum_2510010102_M.RizkyRinaldy/blob/main/ALGO2%20-%20Bpk.%20Yusri%20Ikhwani%2C%20M.Kom/mini_project_kasir.py">
    <p align="center"><b>Source Code Program <code>mini_project_kasir.py</code></b></p>
</a>


**Penjelasan Struktur Program**
Program  di  atas  mendemonstrasikan  integrasi  berbagai  konsep  yang  dipelajari  pada  bab-bab sebelumnya.  Struktur  data  Dictionary  digunakan  untuk  menyimpan  produk  dengan  kode  sebagai key. List digunakan untuk keranjang belanja. Fungsi-fungsi dipisah berdasarkan tanggung jawabnya, misalnya tambah_produk, transaksi, dan cetak_struk. 

Pengolahan file diterapkan pada tiga tempat: file  produk.txt menyimpan daftar produk, file 
riwayat_transaksi.txt  mencatat  semua  transaksi,  dan  folder  struk/  berisi  file  struk  untuk  setiap transaksi. Error handling diterapkan melalui fungsi input_angka yang memvalidasi input user serta blok  try-except  pada  operasi  file.  Percabangan  dan  perulangan  digunakan  pada  hampir  seluruh bagian program untuk mengontrol alur eksekusi. 

**Pengembangan Lanjutan**
Setelah  memahami  program  ini,  mahasiswa  ditantang  untuk  mengembangkan  fitur  tambahan 
seperti: manajemen stok barang (otomatis berkurang saat terjual), laporan penjualan harian/bulanan, sistem member dengan poin, kategori produk, fitur edit dan hapus produk, serta export laporan ke format CSV untuk analisis lebih lanjut. 

---

## 💻 Prasyarat & Lingkungan Pengembangan

Untuk mengompilasi dan menjalankan program-program di atas, Anda memerlukan:
* **Python Interpreter** Download: Kunjungi situs resmi [python.org](https://www.python.org/).
* Rekomendasi IDE/Text Editor: **VS Code (Visual Studio Code)**, **PyCharm**, atau **IDLE:** IDE bawaan yang langsung terinstal saat Anda menginstal Python. .

---



## 🚀 Cara Menjalankan Program lewat Terminal

Pilih salah satu file tugas yang ingin dijalankan, kemudian ikuti langkah-langkah berikut melalui Terminal atau Command Prompt:

1. **Akses File Hasil Download Lewat Terminal:**
   ```bash
    cd C:\Users\rizky\Downloads\
   ```

   > 📌 Note : rizky --> ganti ke nama user sesuai profile di komputer Anda
   
2. **Jalankan file:**
   ```bash
   python namafile.py
   ```

   contoh menjalankan file latihan1_1_kelulusan.py

   ```bash
   python latihan1_1_kelulusan.py
   ```
<div align="center">
  <img src="/ALGO2 - Bpk. Yusri Ikhwani, M.Kom/img/JalankanFilePython.png" width="600" style="border-radius: 16px; box-shadow: 0 4px 8px rgba(0,0,0,0.2);">
  <p><b>Langkah Menjalankan Program.</b></p>
</div>
<p align="center">
  <a href="#-repositori-praktikum-algo---bpk-yusri-ikhwani-m-kom">🔺 Kembali ke Atas</a>
</p>
<div align="center">© 2026 M. Rizky Rinaldy. All Rights Reserved.</div>
