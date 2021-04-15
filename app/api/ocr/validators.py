from wtforms import Form, FileField, StringField
from libs.validators import BaseForm

from flask_wtf.file import FileRequired, FileAllowed


class OcrLetterForm(BaseForm):

    image = FileField(validators=[FileRequired(), FileAllowed(['jpg', 'png'])])
