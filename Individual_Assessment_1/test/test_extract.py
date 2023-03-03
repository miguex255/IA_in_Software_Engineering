from bs4 import BeautifulSoup
import os
from grobit import process_pdf as content


def get_xml(file):
    with open("../PDFs/" + file, 'r', encoding="utf-8") as tei:
        return BeautifulSoup(content(file), 'xml')

# Test that check if the file was correctly generated.
def test_file_generated(): 
    assert len(os.listdir('../PDFs/')) == 1

# Test that check if the images were correctly generated.
def test_images(): 
    assert len(os.listdir('../static/')) > 2
