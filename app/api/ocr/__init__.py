from flask import Blueprint
from config import URL_FIX

api = Blueprint('ocr', __name__, url_prefix=f'{URL_FIX}/ocr')
from .view import *
