# encoding qr code: creating the qr code with python
# decoding qr code: the program returns the data stored in the qr code

import qrcode 


data = ' Live a life you can remember <3 '

qr = qrcode.QRCode(version = 1, box_size=10, border=5)
qr.add_data(data)
qr.make(fit=True)
img = qr.make_image(fill_color = 'pink', back_color = 'white')
img.save('/Users/francesca/Desktop/new/myqr.png')


# tutorial how to get a document pathway on mac: https://setapp.com/how-to/how-to-find-the-path-of-a-file-in-mac#:~:text=Open%20Finder%20on%20your%20Mac,bottom%20of%20the%20Finder%20window.

