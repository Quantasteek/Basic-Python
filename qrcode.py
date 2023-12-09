import pyqrcode
import png
from pyqrcode import QRCode

s="Zairza is an epic club."
url=pyqrcode.create(s)

url.svg('myqr.svg', scale =8)
url.png('myqr.png', scale =6)
