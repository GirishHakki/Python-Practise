# import qrcode as qr
# img = qr.make("https://wa.me/7406429003")
# img.save("Girish_Hakki.png")      # this Girish.Hakki.png is saved in project files




# another method

import qrcode
from PIL import Image

qr = qrcode.QRCode(version=1,
                   error_correction=qrcode.constants.ERROR_CORRECT_H,
                   box_size=10,border=5,)
qr.add_data("https://wa.me/7406429003")
qr.make(fit=True)
img=qr.make_image(fill_color="blue", back_color="black")
img.save("Girish.png")