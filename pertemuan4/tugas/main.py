from kurs import kurs
from konverter import konversi
from tabulate import tabulate

print("=== KONVERTER MATA UANG ===")

tabel = [[k, v] for k, v in kurs.items()]
print(tabulate(tabel, headers = ["Kode", "Kurs"], tablefmt = "grid"))
print("\n")

dari = input("Dari (IDR/USD/EUR/SGD/JPY): ")
ke = input("Ke (IDR/USD/EUR/SGD/JPY): ")
jumlah = float(input("Jumlah: "))

hasil = konversi(jumlah, dari, ke)
print("\n")

print(f"Rp {jumlah:,.0f}".replace(",", ".") + f" = {hasil:.2f} {ke}")