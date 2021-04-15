from . import api
from flask import request
from app.api.ocr.validators import OcrLetterForm
from models.ocr import Ocr
from libs.functions import result_format
from app.plugins.public.ocr import ocr_letters
from app.plugins.public.filetools import WriteFile, FileHandle


@api.route('/letters', methods=['POST'])
def get_letters():
    """用户上传图片，识别返回图片中的字母"""
    form_data = OcrLetterForm().validate_()
    ocr_data = {}
    file_content = request.files.get('image').read()
    file_type = form_data.image.data.filename.split('.')[-1]
    save_path = WriteFile(file_type, file_content)
    ocr_data['file_path'] = save_path
    ocr_data['file_md5'] = FileHandle(save_path).GetFileMd5()
    form = Ocr.query.filter(Ocr.file_md5 == ocr_data['file_md5']).first()
    if form:
        FileHandle(save_path).DeleteFile()
        letters = form.result.split(',')
    else:
        letters = ocr_letters(save_path)
        ocr_data['result'] = ','.join(letters)
        Ocr().set_attrs(ocr_data).direct_commit_()
    return result_format(data={'content': letters})
