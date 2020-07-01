import pyqrcode
link="ลิงค์เว็บไซต์"
image=pyqrcode.create(link)
image.svg("confirm.svg",scale=8)
