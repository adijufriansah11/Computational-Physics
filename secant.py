def secant_akar(f, x0, x1, tol, max_iter):
    """
    Mencari akar fungsi f menggunakan metode Secant.

    Args:
        f (function): Fungsi untuk mencari akarnya.
        x0 (float): Tebakan awal pertama.
        x1 (float): Tebakan awal kedua.
        tol (float): Toleransi kesalahan.
        max_iter (int): Jumlah iterasi maksimum.

    Returns:
        float: Akar dari fungsi f yang ditemukan.
    """
    for i in range(max_iter):
        x_new = x1 - f(x1) * (x1 - x0) / (f(x1) - f(x0))
        if abs(x_new - x1) < tol:
            return x_new
        x0, x1 = x1, x_new
    return None

# Contoh penggunaan:
import math

# Definisikan fungsi
def f(x):
    return x**2 - 5*x + 4

# Tebakan awal
x0 = 2.0
x1 = 5.0

# Toleransi dan jumlah iterasi maksimum
tol = 1e-5
max_iter = 100

# Panggil fungsi secant_akar untuk mencari akar
akar = secant_akar(f, x0, x1, tol, max_iter)
print("Akar dari f(x) = 0 adalah:", akar)
