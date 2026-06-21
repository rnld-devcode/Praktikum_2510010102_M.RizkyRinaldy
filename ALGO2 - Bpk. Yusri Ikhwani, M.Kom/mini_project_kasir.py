#2510010102 - M. Rizky Rinaldy
import os
from datetime import datetime

# ========== FILE KONFIGURASI ==========
FILE_PRODUK     = "produk.txt"
FILE_RIWAYAT    = "riwayat_transaksi.txt"
FOLDER_STRUK    = "struk"

# ========== TAMBAHAN ==========
LEBAR_MENU = 80
LEBAR_STRUK = 42
LEBAR_PRODUK = 80
LEBAR_RIWAYAT = 80

def cetak_garis_atas(lebar):
    print(f"┌{'─' * (lebar - 2)}┐")

def cetak_garis_tengah(lebar):
    print(f"├{'─' * (lebar - 2)}┤")

def cetak_garis_bawah(lebar):
    print(f"└{'─' * (lebar - 2)}┘")

def format_judul(teks, lebar_maksimal, karakter_pengisi=" "):
    return teks.center(lebar_maksimal, karakter_pengisi)

# ========== UTILITAS ==========
def bersihkan_layar():
    os.system('cls' if os.name == 'nt' else 'clear')

def pastikan_folder():
    if not os.path.exists(FOLDER_STRUK):
        os.makedirs(FOLDER_STRUK)

def format_rupiah(angka):
    return f"Rp {int(angka):,}".replace(",", ".")

def input_angka(prompt, tipe=int):
    while True:
        try:
            return tipe(input(prompt))
        except ValueError:
            print(" ❌ Input harus berupa Angka!")

# ========== MANAJEMEN PRODUK ==========
def muat_produk():
    produk = {}
    if not os.path.exists(FILE_PRODUK):
        return produk
    with open(FILE_PRODUK, "r") as f:
        for baris in f:
            data = baris.strip().split("|")
            if len(data) == 3:
                kode, nama, harga = data
                produk[kode] = {"nama": nama, "harga": int(harga)}
    return produk

def simpan_produk(produk):
    with open(FILE_PRODUK, "w") as f:
        for kode, info in produk.items():
            f.write(f"{kode}|{info['nama']}|{info['harga']}\n")

def tambah_produk(produk):
    bersihkan_layar()
    cetak_garis_atas(LEBAR_MENU)
    judul_sub = format_judul("TAMBAH PRODUK BARU", LEBAR_MENU - 4)
    print(f"│ {judul_sub} │")
    cetak_garis_tengah(LEBAR_MENU)
    print(f"│ {'Silakan masukkan data produk di bawah ini:':^{LEBAR_MENU - 4}} │")
    cetak_garis_tengah(LEBAR_MENU)
    print("│")
    kode = input("│  🔑 Kode produk   : ").upper()[:10]
    
    if kode in produk:
        print("│")
        pesan_gagal = f"❌ Gagal! Kode '{kode}' sudah terdaftar!"
        print(f"│  {pesan_gagal}")
        print("│")
        cetak_garis_bawah(LEBAR_MENU)
        input("\nTekan Enter untuk kembali...")
        return
        
    nama = input("│  📦 Nama Produk   : ")[:25] # Membatasi nama produk maks 25 karakter
    harga = input_angka("│  💵 Harga         : ")
    print("│")
    cetak_garis_tengah(LEBAR_MENU)
    print("│")
    produk[kode] = {"nama": nama, "harga": harga}
    simpan_produk(produk)
    print(f"│  ✔️   Sukses! Produk '{nama}' berhasil ditambahkan.")
    print("│")
    cetak_garis_bawah(LEBAR_MENU)
    
    input("\nTekan Enter untuk kembali ke menu...")

def tampil_produk(produk):
    if len(produk) == 0:
        print("\n(Belum ada produk)")
        return
    cetak_garis_atas(LEBAR_PRODUK)
    print(f"│ {'DAFTAR PRODUK TOKO RIZKY':^{LEBAR_PRODUK - 4}} │")
    cetak_garis_tengah(LEBAR_PRODUK)
    print(f"│ {'KODE':<10} │ {'NAMA PRODUK':<40} │ {'HARGA':>20} │")
    cetak_garis_tengah(LEBAR_PRODUK)
    for kode, info in produk.items():
        nama_produk = info['nama'][:40] 
        print(f"│ {kode:<10} │ {nama_produk:<40} │ {format_rupiah(info['harga']):>20} │")
    cetak_garis_bawah(LEBAR_PRODUK)
    input()

