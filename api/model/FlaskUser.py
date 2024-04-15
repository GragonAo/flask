from peewee import AutoField, CharField, Model

from initialize import db


class FlaskUser(Model):
    id = AutoField(primary_key=True)
    name = CharField(max_length=255)

    class Meta:
        database = db.conn
        table_name = 'flask_user'