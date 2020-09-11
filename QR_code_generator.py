import pyqrcode
import png
url = pyqrcode.create("GOOGLE")
url.png("google.png",scale=8)