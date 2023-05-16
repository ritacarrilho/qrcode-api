# Import pyqrcode
import pyqrcode

class QRCodeBuilder:
  # Generate QR code
  def generate_qr(url: str):
    qr_code = pyqrcode.create(url)
    
    # img = qr_code.png("test.png", scale=8)
    qrcode_encoded = encode(qr_code)
    # print in the terminal
    print(qr_code.terminal())
    
    image_as_str = qr_code.png_as_base64_str(scale=5)
    # print code encoded base64
    print(image_as_str)
    
    # binary
    text = qr_code.text()
    print(text)
    
    print(qr_code.show())
    
    '''
    const qrText = new QRCodeText('some value', {
      blackSymbol: '@@',
      whiteSymbol: '..',
    });
    
    const qrCode = qrText.toString();
    console.log(qrCode);
    '''
    
    
    return qrcode_encoded
