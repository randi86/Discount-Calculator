import tkinter as tk
from tkinter import messagebox

#-GUI-
root = tk.Tk()
root.title("Discount Calculator")
root.geometry("450x300")

#-Label Harga-
label_harga = tk.Label(root, text="Original Price:")
label_harga.pack()

#-Input Harga-
harga = tk.Entry(root)
harga.pack()

#-Label Diskon-
label_diskon = tk.Label(root, text="Discount (%):")
label_diskon.pack()

#-Input Diskon-
diskon = tk.Entry(root)
diskon.pack()

#-Fungsi Hitung-
def hitung_diskon():
    try:
        dataHarga = float(harga.get())
        dataDiskon = float(diskon.get())

        harga_akhir = dataHarga - (dataHarga * dataDiskon / 100)

        label_hasil.config(text=f"Final Price: Rp. {harga_akhir:.2f}")

    except ValueError:
        messagebox.showerror("Error", "Please enter valid numbers")

#-Tombol Hitung-
tombol_hitung = tk.Button(root, text="Calculate", command=hitung_diskon)
tombol_hitung.pack(pady=10)

#-Hasil Hitung-
label_hasil = tk.Label(root, text="Final Price: Rp. 0.00")
label_hasil.pack()

root.mainloop()
