import pandas as pd
#Fungsi
def Operasi(Saldo, Pengeluaran):
    Saldo -= Pengeluaran
    print(f"Saldo Anda saat ini adalah Rp.{int(Saldo)}.") 
#input
Saldo = 10000
pengeluaran = int(input("Masukkan pengeluaran Anda: Rp."))
#proses dan output
Operasi(Saldo, pengeluaran)

