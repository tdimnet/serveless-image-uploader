import requests
import base64
import json
import os


BASE_URL = 'https://jd42y35twj.execute-api.us-east-1.amazonaws.com/prod'
FILE_PATH = './scripts/assets'
FILES = os.listdir(FILE_PATH)


def upload_image(base64_file, file_name):
    data = {
        'name': file_name,
        'file': base64_file
    }

    upload_requests = requests.post(
        '{}/images'.format(BASE_URL),
        data=json.dumps(data)
    )

    print(upload_requests.json())


def main():
    for file in FILES:
        image = open('{}/{}'.format(FILE_PATH, file), 'rb')

        image_read = image.read()
        image_64_encode = base64.encodebytes(image_read)
        encode_to_uft8 = str(image_64_encode, 'utf-8')

        upload_image(encode_to_uft8, file)


if __name__ == '__main__':
    main()

