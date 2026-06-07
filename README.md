# 📚 Repositori Praktikum

Repositori ini merupakan kumpulan latihan praktikumh berbasis bahasa pemrograman, **Python**, **Pascal**, dll (seperti Algoritma Pemrograman dan Sistem Perancangan Basis Data). Semua kode di dalam repositori ini dibuat untuk memenuhi tugas akademik di program studi Informatika.

---

## 📝 Identitas Mahasiswa
* **Nama** : M. Rizky Rinaldy
* **NPM** : 2510010102
* **Program Studi** : Teknik Informatika
---

## 🗂️ Daftar Tugas

Di bawah ini adalah daftar program yang telah digabungkan ke dalam repositori ini:

<table>
  <tr>
    <td width="60%">
      <h3>1.1 Program Penentu Kelulusan 
([latihan1_1_kelulusan.py](/ALGO2%20-%20Bpk.%20Yusri%20Ikhwani,%20M.Kom/latihan1_1_kelulusan.py))</h3>
      <ul>
        <li><b>Praktikum:</b> ALGO2</li>
        <li><b>Materi:</b> Percabangan (Selection) menggunakan <code>if-elif-else</code> dan Operator relasi yang sering digunakan: == (sama dengan), != (tidak sama), > (lebih besar), < (lebih kecil),  >=  (lebih  besar  sama  dengan),  <=  (lebih  kecil  sama  dengan).  Sedangkan  operator  logika meliputi and, or, dan not. .</li>
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
      <p><b>Program Pengecekan Kelulusan.</b></p>
    </td>
  </tr>
  <tr>
    <td width="60%">
      <h3>1.2 Program Konversi Nilai ke Huruf (<code>latihan1_2_nilaihuruf.py</code>)</h3>
      <ul>
        <li><b>Praktikum:</b> ALGO2</li>
        <li><b>Materi:</b> Percabangan (Selection) menggunakan <code>if-elif-else</code> dan Operator relasi yang sering digunakan: == (sama dengan), != (tidak sama), > (lebih besar), < (lebih kecil),  >=  (lebih  besar  sama  dengan),  <=  (lebih  kecil  sama  dengan).  Sedangkan  operator  logika meliputi and, or, dan not. .</li>
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
      <p><b>Program Konversi Nilai ke Huruf.</b></p>
    </td>
  </tr>
  <tr>
    <td width="60%">
      <h3>1.3 Kalkulator BMI (<code>latihan1_3_bmi.py</code>)</h3>
      <ul>
        <li><b>Praktikum:</b> ALGO2</li>
        <li><b>Materi:</b> Percabangan (Selection) menggunakan <code>if-elif-else</code> dan Operator relasi yang sering digunakan: == (sama dengan), != (tidak sama), > (lebih besar), < (lebih kecil),  >=  (lebih  besar  sama  dengan),  <=  (lebih  kecil  sama  dengan).  Sedangkan  operator  logika meliputi and, or, dan not. .</li>
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
      <p><b>Program Kalkulator BMI.</b></p>
    </td>
  </tr>
  <tr>
    <td width="60%">
      <h3>1.4 Program Loket Tiket Bioskop (<code>latihan1_4_tiket.py</code>)</h3>
      <ul>
        <li><b>Praktikum:</b> ALGO2</li>
        <li><b>Materi:</b> Percabangan (Selection) menggunakan <code>if-elif-else</code> dan Operator relasi yang sering digunakan: == (sama dengan), != (tidak sama), > (lebih besar), < (lebih kecil),  >=  (lebih  besar  sama  dengan),  <=  (lebih  kecil  sama  dengan).  Sedangkan  operator  logika meliputi and, or, dan not. .</li>
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
      <p><b>Program Loket Tiket Bioskop.</b></p>
    </td>
  </tr>
  <tr>
  <td width="60%">
      <h3>1.5 Program Penentu Jenis Segitiga (<code>latihan1_5_segitiga.py</code>)</h3>
      <ul>
        <li><b>Praktikum:</b> ALGO2</li>
        <li><b>Materi:</b> Percabangan (Selection) menggunakan <code>if-elif-else</code> dan Operator relasi yang sering digunakan: == (sama dengan), != (tidak sama), > (lebih besar), < (lebih kecil),  >=  (lebih  besar  sama  dengan),  <=  (lebih  kecil  sama  dengan).  Sedangkan  operator  logika meliputi and, or, dan not. .</li>
        <li><b>SourceCode:</b> 
            <pre style="background: #f4f4f4; padding: 10px; border-radius: 5px; overflow-x: auto;">
              <code>
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
              </code>
            </pre>
        </li>
      </ul>
    </td>
    <td width="40%">
      <img src="/ALGO2 - Bpk. Yusri Ikhwani, M.Kom/img/PenentuJenisSegitiga.png" alt="Pratinjau_PenentuJenisSegitiga">
      <p><b>Program Penentu Jenis Segitiga.</b></p>
    </td>
  </tr>
</table>

---

## 💻 Prasyarat & Lingkungan Pengembangan

Untuk mengompilasi dan menjalankan program-program di atas, Anda memerlukan:
* **Python Interpreter** Download: Kunjungi situs resmi <link>python.org</link>.
* Rekomendasi IDE/Text Editor: **VS Code (Visual Studio Code)**, **PyCharm**, atau **IDLE:** IDE bawaan yang langsung terinstal saat Anda menginstal Python. .

---

## 🚀 Cara Menjalankan Program lewat Terminal

Pilih salah satu file tugas yang ingin dijalankan, kemudian ikuti langkah-langkah berikut melalui Terminal atau Command Prompt:

1. **Akses File Hasil Download Lewat Terminal:**
   ```bash
    cd C:\Users\rizky\Downloads\
   ```
   Note : rizky --> ganti ke nama user sesuai profile di komputer Anda
   
2. **Jalankan file:**
   ```bash
   start namafile.py
   ```
   contoh menjalankan file latihan1_1_kelulusan.py
   ```bash
   start latihan1_1_kelulusan.py
   ```
<div align="center">
  <img src="/ALGO2 - Bpk. Yusri Ikhwani, M.Kom/img/JalankanFilePython.png" width="600" style="border-radius: 16px; box-shadow: 0 4px 8px rgba(0,0,0,0.2);">
  <p><b>Gambar:</b> Visual Langkah Menjalankan Program.</p>
</div>
