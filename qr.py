# This script allows you to name the folder before sending each QR code to each.

import os
import qrcode

path = "C:\\Users\\trini\\OneDrive\\Desktop\\qr_test\\qrs"


def main():
  with open('urls.txt', 'r') as file:
    urls = file.readlines()

  for url in urls:
    tank_name, url = url.split('=', 1)
    tank_name = tank_name.strip()

    x = input("Which folder inside of the directory would you like this QR code to go into? ")

    subfolder_path = os.path.join(path, x)

    if os.path.exists(subfolder_path):
      print("Folder already exists, sending it to desired folder")
    else:
      print(f"{x} folder does not exist. Creating folder and sending generated QR Code to it now...")
      os.makedirs(subfolder_path)

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
    qr_path = os.path.join(subfolder_path, qr_filename)

    
    img.save(qr_path)

if __name__ == "__main__":
  main()