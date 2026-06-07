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
      <h3>💵 Program Penentu Kelulusan (<code>latihan1_1_kelulusan.py</code>)</h3>
      <ul>
        <li><b>Praktikum:</b> ALGO2</li>
        <li><b>Materi:</b> Percabangan (Selection) menggunakan <code>if-elif-else</code> dan Operator relasi yang sering digunakan: == (sama dengan), != (tidak sama), > (lebih besar), < (lebih kecil),  >=  (lebih  besar  sama  dengan),  <=  (lebih  kecil  sama  dengan).  Sedangkan  operator  logika meliputi and, or, dan not. .</li>
        <li><b>SourceCode:</b> 
            <pre style="background: #f4f4f4; padding: 10px; border-radius: 5px; overflow-x: auto;">
              <code>
# M. Rizky Rinaldy - 2510010102
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
              </code>
            </pre>
        </li>
      </ul>
    </td>
    <td width="40%">
      <img src="/ALGO2 - Bpk. Yusri Ikhwani, M.Kom/img/ProgramCekKelulusan.png" alt="Pratinjau_ProgramCekKelulusan">
    </td>
  </tr>
</table>

---

## 💻 Prasyarat & Lingkungan Pengembangan

Untuk mengompilasi dan menjalankan program-program di atas, Anda memerlukan:
* **Python Interpreter** Download: Kunjungi situs resmi <link>python.org</link>.
* Rekomendasi IDE/Text Editor: **VS Code (Visual Studio Code)**, **PyCharm**, atau ***IDLE:** IDE bawaan yang langsung terinstal saat Anda menginstal Python. .

---

## 🚀 Cara Menjalankan Program lewat Terminal

Pilih salah satu file tugas yang ingin dijalankan, kemudian ikuti langkah-langkah berikut melalui Terminal atau Command Prompt:

1. **Akses File Hasil Download Lewat Terminal:**
   ```bash
    cd C:\Users\rizky\Downloads\
   ```
   Note : rizky --> ganti ke nama user sesuai profile di komputer Anda
   
2. **Jalankan file executable hasil kompilasi:**
   ```bash
   start  "" "namafile.py"
   ```
<div align="center">
  <img src="img/PratinjauProgram/InstruksiMenjalankanProgram.png" width="600" style="border-radius: 16px; box-shadow: 0 4px 8px rgba(0,0,0,0.2);">
  <p><b>Gambar:</b> Visual Intruksi Menjalankan Program.</p>
</div>
