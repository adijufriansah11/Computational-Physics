def newton_raphson_akar(f, f_prime, x0, tol, max_iter):
    """
    Mencari akar fungsi f menggunakan metode Newton-Raphson.

    Args:
        f (function): Fungsi untuk mencari akarnya.
        f_prime (function): Turunan pertama dari fungsi f.
        x0 (float): Tebakan awal.
        tol (float): Toleransi kesalahan.
        max_iter (int): Jumlah iterasi maksimum.

    Returns:
        float: Akar dari fungsi f yang ditemukan.
    """
    x = x0
    for i in range(max_iter):
        x_new = x - f(x) / f_prime(x)
        if abs(x_new - x) < tol:
            return x_new
        x = x_new
    return None

# Contoh penggunaan:
import math

# Definisikan fungsi dan turunannya
def f(x):
    return x**2 - 5*x + 4

def f_prime(x):
    return 2*x - 5

# Tebakan awal
x0 = 3.0

# Toleransi dan jumlah iterasi maksimum
tol = 1e-5
max_iter = 100

# Panggil fungsi newton_raphson_akar untuk mencari akar
akar = newton_raphson_akar(f, f_prime, x0, tol, max_iter)
print("Akar dari f(x) = 0 adalah:", akar)
