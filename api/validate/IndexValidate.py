from wtforms.fields.simple import StringField
from wtforms.form import Form
from wtforms.validators import DataRequired, Length


class IndexValidate(Form):
    name = StringField('Name',validators=[DataRequired(message="名称为必填项"), Length(max=255, message="名称最长255个字符")])
