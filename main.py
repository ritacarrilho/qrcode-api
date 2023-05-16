from fastapi import FastAPI
from qr_controller import generate_qr
import QRCodeBuilder 

app = FastAPI()

@app.get("/{url}")
async def generate_qr_code(url: str):
    QRCodeBuilder.generate_qr(url)
    qr_code = generate_qr(url)
    # print(type(qr_code))
    return qr_code
