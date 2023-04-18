import os
import qrcode
from PIL import Image

# Defina a entrada de texto ou link que deseja transformar em um QR Code
input_data = "olá voce"

# Verifique se o diretório "qr_codes" existe e crie-o, se necessário
if not os.path.exists("qr_codes"):
    os.makedirs("qr_codes")

# Crie um objeto QR Code
qr = qrcode.QRCode(
    version=None,
    error_correction=qrcode.constants.ERROR_CORRECT_H,
    box_size=10,
    border=4,
)

# Adicione os dados à imagem QR Code
qr.add_data(input_data)
qr.make(fit=True)

# Crie a imagem do QR Code
qr_image = qr.make_image(fill_color="black", back_color="white")

# Salve a imagem em uma pasta com o nome correspondente
file_name = input_data.split("/")[-1] + ".png"
qr_image.save(f"qr_codes/{file_name}")
