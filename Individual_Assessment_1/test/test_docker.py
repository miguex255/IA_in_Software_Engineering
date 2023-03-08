import os

# Test that check if the file was correctly generated.
def test_file_generated(): 
    assert len(os.listdir('./Individual_Assessment_1/templates/')) == 1

# Test that check if the file was correctly generated.
def test_file_size(): 
    assert os.stat('./Individual_Assessment_1/templates/').st_size > 0

# Test that check if the images were correctly generated.
def test_images(): 
    assert len(os.listdir('./Individual_Assessment_1/static/')) >= 2

def test_check_input_file_extension():
    for file in os.listdir('./Individual_Assessment_1/PDFs/'):
        assert file.endswith('.pdf') == True