# ========== TRANSAKSI ==========
def transaksi(produk):
    bersihkan_layar()
    if len(produk) == 0:
        print("\n ❌ Tambahkan produk terlebih dahulu!")
        input("\nTekan Enter untuk kembali...")
        return
        
    keranjang = []    
    tampil_produk(produk)
    cetak_garis_atas(LEBAR_PRODUK)
    judul_sub = format_judul("TRANSAKSI BARU TOKO RIZKY", LEBAR_PRODUK - 4)
    print(f"│ {judul_sub} │")
    while True:
        cetak_garis_tengah(LEBAR_PRODUK)
        print(f"│  🔑 Kode produk (X=selesai)\033[55G: ", end="")
        kode = input().upper()
        if kode == "X":
            break
        if kode not in produk:
            print(f"│  ❌ Kode '{kode}' tidak ditemukan\n│")
            continue
        
        print(f"│  📦 Jumlah beli '{produk[kode]['nama']}'\033[55G: ", end="")
        jumlah = input_angka("")
        if jumlah <= 0:
            print("│  ❌ Jumlah harus positif\n│")
            continue

        subtotal = produk[kode]["harga"] * jumlah
        keranjang.append({
            "kode"      : kode,
            "nama"      : produk[kode]["nama"],
            "harga"     : produk[kode]["harga"],
            "jumlah"    : jumlah,
            "subtotal"  : subtotal,
        })
        print("|")
        print(f"│  ✔️   + {jumlah}x {produk[kode]['nama']} ({format_rupiah(subtotal)})")

    if len(keranjang) == 0:
        print("│  ❌ Transaksi dibatalkan - keranjang kosong")
        cetak_garis_bawah(LEBAR_PRODUK)
        input("\nTekan Enter untuk kembali ke menu...")
        return
    
    proses_pembayaran(keranjang)

def proses_pembayaran(keranjang):
    total = sum(item["subtotal"] for item in keranjang)
    print("│")
    cetak_garis_tengah(LEBAR_PRODUK)
    print(f"│ {'RINGKASAN BELANJAAN':^{LEBAR_PRODUK - 4}} │")
    cetak_garis_tengah(LEBAR_PRODUK)
    
    for item in keranjang:
        detail_item = f"• {item['nama']} ({item['jumlah']}x)"
        harga_item = format_rupiah(item['subtotal'])
        print(f"│  {detail_item:<54} {harga_item:>20} │")
        
    cetak_garis_tengah(LEBAR_PRODUK)
    print(f"│  {'TOTAL BELANJA':<54} {format_rupiah(total):>20} │")

    # 5. Hitung Diskon Otomatis di dalam Box
    diskon = 0
    if total >= 500000:
        diskon = total * 0.10
        print(f"│  🎉 Diskon 10% (belanja >500rb)                        -{format_rupiah(diskon):>20} │")
    elif total >= 200000:
        diskon = total * 0.05
        print(f"│  🎉 Diskon 5% (belanja >200rb)                         -{format_rupiah(diskon):>20} │")

    total_bayar = total - diskon
    if diskon > 0:
        cetak_garis_tengah(LEBAR_PRODUK)
        print(f"│  {'TOTAL TAGIHAN NETT':<54} {format_rupiah(total_bayar):>20} │")
        
    cetak_garis_tengah(LEBAR_PRODUK)
    while True:
        try:
            print(f"│  💵       Total tagihan\033[55G: {format_rupiah(total_bayar)}")
            bayar = int(input(f"│           Uang diterima\033[55G: Rp "))
            if bayar < total_bayar:
                print(f"│  ❌       Uang kurang\033[55G {format_rupiah(total_bayar - bayar)}│")
                continue
            break
        except ValueError:
            print(f"│ {' ❌ Masukkan angka yang valid':^{LEBAR_PRODUK - 4}}")

    kembalian = bayar - total_bayar
    
    print("│")
    print(f"│  ✔️      Kembalian\033[55G: {format_rupiah(kembalian)}")
    cetak_garis_bawah(LEBAR_PRODUK)
    
    # Jalankan cetak struk bawaanmu
    cetak_struk(keranjang, total, diskon, total_bayar, bayar, kembalian)

