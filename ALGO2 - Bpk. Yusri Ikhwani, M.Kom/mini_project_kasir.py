#2510010102 - M. Rizky Rinaldy
import os
from datetime import datetime

# ========== TAMBAHAN ==========
def bersihkan_layar():
    os.system('cls' if os.name == 'nt' else 'clear')

# ========== FILE KONFIGURASI ==========
FILE_PRODUK     = "produk.txt"
FILE_RIWAYAT    = "riwayat_transaksi.txt"
FOLDER_STRUK    = "struk"

# ========== UTILITAS ==========
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
    print("\n--- Tambah Produk ---")
    kode = input("Kode produk   : ").upper()
    if kode in produk:
        print(f" ❌ Kode {kode} sudah ada! ")
        return
    nama  = input("Nama Produk   : ")
    harga = input_angka("Harga         : ")
    produk[kode] = {"nama": nama, "harga": harga}
    simpan_produk(produk)
    print(f" ✔️ Produk '{nama}' ditambahkan")
    input("\nTekan Enter untuk kembali ke menu...")

def tampil_produk(produk):
    if len(produk) == 0:
        print("\n(Belum ada produk)")
        return
    print("\n" + "=" * 55)
    print(f"{'KODE':<8}{'NAMA PRODUK':<30}{'HARGA':>15}")
    print("=" * 55)
    for kode, info in produk.items():
        print(f"{kode:<8}{info['nama']:<30}{format_rupiah(info['harga']):>15}")
    print("=" * 55)
    input("\nTekan Enter untuk kembali ke menu...")

# ========== TRANSAKSI ==========
def transaksi(produk):
    bersihkan_layar()
    if len(produk) == 0:
        print("\n ❌ Tambahkan produk terlebih dahulu!")
        return
    keranjang = []
    print("\n========== TRANSAKSI BARU ==========")
    tampil_produk(produk)

    while True:
        kode = input("\nKode produk (X=selesai): ").upper()
        if kode == "X":
            break
        if kode not in produk:
            print(f" ❌ Kode '{kode}' tidak ditemukan")
            continue
        
        jumlah = input_angka(f"Jumlah beli '{produk[kode]['nama']}': ")
        if jumlah <= 0:
            print(" ❌ Jumlah harus positif")
            continue

        subtotal = produk[kode]["harga"] * jumlah
        keranjang.append({
            "kode"      : kode,
            "nama"      : produk[kode]["nama"],
            "harga"     : produk[kode]["harga"],
            "jumlah"    : jumlah,
            "subtotal"  : subtotal,
        })
        print(f" ✔️ + {jumlah}x {produk[kode]['nama']} ({format_rupiah(subtotal)})")

    if len(keranjang) == 0:
        print("\n(Transaksi dibatalkan - keranjang kosong)")
        return
    
    proses_pembayaran(keranjang)

def proses_pembayaran(keranjang):
    total = sum(item["subtotal"] for item in keranjang)
    print("\n--- Ringkasan Belanja ---")
    for item in keranjang:
        print(f"    {item['nama']} ({item['jumlah']}x) = {format_rupiah(item['subtotal'])}")
    print(f"    TOTAL: {format_rupiah(total)}")

    # Diskon otomatis
    diskon = 0
    if total >= 500000:
        diskon = total * 0.10
        print(f" 🎉 Diskon 10% (belanja >500rb): -{format_rupiah(diskon)}")
    elif total >= 200000:
        diskon = total * 0.05
        print(f" 🎉 Diskon 5% (belanja >200rb): -{format_rupiah(diskon)}")

    total_bayar = total - diskon

    while True:
        try:
            bayar = int(input(f"\nTotal tagihan {format_rupiah(total_bayar)}. Uang diterima: Rp "))
            if bayar < total_bayar:
                print(f" ❌ Uang kurang Rp {total_bayar - bayar:,}")
                continue
            break
        except ValueError:
            print(" ❌ Masukkan angka yang valid")

    kembalian = bayar - total_bayar
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
    baris.append("     Jl. Ahmad Yani Km.5 Banjarmasin")
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
        return
    print("\n" + "=" * 65)
    print(f"{'ID Transaksi':<20}{'Tanggal':<22}{'Item':>5}{'Total':>18}")
    print("=" * 65)
    total_semua = 0
    jumlah_trx  = 0
    with open(FILE_RIWAYAT, "r") as f:
        for baris in f:
            data = baris.strip().split("|")
            if len(data) == 4:
                id_trx, tgl, total, item = data
                print(f"TRX-{id_trx:<16}{tgl:<22}{item:>5}{format_rupiah(int(total)):>18}")
                total_semua += int(total)
                jumlah_trx  += 1
    print("=" * 65)
    print(f"Total Transaksi: {jumlah_trx}   |   Total Omset: {format_rupiah(total_semua)}")
    input("\nTekan Enter untuk kembali ke menu...")

# ========== MENU UTAMA ==========
def tampilkan_menu():
    print("\n" + "=" * 45)
    print("     APLIKASI KASIR - TOKO RIZKY")
    print("=" * 45)
    print("1. Tambah Produk")
    print("2. Lihat Daftar Produk")
    print("3. Mulai Transaksi")
    print("4. Lihat Riwayat Transaksi")
    print("5. Keluar")
    print("=" * 45)

def main():
    produk = muat_produk()

    while True:
        bersihkan_layar()
        tampilkan_menu()
        pilih = input("Pilihan menu [1-5]: ")

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