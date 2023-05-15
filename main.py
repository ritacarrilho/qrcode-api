from fastapi import FastAPI
from qr_controller import generate_qr

app = FastAPI()

@app.get("/{url}")
async def generate_qr_code(url: str):
    qr_code = generate_qr(url)
    # print(type(qr_code))
    return qr_code