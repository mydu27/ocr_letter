import os
import uuid
import hashlib
import config
import datetime


class FileHandle:

    def __init__(self, path):
        self.file_path = path

    def GetFileMd5(self):
        """计算图片的md5值"""
        with open(self.file_path, 'rb') as f:
            md = hashlib.md5()
            md.update(f.read())
        res = md.hexdigest()
        return res

    def DeleteFile(self):
        if os.path.exists(self.file_path):
            os.remove(self.file_path)


def GetNewPath(file_type):
    """根据uuid生成新的唯一文件名, 并按日期归档"""
    file_directory = config.savePath + datetime.datetime.now().strftime("%Y/%m/%d")
    if not os.path.exists(file_directory):
        os.makedirs(file_directory)
    file_path = file_directory + '/' + uuid.uuid1().hex + f'.{file_type}'
    return file_path


def WriteFile(file_type, content):
    """将request获取到的文件流写入到本地"""
    try:
        save_path = GetNewPath(file_type)
        with open(save_path, "wb") as code:
            code.write(content)
    except Exception as e:
        print(e)
        return None
    else:
        return save_path
