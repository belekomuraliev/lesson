from flask_wtf import FlaskForm
from wtforms import SubmitField, StringField, IntegerField, SelectField, DateField, PasswordField

from .models import Item


class ItemForm(FlaskForm):
    name = StringField(label='Название товара')
    price = IntegerField(label='Цена товара')
    submit = SubmitField(label='Сохранить товар')


class PurchaseForm(FlaskForm):
    name = StringField(label='Имя клиента')
    age = IntegerField(label='возраст')
    item_id = SelectField(label='Что купил')
    date_purchase = DateField('Дата')
    submit = SubmitField(label='Сохранить покупку')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        result = []
        for item in Item.query.all():
            result.append((item.id, item.name))
        self.item_id.choices = result


class UserForm(FlaskForm):
    username = StringField(label='Имя пользователя')
    password = PasswordField(label='Пароль')
    submit = SubmitField(label='Сохранить пользователя')