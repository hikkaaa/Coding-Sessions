from pyzbar.pyzbar import decode
from PIL import Image

def decode_qr():
    img = Image.open(str(input('Enter the QR code pathway: '))) # see tutorial in encoding_qr.py if you don't know how to get it :)
    data = decode(img)
    print(data)

print(decode_qr())

