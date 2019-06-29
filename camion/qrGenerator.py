import pyqrcode
import gmaps
s = "https://princesanndy.wixsite.com/muevetegdl"
# Generate QR code
url = pyqrcode.create(s)
url.svg("myqr.svg", scale=8)
