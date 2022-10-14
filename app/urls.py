from .views import app, item_views, purchase_views, \
    get_single_item, update_single_item, delete_single_item, \
    register_view, login_view, logout_view

app.add_url_rule('/purchase', view_func=purchase_views, methods=['GET', 'POST'], endpoint='purchase')
app.add_url_rule('/item', view_func=item_views, methods=['GET', 'POST'], endpoint='item')
app.add_url_rule('/item/<int:item_id>', view_func=get_single_item, methods=['GET', ], endpoint='single_item')
app.add_url_rule('/item/<int:item_id>/update', view_func=update_single_item, methods=['GET', 'POST'], endpoint='update_single_item')
app.add_url_rule('/item/<int:item_id>/delete', view_func=delete_single_item, methods=['GET', 'POST'], endpoint='delete_single_item')
app.add_url_rule('/register', view_func=register_view, methods=['GET', 'POST'], endpoint='register')
app.add_url_rule('/login', view_func=login_view, methods=['GET', 'POST'], endpoint='login')
app.add_url_rule('/logout', view_func=logout_view, methods=['GET', ], endpoint='logout')