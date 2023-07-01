from pypdf import PdfReader
import os


# TODO оформить в тест, добавить ассерты и использовать универсальный путь


def test_for_pdf():
    path_to_pdf = os.path.join(os.path.dirname(os.path.dirname(__file__)), "resources")
    reader = PdfReader(os.path.join(path_to_pdf, 'docs-pytest-org-en-latest.pdf'))
    number_of_pages = len(reader.pages)
    page = reader.pages[0]
    text = page.extract_text()
    assert number_of_pages == 412
    assert text == "pytest Documentation\nRelease 0.1\nholger krekel, trainer and \
consultant, https://merlinux.eu/\nJul 14, 2022"