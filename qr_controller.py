# Import pyqrcode
import pyqrcode

# Generate QR code
def generate_qr(url: str):
    qr_code = pyqrcode.create(url)
    img = qr_code.png("test.png", scale=8)

    return qr_code