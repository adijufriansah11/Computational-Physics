def bisection_akar(f, a, b, tol, max_iter):
    """
    Mencari akar fungsi f menggunakan metode biseksi.

    Args:
        f (function): Fungsi untuk mencari akarnya.
        a (float): Batas bawah interval pencarian.
        b (float): Batas atas interval pencarian.
        tol (float): Toleransi kesalahan.
        max_iter (int): Jumlah iterasi maksimum.

    Returns:
        float: Akar dari fungsi f yang ditemukan.
    """
    if f(a) * f(b) >= 0:
        print("Tebakan awal tidak valid.")
        return None

    for i in range(max_iter):
        c = (a + b) / 2
        if f(c) == 0 or (b - a) / 2 < tol:
            return c
        if f(c) * f(a) < 0:
            b = c
        else:
            a = c
    return (a + b) / 2

# Contoh penggunaan:
import math

# Definisikan fungsi
def f(x):
    return x**2 - 5*x + 4

# Batas awal interval
a = 3.0
b = 7.0

# Toleransi dan jumlah iterasi maksimum
tol = 1e-5
max_iter = 100

# Panggil fungsi bisection_akar untuk mencari akar
akar = bisection_akar(f, a, b, tol, max_iter)
print("Akar dari f(x) = 0 adalah:", akar)
