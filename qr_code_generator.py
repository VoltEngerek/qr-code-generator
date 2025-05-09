# derleme için 'pyinstaller --onefile --windowed --icon=logo.ico mod_installer.py' komudunu kullan mod_installer.py kısmında mod_installeri .py kaynak dosyasının adı yap, logo içinse --icon=logo.ico yerinde logo yazan yeri, logonun ismiyle değiştir.

import qrcode
import tkinter as tk
from tkinter import messagebox
from datetime import datetime
from pathlib import Path

def get_desktop_path():
    onedrive = Path.home() / "OneDrive" / "Desktop"
    normal = Path.home() / "Desktop"
    if onedrive.exists():
        return onedrive
    elif normal.exists():
        return normal
    else:
        raise FileNotFoundError("Masaüstü klasörü bulunamadı.")

def qr_uret():
    link = entry.get().strip()
    if not link:
        messagebox.showerror("Hata", "Lütfen bir link girin.")
        return

    # QR kod oluştur
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_H,
        box_size=10,
        border=4,
    )
    qr.add_data(link)
    qr.make(fit=True)
    img = qr.make_image(fill_color="black", back_color="white")

    # Dosya adı ss.hh.dd.mm.yyyy formatında
    now = datetime.now().strftime("%S.%H.%d.%m.%Y")
    dosya_adi = f"qr_{now}.png"

    # Masaüstüne kaydet
    try:
        masaustu = get_desktop_path()
        dosya_yolu = masaustu / dosya_adi
        img.save(dosya_yolu)
        messagebox.showinfo("Başarılı", f"QR kodu başarıyla masaüstüne kaydedildi:\n{dosya_adi}")
    except Exception as e:
        messagebox.showerror("Hata", f"QR kodu kaydedilirken hata oluştu:\n{e}")

# Arayüz
pencere = tk.Tk()
pencere.title("QR Kod Üretici")
pencere.geometry("600x300")
pencere.configure(bg="#121212")

etiket = tk.Label(pencere, text="Linki buraya yapıştır:", font=("Helvetica", 14), fg="#D4D4D4", bg="#121212")
etiket.pack(pady=20)

entry = tk.Entry(pencere, width=50, font=("Helvetica", 12), fg="#FFFFFF", bg="#1E1E1E", insertbackground="#FFFFFF", relief=tk.FLAT)
entry.pack(pady=10)

buton = tk.Button(
    pencere,
    text="QR Kod Üret",
    command=qr_uret,
    font=("Helvetica", 12),
    fg="#FFFFFF",
    bg="#333333",
    activebackground="#444444",
    activeforeground="#FFFFFF",
    relief=tk.FLAT,
    padx=10,
    pady=5
)
buton.pack(pady=20)

pencere.mainloop()
