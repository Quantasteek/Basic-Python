from pyzbar.pyzbar import decode
from PIL import Image
decodeQR=decode(Image.open('path of qr code here'))
print(decodeQR[0].data.decode('ascii'))
