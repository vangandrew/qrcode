# This script will print out all qr codes into the folder "qrs" without any subfolders

import os
import qrcode

path = "C:\\Users\\trini\\OneDrive\\Desktop\\qr_test\\qrs"


def main():
  with open('urls.txt', 'r') as file:
    urls = file.readlines()

  for url in urls:
    tank_name, url = url.split('=', 1)
    tank_name = tank_name.strip()

    qr = qrcode.QRCode(
      version = 1,
      error_correction = qrcode.constants.ERROR_CORRECT_L,
      box_size = 50,
      border = 4
    )

    qr.add_data(url)
    qr.make()

    img = qr.make_image()

    qr_filename = f"{tank_name}.png"

    img.save(os.path.join(path, qr_filename))

if __name__ == "__main__":
  main()