# ========== STRUK ==========
def cetak_struk(keranjang, total, diskon, total_bayar, bayar, kembalian):
    pastikan_folder()
    waktu = datetime.now()
    id_trx = waktu.strftime("%Y%m%d%H%M%S")
    garis = "=" * 42
    baris = []
    baris.append(garis)
    baris.append("           TOKO KELONTONG RIZKY")
    baris.append("     Jl. Ahmad Yani Km.33 Banjarbaru")
    baris.append(garis)
    baris.append(f"No. Transaksi : TRX-{id_trx}")
    baris.append(f"Tanggal       : {waktu.strftime('%d-%m-%Y %H:%M:%S')}")
    baris.append("-" * 42)
    baris.append(f"{'Nama':<20}{'Qty':>5}{'Subtotal':>17}")
    baris.append("-" * 42)
    for item in keranjang:
        nama = item["nama"][:18]
        baris.append(f"{nama:<20}{item['jumlah']:>5}{format_rupiah(item['subtotal']):>17}") 
    baris.append("-" * 42)
    baris.append(f"{'Total':<25}{format_rupiah(total):>17}")
    if diskon > 0:
        baris.append(f"{'Diskon':<25}{'-' + format_rupiah(diskon):>17}")
    baris.append(f"{'Total bayar':<25}{format_rupiah(total_bayar):>17}")
    baris.append(f"{'Tunai':<25}{format_rupiah(bayar):>17}")
    baris.append(f"{'Kembalian':<25}{format_rupiah(kembalian):>17}")
    baris.append(garis)
    baris.append("      Terima kasih atas kunjungan Anda")
    baris.append("         Selamat berbelanja kembali")
    baris.append(garis)

    struk = "\n".join(baris)

    print("\n" + struk)

    nama_struk = f"{FOLDER_STRUK}/struk_{id_trx}.txt"
    with open(nama_struk, "w") as f:
        f.write(struk)
    print(f"\n 📄 Struk tersimpan: {nama_struk}")

    with open(FILE_RIWAYAT, "a") as f:
        f.write(f"{id_trx}|{waktu.strftime('%d-%m-%Y %H:%M')}|{total_bayar}|{len(keranjang)}\n")
    input("\nTekan Enter untuk kembali ke menu...")

# ========== RIWAYAT ==========
def tampil_riwayat():
    if not os.path.exists(FILE_RIWAYAT):
        print("\n(Belum ada transaksi)")
        input("\nTekan Enter untuk kembali...")
        return
    cetak_garis_atas(LEBAR_RIWAYAT)
    print(f"│ {'LAPORAN RIWAYAT TRANSAKSI':^{LEBAR_RIWAYAT - 4}} │")
    cetak_garis_tengah(LEBAR_RIWAYAT)
    print(f"│ {'ID Transaksi':<20} │ {'Tanggal':<22} │ {'Item':>5} │ {'Total':>20} │")
    cetak_garis_tengah(LEBAR_RIWAYAT)
    total_semua = 0
    jumlah_trx  = 0
    with open(FILE_RIWAYAT, "r") as f:
        for baris in f:
            data = baris.strip().split("|")
            if len(data) == 4:
                id_trx, tgl, total, item = data
                id_lengkap = f"TRX-{id_trx}"
                print(f"│ {id_lengkap:<20} │ {tgl:<22} │ {item:>5} │ {format_rupiah(int(float(total))):>20} │")
                total_semua += int(float(total))
                jumlah_trx  += 1
    cetak_garis_tengah(LEBAR_RIWAYAT)
    info_ringkasan = f"Total Transaksi: {jumlah_trx}   │   Total Omset: {format_rupiah(total_semua)}"
    print(f"│ {info_ringkasan:<{LEBAR_RIWAYAT - 4}} │")
    cetak_garis_bawah(LEBAR_RIWAYAT)
    input("\nTekan Enter untuk kembali ke menu...")

# ========== MENU UTAMA ==========
def tampilkan_menu():
    cetak_garis_atas(LEBAR_MENU)
    judul_tengah = format_judul("APLIKASI KASIR - TOKO RIZKY", LEBAR_MENU - 4)
    print(f"│ {judul_tengah} │")
    cetak_garis_tengah(LEBAR_MENU)
    print(f"│  1. {'Tambah Produk':<{LEBAR_MENU - 8}} │")
    print(f"│  2. {'Lihat Daftar Produk':<{LEBAR_MENU - 8}} │")
    print(f"│  3. {'Mulai Transaksi':<{LEBAR_MENU - 8}} │")
    print(f"│  4. {'Lihat Riwayat Transaksi':<{LEBAR_MENU - 8}} │")
    print(f"│  5. {'Keluar':<{LEBAR_MENU - 8}} │")
    cetak_garis_bawah(LEBAR_MENU)

def main():
    produk = muat_produk()

    while True:
        bersihkan_layar()
        tampilkan_menu()
        pilih = input(" ==> Pilihan menu [1-5]: ")

        if   pilih == "1": tambah_produk(produk)
        elif pilih == "2": tampil_produk(produk)
        elif pilih == "3": transaksi(produk)
        elif pilih == "4": tampil_riwayat()
        elif pilih == "5": 
            print("\n ✔️ Terima kasih telah menggunakan aplikasi ini")
            break
        else:
            print(" ❌ Pilihan tidak valid")

if __name__ == "__main__":
    main()