def modified_false_position(f, a, b, tol, max_iter):
    """
    Mencari akar fungsi f menggunakan metode regulafasi termodifikasi.

    Args:
        f (function): Fungsi untuk mencari akarnya.
        a (float): Tebakan awal pertama.
        b (float): Tebakan awal kedua.
        tol (float): Toleransi kesalahan.
        max_iter (int): Jumlah iterasi maksimum.

    Returns:
        float: Akar dari fungsi f yang ditemukan.
    """
    for i in range(max_iter):
        c = (a*f(b) - b*f(a)) / (f(b) - f(a))
        if abs(f(c)) < tol:
            return c
        if f(c) * f(a) < 0:
            b = c
        else:
            a = c
    return None

# Contoh penggunaan:
import math

# Definisikan fungsi
def f(x):
    return x**2 - 5*x + 4

# Tebakan awal
a = 2.0
b = 5.0

# Toleransi dan jumlah iterasi maksimum
tol = 1e-5
max_iter = 100

# Panggil fungsi modified_false_position untuk mencari akar
akar = modified_false_position(f, a, b, tol, max_iter)
print("Akar dari f(x) = 0 adalah:", akar)
