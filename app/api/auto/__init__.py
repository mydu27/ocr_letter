from flask import Blueprint
from config import URL_FIX

api = Blueprint('auto', __name__, url_prefix=f'{URL_FIX}/auto')
from .view import *
