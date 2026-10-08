"""Kebutuhan
1.IMPORT datetime
2.wadah list
3. fungsi validasi input nomminal
- while
-try except return
4.Input Tanggal dengan lib datetime 
5.tambah transaksi
6.cek pengeluaran
"""

"""DIAGRAM ALIR ADA DI MAIN()
if pilihan 1 = tambah transaksi
cek pengeluaran
"""


from datetime import datetime
import json

DATA_FILE = "data_transaksi.json"

def muat_data():
    try:
        with open(DATA_FILE, "r") as f:
            return json.load(f)
    except (FileNotFoundError, json.JSONDecodeError):
        return []   

def simpan_data():
     with open(DATA_FILE, "w") as f:
         json.dump(daftar_transaksi, f, indent=4 )   

daftar_transaksi = muat_data()

def format_rupiah(nominal):
    return f"Rp {nominal:,.2f}".replace(",", ".")

def input_nominal(prompt):
    while True:
        try:
            nominal = float(input(prompt))
            if nominal <= 0:
                print("Nominal harus lebih besar dari 0")
                continue
            return nominal
        except ValueError:
            print("Input tidak valid! Harap masukan nominal yang valid")
            
#    Input Tanggal Pemasukan/Pengeluaran
def input_tanggal():
    #Input tanggal otomais(Real time) dengan library datetime
    hari_ini = datetime.now().strftime("%d-%m-%Y")
    tanggal = input(f"Tanggal (DD-MM-YYY) [Enter : {hari_ini}]  ").strip()
    return hari_ini if not tanggal else tanggal

#Fungsi untuk menaambah transaksi
def tambah_transaksi():
    print("\n" + "=" * 45)
    print(" INPUT TRANSAKSI BARU ")
    print("=" *45)
    print("1. Pemasukan(+)")
    print("2. Pengeluaran(-)")
    print("3. Kembali ke Menu Utama")
    
    pilihan = input("Pilih jenis transaksi 1/2/3: ").strip()
    if pilihan == "1":
        tipe = "Pemasukan"
    elif pilihan == "2":
        tipe = "Pengeluaran"
    elif pilihan == "3":
        return
    else:
        print("Pilihan tidak valid")
        return
    
    #Input keterangan, Nominal & Tanggal
    keterangan_input = input("Masukan keterangan transaksi: ").strip()
    if not keterangan_input:
        keterangan_input = "Tanpa Keterangan"
    #Input dengan memanggil fungsi saldo dan tanggal    
    saldo = input_nominal(f"Masukan nominal {tipe.lower()} (Rp): ")
    tanggal = input_tanggal()
    
    #Menyimmpan list ke dalam benntuk dictionary
    transaksi = {
    "tipe": tipe,
    "keterangan": keterangan_input,
    "saldo": saldo,
    "tanggal": tanggal
    }
    
    daftar_transaksi.append(transaksi)
    simpan_data()
    print(f"\nBerhasil mencatat {tipe.lower()} sebesar {format_rupiah(saldo)}!")

def cek_pengeluaran():
    # fitur untuk menampilkan total pengeluaran dan rincian riwayat pengeluaran
    print("\n" + "=" * 60)
    print(" LAPORAN & PENGECEKAN TRANSAKSI ")
    print("=" * 60)
    
    
    #Menghitung total pengeluaran dan pemasukan dengan "saldo"
    total_pengeluaran = sum(t["saldo"] for t in daftar_transaksi if t["tipe"] == "Pengeluaran")
    total_pemasukan = sum(t["saldo"] for t in daftar_transaksi if t["tipe"] == "Pemasukan")
    saldo_tersisa = total_pemasukan - total_pengeluaran
    
    # Ringkasan saldo
    print(f"Total Pemasukan : {format_rupiah(total_pemasukan)}")
    print(f"Total Pengeluaran : {format_rupiah(total_pengeluaran)}")
    print(f"Sisa Saldo : {format_rupiah(saldo_tersisa)}")
    print("=" * 60)
    
    #Filter data khusus pengeluaran
    riwayat_pengeluaran = [t for t in daftar_transaksi if t["tipe"] == "Pengeluaran"]
    
    print("\n --- DAFTAR DETAIL PENGELUARAN ---")
    if not riwayat_pengeluaran:
        print("(Belum ada catatan pengeluaran)")
    else:
        #Tabel Sederhana
        print(f"{'No':<4} | {'Tanggal':<12} | {'Keterangan':<22} | {'Nominal'}")
        print("-" * 60)
        for i, item in enumerate(riwayat_pengeluaran, 1 ):
            print(f"{i:<4} | {item['tanggal']:<12} | {item['keterangan']:<22} | {format_rupiah(item['saldo'])}")
        
        
# Display
def main():
    while True:
        print("\n" + "=" * 45)
        print("Money Tracker Sederhana")
        print("=" * 45)
        print("1. Masukan transaksi (Pemasukan/Pengeluaran)")
        print("2. Cek pengeluaran & Ringkasan saldo")
        print("3. Keluar dari Aplikasi")
        print("=" * 45)
        
        pilihan = input("Pilih menu (1/2/3): ").strip()
        if pilihan == "1":
            tambah_transaksi()
        elif pilihan == "2":
            cek_pengeluaran()
        elif pilihan == "3":
            print("\n Terimakasih telah menggunakan aplikkasi kami!")
            break
        else:
            print("pilihan tidak valid!")

# Entry Point
if __name__ == "__main__":
    main()
        