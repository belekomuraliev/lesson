import datetime

from flask import render_template, request, redirect, url_for
from . import app, db
from .models import Purchase, Item, User
from .forms import PurchaseForm, ItemForm, UserForm
from flask_login import login_user, logout_user, login_required


def item_views():
    form = ItemForm()
    if request.method == 'POST':
        new_item = request.form.get('name')
        new_price = request.form.get('price')
        if new_item and new_price:
            new_item = Item(name=new_item, price=new_price)
            db.session.add(new_item)
            db.session.commit()
    items = Item.query.all()
    return render_template('items.html', items=items, form=form)


def purchase_views():
    form = PurchaseForm()
    if request.method == 'POST':
        new_name = request.form.get('name')
        new_age = request.form.get('age')
        new_date = request.form.get('date_purchase')
        new_item_id = request.form.get('item_id')
        new_date_formatted = datetime.datetime.strptime(new_date, '%Y-%m-%d')
        print(new_date)
        print(type(new_date))
        new_purchase = Purchase(name=new_name, age=new_age, item_id=new_item_id, date_purchase=new_date_formatted)
        db.session.add(new_purchase)
        db.session.commit()
    purchases = Purchase.query.all()
    return render_template('purchase.html', purchases=purchases, form=form)


def get_single_item(item_id):
    item = Item.query.filter_by(id=item_id).first()
    return render_template('single_item.html', item=item)


@login_required
def update_single_item(item_id):
    form = ItemForm()
    item = Item.query.filter_by(id=item_id).first()
    if request.method == 'POST':
        name = request.form.get('name')
        price = request.form.get('price')
        item.name = name
        item.price = price
        db.session.commit()
    return render_template('update_single_item.html', form=form, item=item)


def delete_single_item(item_id):
    item = Item.query.filter_by(id=item_id).first()
    db.session.delete(item)
    db.session.commit()
    return f"Товар №{item.id} удален"


def register_view():
    form = UserForm()
    if request.method == 'POST':
        new_username = request.form.get('username')
        new_password = request.form.get('password')
        new_user = User(username=new_username, password=new_password)
        db.session.add(new_user)
        db.session.commit()
        return redirect(url_for('login'))
    return render_template('register.html', form=form)


def login_view():
    form = UserForm()
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')
        user = User.query.filter_by(username=username).first()
        if user and user.check_password(password):
            login_user(user)
            return redirect(url_for('item'))
    return render_template('login.html', form=form)


@login_required
def logout_view():
    logout_user()
    return redirect(url_for('login'))
