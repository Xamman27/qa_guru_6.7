import os.path
import requests
# TODO оформить в тест, добавить ассерты, сохранять и читать из tmp, использовать универсальный путь


def test_download_with_requests():
    tmp_path = os.path.join(os.path.dirname(os.path.dirname(__file__)), "tmp")
    url = 'https://selenium.dev/images/selenium_logo_square_green.png'

    response = requests.get(url)
    with open(os.path.join(tmp_path, 'selenium_logo.png'), 'wb') as file:
        file.write(response.content)

    size = os.path.getsize(os.path.join(tmp_path, 'selenium_logo.png'))
    assert size == 30803
