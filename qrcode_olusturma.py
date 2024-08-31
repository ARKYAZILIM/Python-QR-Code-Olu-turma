import qrcode

# QR kodu Dönüştürülecek link
data = "https://www.arkyazilim.com"

# QR kodu oluştur
qr = qrcode.QRCode(
    version=1,  # Versiyon: QR kodunun boyutu. 1-40 arasında değişir.
    error_correction=qrcode.constants.ERROR_CORRECT_L,  # Hata düzeltme kapasitesi
    box_size=10,  # QR kodundaki kutuların boyutu
    border=4,  # QR kodunun kenarındaki kutuların sayısı
)

qr.add_data(data)
qr.make(fit=True)

# QR kodunu görüntüye dönüştür
img = qr.make_image(fill_color="black", back_color="white")

# QR kodunu kaydet
img.save("qrcode.png")
