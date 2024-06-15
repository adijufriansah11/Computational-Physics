import tkinter as tk

class GerakLurusBeraturan:
    def __init__(self, posisi_awal, kecepatan):
        self.posisi_awal = posisi_awal
        self.kecepatan = kecepatan
    
    def hitung_perpindahan(self, waktu):
        return self.posisi_awal + self.kecepatan * waktu

class GerakLurusBerubahBeraturan:
    def __init__(self, posisi_awal, kecepatan_awal, percepatan):
        self.posisi_awal = posisi_awal
        self.kecepatan_awal = kecepatan_awal
        self.percepatan = percepatan
    
    def hitung_perpindahan(self, waktu):
        return self.posisi_awal + self.kecepatan_awal * waktu + 0.5 * self.percepatan * waktu**2

def hitung_perpindahan_glb():
    posisi_awal = float(entry_posisi_awal.get())
    kecepatan = float(entry_kecepatan.get())
    waktu = float(entry_waktu.get())
    
    glb = GerakLurusBeraturan(posisi_awal, kecepatan)
    perpindahan = glb.hitung_perpindahan(waktu)
    
    label_hasil['text'] = "Perpindahan GLB: {:.2f}".format(perpindahan)

def hitung_perpindahan_glbb():
    posisi_awal = float(entry_posisi_awal.get())
    kecepatan_awal = float(entry_kecepatan_awal.get())
    percepatan = float(entry_percepatan.get())
    waktu = float(entry_waktu.get())
    
    glbb = GerakLurusBerubahBeraturan(posisi_awal, kecepatan_awal, percepatan)
    perpindahan = glbb.hitung_perpindahan(waktu)
    
    label_hasil['text'] = "Perpindahan GLBB: {:.2f}".format(perpindahan)

# Membuat GUI
root = tk.Tk()
root.title("Aplikasi Modelus X")

# Label dan Entry untuk GLB
label_posisi_awal = tk.Label(root, text="Posisi Awal (GLB):")
label_posisi_awal.grid(row=0, column=0)
entry_posisi_awal = tk.Entry(root)
entry_posisi_awal.grid(row=0, column=1)

label_kecepatan = tk.Label(root, text="Kecepatan:")
label_kecepatan.grid(row=1, column=0)
entry_kecepatan = tk.Entry(root)
entry_kecepatan.grid(row=1, column=1)

# Label dan Entry untuk GLBB
label_posisi_awal_glbb = tk.Label(root, text="Posisi Awal (GLBB):")
label_posisi_awal_glbb.grid(row=2, column=0)
entry_posisi_awal_glbb = tk.Entry(root)
entry_posisi_awal_glbb.grid(row=2, column=1)

label_kecepatan_awal = tk.Label(root, text="Kecepatan Awal:")
label_kecepatan_awal.grid(row=3, column=0)
entry_kecepatan_awal = tk.Entry(root)
entry_kecepatan_awal.grid(row=3, column=1)

label_percepatan = tk.Label(root, text="Percepatan:")
label_percepatan.grid(row=4, column=0)
entry_percepatan = tk.Entry(root)
entry_percepatan.grid(row=4, column=1)

# Entry untuk waktu
label_waktu = tk.Label(root, text="Waktu:")
label_waktu.grid(row=5, column=0)
entry_waktu = tk.Entry(root)
entry_waktu.grid(row=5, column=1)

# Tombol untuk GLB dan GLBB
button_glb = tk.Button(root, text="Hitung GLB", command=hitung_perpindahan_glb)
button_glb.grid(row=6, column=0)

button_glbb = tk.Button(root, text="Hitung GLBB", command=hitung_perpindahan_glbb)
button_glbb.grid(row=6, column=1)

# Label untuk hasil
label_hasil = tk.Label(root, text="")
label_hasil.grid(row=7, columnspan=2)

root.mainloop()
