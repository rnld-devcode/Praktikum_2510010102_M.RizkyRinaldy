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
        <li><b>SourceCode:</b> 
            <pre style="background: #f4f4f4; padding: 10px; border-radius: 5px; overflow-x: auto;">
              <code>
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
              </code>
            </pre>
        </li>
      </ul>
    </td>
    <td width="40%">
      <img src="/ALGO2 - Bpk. Yusri Ikhwani, M.Kom/img/ProgramCekKelulusan.png" alt="Pratinjau_ProgramCekKelulusan">
      
  <a href="https://github.com/rnld-devcode/Praktikum_2510010102_M.RizkyRinaldy/blob/main/ALGO2%20-%20Bpk.%20Yusri%20Ikhwani%2C%20M.Kom/latihan1_1_kelulusan.py">
        <p><b>Program Pengecekan Kelulusan.</b></p>
  </a>
    </td>
  </tr>
  <tr>
    <td width="60%">
      <h3>1.2 Program Konversi Nilai ke Huruf (<code>latihan1_2_nilaihuruf.py</code>)</h3>
      <ul>
        <li><b>Percabangan (Selection)</b></li>
        <li><b>Soal: </b> Buatlah program yang mengkonversi nilai angka menjadi nilai huruf dengan ketentuan: A (>=85), B (70-84), C (55-69), D (40-54), E (<\40). </li>
        <li><b>SourceCode:</b> 
            <pre style="background: #f4f4f4; padding: 10px; border-radius: 5px; overflow-x: auto;">
              <code>
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
              </code>
            </pre>
        </li>
      </ul>
    </td>
    <td width="40%">
      <img src="/ALGO2 - Bpk. Yusri Ikhwani, M.Kom/img/ProgramKonversiNilaiHuruf.png" alt="Pratinjau_ProgramKonversiNilaiHuruf">
  <a href="https://github.com/rnld-devcode/Praktikum_2510010102_M.RizkyRinaldy/blob/main/ALGO2%20-%20Bpk.%20Yusri%20Ikhwani%2C%20M.Kom/latihan1_2_nilaihuruf.py">
        <p><b>Program Konversi Nilai Ke Huruf.</b></p>
  </a>
    </td>
  </tr>
  <tr>
    <td width="60%">
      <h3>1.3 Kalkulator BMI (<code>latihan1_3_bmi.py</code>)</h3>
      <ul>
        <li><b>Percabangan (Selection)</b></li>
        <li><b>Soal: </b> Buatlah  program  yang  menghitung  BMI dengan  rumus  BMI  =  berat  /  (tinggi**2).  Kategori:  Kurus (<\18.5), Normal (18.5-24.9), Gemuk (25-29.9), Obesitas (>=30).</li>
        <li><b>SourceCode:</b> 
            <pre style="background: #f4f4f4; padding: 10px; border-radius: 5px; overflow-x: auto;">
              <code>
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
              </code>
            </pre>
        </li>
      </ul>
    </td>
    <td width="40%">
      <img src="/ALGO2 - Bpk. Yusri Ikhwani, M.Kom/img/KalkulatorBMI.png" alt="Pratinjau_KalkulatorBMI">
  <a href="https://github.com/rnld-devcode/Praktikum_2510010102_M.RizkyRinaldy/blob/main/ALGO2%20-%20Bpk.%20Yusri%20Ikhwani%2C%20M.Kom/latihan1_3_bmi.py">
        <p><b>Kalkulator BMI (Body Mass Index).</b></p>
  </a>
    </td>
  </tr>
  <tr>
    <td width="60%">
      <h3>1.4 Program Tiket Bioskop dengan Diskon (<code>latihan1_4_tiket.py</code>)</h3>
      <ul>
        <li><b>Percabangan (Selection)</b></li>
        <li><b>Soal: </b>  Buatlah program harga tiket bioskop. Harga normal Rp. 50.000. Diskon 50% untuk umur <\12 atau >60 tahun. Diskon 20% untuk pelajar (input Y/T).</li>
        <li><b>SourceCode:</b> 
            <pre style="background: #f4f4f4; padding: 10px; border-radius: 5px; overflow-x: auto;">
              <code>
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
              </code>
            </pre>
        </li>
      </ul>
    </td>
    <td width="40%">
      <img src="/ALGO2 - Bpk. Yusri Ikhwani, M.Kom/img/ProgramLoketTiket.png" alt="Pratinjau_LoketTiket">
  <a href="https://github.com/rnld-devcode/Praktikum_2510010102_M.RizkyRinaldy/blob/main/ALGO2%20-%20Bpk.%20Yusri%20Ikhwani%2C%20M.Kom/latihan1_4_tiket.py">
        <p><b>Program Tiket Bioskop dengan Diskon.</b></p>
  </a>
    </td>
  </tr>
  <tr>
  <td width="60%">
      <h3>1.5 Program Penentu Jenis Segitiga (<code>latihan1_5_segitiga.py</code>)</h3>
      <ul>
        <li><b>Percabangan (Selection)</b></li>
        <li><b>Soal: </b> Buatlah program yang menerima input tiga sisi segitiga kemudian menentukan jenisnya: sama sisi, sama kaki, atau sembarang. Program juga memvalidasi apakah ketiga sisi membentuk segitiga yang valid.</li>
        <li><b>SourceCode:</b> 
            <pre style="background: #f4f4f4; padding: 10px; border-radius: 5px; overflow-x: auto;">
              <code>
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
              </code>
            </pre>
        </li>
      </ul>
    </td>
    <td width="40%">
      <img src="/ALGO2 - Bpk. Yusri Ikhwani, M.Kom/img/PenentuJenisSegitiga.png" alt="Pratinjau_PenentuJenisSegitiga">
  <a href="https://github.com/rnld-devcode/Praktikum_2510010102_M.RizkyRinaldy/blob/main/ALGO2%20-%20Bpk.%20Yusri%20Ikhwani%2C%20M.Kom/latihan1_5_segitiga.py">
        <p><b>Program Penentu Jenis Segitiga.</b></p>
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
        <li><b>SourceCode:</b> 
            <pre style="background: #f4f4f4; padding: 10px; border-radius: 5px; overflow-x: auto;">
              <code>
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
              </code>
            </pre>
        </li>
      </ul>
    </td>
    <td width="40%">
      <img src="/ALGO2 - Bpk. Yusri Ikhwani, M.Kom/img/KamusPerkalian.png" alt="Pratinjau_ProgramKamusPerkalian">
      
  <a href="https://github.com/rnld-devcode/Praktikum_2510010102_M.RizkyRinaldy/blob/main/ALGO2%20-%20Bpk.%20Yusri%20Ikhwani%2C%20M.Kom/latihan2_1_perkalian.py">
        <p><b>Program Tabel Perkalian.</b></p>
  </a>
    </td>
  </tr>
  <tr>
    <td width="60%">
      <h3>2.2 Program Menghitung Faktorial (<code>latihan2_2_faktorial.py</code>)</h3>
      <ul>
        <li><b>Perulangan (Looping)</b></li>
        <li><b>Soal: </b> Buatlah program yang menghitung faktorial dari bilangan bulat positif yang diinput. Faktorial n! = 1 × 2 × 3 × ... × n. </li>
        <li><b>SourceCode:</b> 
            <pre style="background: #f4f4f4; padding: 10px; border-radius: 5px; overflow-x: auto;">
              <code>
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
              </code>
            </pre>
        </li>
      </ul>
    </td>
    <td width="40%">
      <img src="/ALGO2 - Bpk. Yusri Ikhwani, M.Kom/img/KalkulatorFaktorial.png" alt="Pratinjau_ProgramMenghitungFaktorial">
  <a href="https://github.com/rnld-devcode/Praktikum_2510010102_M.RizkyRinaldy/blob/main/ALGO2%20-%20Bpk.%20Yusri%20Ikhwani%2C%20M.Kom/latihan2_2_faktorial.py">
        <p><b>Program Menghitung Faktorial.</b></p>
  </a>
    </td>
  </tr>
  <tr>
    <td width="60%">
      <h3>2.3 Deret Fibonacci (<code>latihan2_3_fibonacci.py</code>)</h3>
      <ul>
        <li><b>Perulangan (Looping)</b></li>
        <li><b>Soal: </b> Buatlah program yang menampilkan deret Fibonacci sebanyak N suku. Deret Fibonacci: 0, 1, 1, 2, 3, 5, 8, 13, ... </li>
        <li><b>SourceCode:</b> 
            <pre style="background: #f4f4f4; padding: 10px; border-radius: 5px; overflow-x: auto;">
              <code>
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
              </code>
            </pre>
        </li>
      </ul>
    </td>
    <td width="40%">
      <img src="/ALGO2 - Bpk. Yusri Ikhwani, M.Kom/img/DeretFibonacci.png" alt="Pratinjau_DeretFibonacci">
  <a href="https://github.com/rnld-devcode/Praktikum_2510010102_M.RizkyRinaldy/blob/main/ALGO2%20-%20Bpk.%20Yusri%20Ikhwani%2C%20M.Kom/latihan2_3_fibonacci.py">
        <p><b>Deret Fibonacci.</b></p>
  </a>
    </td>
  </tr>
  <tr>
    <td width="60%">
      <h3>2.4 Menebak Angka (While-break) (<code>latihan2_4_tebak_angka.py</code>)</h3>
      <ul>
        <li><b>Perulangan (Looping)</b></li>
        <li><b>Soal: </b>  Buatlah  game  sederhana:  komputer  memikirkan  angka  1-20,  user  menebak.  Program  memberi petunjuk 'Terlalu besar' atau 'Terlalu kecil' sampai tebakan benar.</li>
        <li><b>SourceCode:</b> 
            <pre style="background: #f4f4f4; padding: 10px; border-radius: 5px; overflow-x: auto;">
              <code>
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
              </code>
            </pre>
        </li>
      </ul>
    </td>
    <td width="40%">
      <img src="/ALGO2 - Bpk. Yusri Ikhwani, M.Kom/img/GameTebakAngka.png" alt="Pratinjau_GameTebakAngka">
  <a href="https://github.com/rnld-devcode/Praktikum_2510010102_M.RizkyRinaldy/blob/main/ALGO2%20-%20Bpk.%20Yusri%20Ikhwani%2C%20M.Kom/latihan2_4_tebak_angka.py">
        <p><b>Game Tebak Angka Random</b></p>
  </a>
    </td>
  </tr>
  <tr>
  <td width="60%">
      <h3>2.5 Program Pola Piramida Angka (<code>latihan2_5_piramida.py</code>)</h3>
      <ul>
        <li><b>Perulangan (Looping)</b></li>
        <li><b>Soal: </b> Buatlah  program  yang  menampilkan  pola  piramida  angka  menggunakan  perulangan  bersarang (nested loop).</li>
        <li><b>SourceCode:</b> 
            <pre style="background: #f4f4f4; padding: 10px; border-radius: 5px; overflow-x: auto;">
              <code>
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
              </code>
            </pre>
        </li>
      </ul>
    </td>
    <td width="40%">
      <img src="/ALGO2 - Bpk. Yusri Ikhwani, M.Kom/img/PiramidaAngka.png" alt="Pratinjau_PolaPiramidaAngka">
  <a href="https://github.com/rnld-devcode/Praktikum_2510010102_M.RizkyRinaldy/blob/main/ALGO2%20-%20Bpk.%20Yusri%20Ikhwani%2C%20M.Kom/latihan2_5_piramida.py">
        <p><b>Program Pola Piramida Angka.</b></p>
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
        <li><b>SourceCode:</b> 
            <pre style="background: #f4f4f4; padding: 10px; border-radius: 5px; overflow-x: auto;">
              <code>
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
              </code>
            </pre>
        </li>
      </ul>
    </td>
    <td width="40%">
      <img src="/ALGO2 - Bpk. Yusri Ikhwani, M.Kom/img/ListBelanja.png" alt="Pratinjau_ProgramDaftarBelanjaan">
      
  <a href="https://github.com/rnld-devcode/Praktikum_2510010102_M.RizkyRinaldy/blob/main/ALGO2%20-%20Bpk.%20Yusri%20Ikhwani%2C%20M.Kom/latihan3_1_list_belanja.py">
        <p><b>Program Daftar Belanjaan.</b></p>
  </a>
    </td>
  </tr>
  <tr>
    <td width="60%">
      <h3>3.2 Statistika Nilai Mahasiswa (List) (<code>latihan3_2_statistik.py</code>)</h3>
      <ul>
        <li><b>Struktur Data Dasar</b></li>
        <li><b>Soal: </b> Buatlah program yang menerima N nilai mahasiswa, lalu menampilkan nilai tertinggi, terendah, rata-rata, dan jumlah total.</li>
        <li><b>SourceCode:</b> 
            <pre style="background: #f4f4f4; padding: 10px; border-radius: 5px; overflow-x: auto;">
              <code>
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
              </code>
            </pre>
        </li>
      </ul>
    </td>
    <td width="40%">
      <img src="/ALGO2 - Bpk. Yusri Ikhwani, M.Kom/img/StatistikNilaiMahasiswa.png" alt="Pratinjau_ProgramStatistik">
  <a href="https://github.com/rnld-devcode/Praktikum_2510010102_M.RizkyRinaldy/blob/main/ALGO2%20-%20Bpk.%20Yusri%20Ikhwani%2C%20M.Kom/latihan3_2_statistik.py">
        <p><b>Program Statistika Nilai Mahasiswa.</b></p>
  </a>
    </td>
  </tr>
  <tr>
    <td width="60%">
      <h3>3.3 Data Mahasiswa (Dictionary) (<code>latihan3_3_dictionary.py</code>)</h3>
      <ul>
        <li><b>Struktur Data Dasar</b></li>
        <li><b>Soal: </b> Buatlah program yang menyimpan data mahasiswa menggunakan dictionary, kemudian menampilkannya dalam format rapi.</li>
        <li><b>SourceCode:</b> 
            <pre style="background: #f4f4f4; padding: 10px; border-radius: 5px; overflow-x: auto;">
              <code>
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
              </code>
            </pre>
        </li>
      </ul>
    </td>
    <td width="40%">
      <img src="/ALGO2 - Bpk. Yusri Ikhwani, M.Kom/img/DataMahasiswa.png" alt="Pratinjau_ProgramDataMahasiswa">
  <a href="https://github.com/rnld-devcode/Praktikum_2510010102_M.RizkyRinaldy/blob/main/ALGO2%20-%20Bpk.%20Yusri%20Ikhwani%2C%20M.Kom/latihan3_3_dictionary.py">
        <p><b>Program Data Mahasiswa</b></p>
  </a>
    </td>
  </tr>
  <tr>
    <td width="60%">
      <h3>3.4 Menghitung Frekuensi Huruf (Dictionary) (<code>latihan3_4_frekuensi.py</code>)</h3>
      <ul>
        <li><b>Struktur Data Dasar</b></li>
        <li><b>Soal: </b> Buatlah program yang menghitung berapa kali setiap huruf muncul dalam sebuah kalimat menggunakan dictionary.</li>
        <li><b>SourceCode:</b> 
            <pre style="background: #f4f4f4; padding: 10px; border-radius: 5px; overflow-x: auto;">
              <code>
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
              </code>
            </pre>
        </li>
      </ul>
    </td>
    <td width="40%">
      <img src="/ALGO2 - Bpk. Yusri Ikhwani, M.Kom/img/FrekuensiHuruf.png" alt="Pratinjau_FrekuensiHuruf">
  <a href="https://github.com/rnld-devcode/Praktikum_2510010102_M.RizkyRinaldy/blob/main/ALGO2%20-%20Bpk.%20Yusri%20Ikhwani%2C%20M.Kom/latihan3_4_frekuensi.py">
        <p><b>Menghitung Frekuensi Huruf</b></p>
  </a>
    </td>
  </tr>
  <tr>
  <td width="60%">
      <h3>3.5 Operasi Himpunan (Set) (<code>latihan3_5_set.py</code>)</h3>
      <ul>
        <li><b>Perulangan (Looping)</b></li>
        <li><b>Soal: </b> Buatlah  program  yang  menerima  dua  himpunan  bilangan,  kemudian  menampilkan  hasil  operasi gabungan (union), irisan (intersection), dan selisih (difference). </li>
        <li><b>SourceCode:</b> 
            <pre style="background: #f4f4f4; padding: 10px; border-radius: 5px; overflow-x: auto;">
              <code>
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
              </code>
            </pre>
        </li>
      </ul>
    </td>
    <td width="40%">
      <img src="/ALGO2 - Bpk. Yusri Ikhwani, M.Kom/img/OperasiHimpunan.png" alt="Pratinjau_OperasiHimpunan">
  <a href="https://github.com/rnld-devcode/Praktikum_2510010102_M.RizkyRinaldy/blob/main/ALGO2%20-%20Bpk.%20Yusri%20Ikhwani%2C%20M.Kom/latihan3_5_set.py">
        <p><b>Operasi Himpunan.</b></p>
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
        <li><b>Struktur Data Dasar</b></li>
        <li><b>Soal: </b> Buatlah fungsi untuk mengkonversi suhu antara Celcius, Fahrenheit, dan Reamur menggunakan tiga fungsi terpisah.</li>
        <li><b>SourceCode:</b>
            <details>
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
        <p><b>Program Konversi Suhu.</b></p>
  </a>
    </td>
  </tr>
  <tr>
    <td width="60%">
      <h3>4.2 Fungsi Cek Bilangan Prima (<code>latihan4_2_prima.py</code>)</h3>
      <ul>
        <li><b>Struktur Data Dasar</b></li>
        <li><b>Soal: </b> Buatlah fungsi yang mengembalikan True jika sebuah bilangan adalah prima, dan False jika bukan. Gunakan fungsi tersebut untuk mencetak bilangan prima dari 1 sampai N. </li>
        <li><b>SourceCode:</b> 
            <pre style="background: #f4f4f4; padding: 10px; border-radius: 5px; overflow-x: auto;">
              <code>
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
              </code>
            </pre>
        </li>
      </ul>
    </td>
    <td width="40%">
      <img src="/ALGO2 - Bpk. Yusri Ikhwani, M.Kom/img/BilanganPrima.png" alt="Pratinjau_ProgramBilanganPrima">
  <a href="https://github.com/rnld-devcode/Praktikum_2510010102_M.RizkyRinaldy/blob/main/ALGO2%20-%20Bpk.%20Yusri%20Ikhwani%2C%20M.Kom/latihan4_2_prima.py">
        <p><b>Program Pencari Bilangan Prima.</b></p>
  </a>
    </td>
  </tr>
  <tr>
    <td width="60%">
      <h3>4.3 Fungsi dengan Default Parameter (<code>latihan4_3_diskon.py</code>)</h3>
      <ul>
        <li><b>Struktur Data Dasar</b></li>
        <li><b>Soal: </b> Buatlah  fungsi  penghitung  harga  setelah  diskon  dengan  parameter  default.  Diskon  default  10%, pajak default 11%.</li>
        <li><b>SourceCode:</b> 
            <pre style="background: #f4f4f4; padding: 10px; border-radius: 5px; overflow-x: auto;">
              <code>
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
              </code>
            </pre>
        </li>
      </ul>
    </td>
    <td width="40%">
      <img src="/ALGO2 - Bpk. Yusri Ikhwani, M.Kom/img/KalkulatorHarga.png" alt="Pratinjau_ProgramKalkulatorHarga">
  <a href="https://github.com/rnld-devcode/Praktikum_2510010102_M.RizkyRinaldy/blob/main/ALGO2%20-%20Bpk.%20Yusri%20Ikhwani%2C%20M.Kom/latihan4_3_diskon.py">
        <p><b>Program Kalkulator Harga</b></p>
  </a>
    </td>
  </tr>
  <tr>
    <td width="60%">
      <h3>4.4 Fungsi Rekursif Faktorial (<code>latihan4_4_rekursif.py</code>)</h3>
      <ul>
        <li><b>Struktur Data Dasar</b></li>
        <li><b>Soal: </b> BBuatlah  fungsi  rekursif  untuk  menghitung  faktorial.  Fungsi  rekursif  adalah  fungsi  yang memanggil dirinya sendiri.</li>
        <li><b>SourceCode:</b> 
            <pre style="background: #f4f4f4; padding: 10px; border-radius: 5px; overflow-x: auto;">
              <code>
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
              </code>
            </pre>
        </li>
      </ul>
    </td>
    <td width="40%">
      <img src="/ALGO2 - Bpk. Yusri Ikhwani, M.Kom/img/FungsiRekursif.png" alt="Pratinjau_FungsiRekursif">
  <a href="https://github.com/rnld-devcode/Praktikum_2510010102_M.RizkyRinaldy/blob/main/ALGO2%20-%20Bpk.%20Yusri%20Ikhwani%2C%20M.Kom/latihan4_4_rekursif.py">
        <p><b>Menghitung Fungsi Rekursif</b></p>
  </a>
    </td>
  </tr>
  <tr>
  <td width="60%">
      <h3>4.5 Kalkulator Fungsional (<code>latihan4_5_kalkulator.py</code>)</h3>
      <ul>
        <li><b>Perulangan (Looping)</b></li>
        <li><b>Soal: </b> Buatlah kalkulator yang memanfaatkan beberapa fungsi untuk operasi matematika. Setiap operasi ditangani oleh fungsi terpisah.</li>
        <li><b>SourceCode:</b> 
            <pre style="background: #f4f4f4; padding: 10px; border-radius: 5px; overflow-x: auto;">
    <code>

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
  </code>
            </pre>
        </li>
      </ul>
    </td>
    <td width="40%">
      <img src="/ALGO2 - Bpk. Yusri Ikhwani, M.Kom/img/KalkulatorSederhana.png" alt="Pratinjau_KalkulatorSederhana">
  <a href="https://github.com/rnld-devcode/Praktikum_2510010102_M.RizkyRinaldy/blob/main/ALGO2%20-%20Bpk.%20Yusri%20Ikhwani%2C%20M.Kom/latihan4_5_kalkulator.py">
        <p><b>Kalkulator Sederhana.</b></p>
  </a>
    </td>
  </tr>
</table>

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
