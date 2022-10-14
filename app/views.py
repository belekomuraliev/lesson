import datetime

from flask import render_template, request
from . import app, db
from .models import Purchase, Item
from .forms import PurchaseForm, ItemForm


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
