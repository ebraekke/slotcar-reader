
import pyzbar.pyzbar as pyzbar
from PIL import Image



# obj.data.decode('UTF-8')  => string of data
def decode(im):
    # Find barcodes and QR codes
    decoded_objects = pyzbar.decode(im)

    # Print results
    for obj in decoded_objects:
        print('Type : ', obj.type)
        print('Data : ', obj.data, '\n')

    return decoded_objects





if __name __ == "main__":
    img = Image.open('tests/resources/qr_frame.png')
    img = Image.open('tests/resources/Capture_barcode.PNG')
    img = Image.open('tests/resources/barcode_cloud_day.png')
    pyzbar.decode(img)


img = Image.open('tests/resources/qr_frame.png')
img = Image.open('tests/resources/Capture_barcode.PNG')
img = Image.open('tests/resources/barcode_cloud_day.png')

img = Image.open('tests/resources/barcode_cloud_day.png')
img = Image.open('tests/resources/testcapture.jpg')
img = Image.open('tests/resources/tensecondscapture.jpg')

img = Image.open('tests/resources/fifteensecondscapture.jpg')

barcodes = pyzbar.decode(img)

barcodes[0].data
