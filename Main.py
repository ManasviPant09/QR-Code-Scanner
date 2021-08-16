import pyqrcode
import png
from pyqrcode import QRCode
url = pyqrcode.create('http://en.wikipedia.org')
url.png('Wikipedia-Url.png',scale = 10)
