import io
import qrcode
from qrcode.image.styledpil import StyledPilImage
from qrcode.image.styles.moduledrawers.pil import RoundedModuleDrawer
from qrcode.image.styles.colormasks import RadialGradiantColorMask

website_link = input()

# Creates an QR code object and add the website link to be encoded into the QR code
qr = qrcode.QRCode(version=1, error_correction=qrcode.constants.ERROR_CORRECT_H, box_size=10, border=5)
qr.add_data(website_link)
qr.make()

# Prints a text-based (ASCII) version of the QR code to the console
f = io.StringIO()         # Creates a text-based in-memory file (Lives in RAM, not hard drive)
qr.print_ascii(out=f)     # Prints the text-based (ASCII) version of the QR code to f
f.seek(0)                 # Resets file pointer to beginning of the file f
print(f.read())

# Original QR code
img_original = qr.make_image(fill_color='purple', back_color='white')
img_original.save("qr_code.png")

# QR code version 1
img_1 = qr.make_image(image_factory=StyledPilImage, module_drawer=RoundedModuleDrawer())
img_1.save("qrcode_ver1.png")

# QR code version 2
img_2 = qr.make_image(image_factory=StyledPilImage, color_mask=RadialGradiantColorMask())
img_2.save("qrcode_ver2.png")

# QR code version 3
img_3 = qr.make_image(image_factory=StyledPilImage, embedded_image_path="./galaxy.jpg")
img_3.save("qrcode_ver3.png")
