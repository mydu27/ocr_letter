import pytesseract
from PIL import Image


def ocr_letters(image_path):
    """识别出图片的字母和数字，过滤只保存字母"""
    res_str = pytesseract.image_to_boxes(Image.open(image_path))
    letters = [
        character for character in res_str.replace('\n', ' ').split(' ')
        if character.isalpha()
    ]
    return letters
