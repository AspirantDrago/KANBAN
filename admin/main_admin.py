from flask import Flask, redirect
from flask_admin import Admin, AdminIndexView, expose
from flask_sqlalchemy import SQLAlchemy

from admin import config_admin
from admin.view_models.container_view import ContainerView
from admin.view_models.product_view import ProductView
from admin.view_models.provider_view import ProviderView
from admin.view_models.supply_card_view import SupplyCardView
from admin.view_models.warehouse_view import WarehouseView
from models.card import SupplyCard
from models.container import Container
from models.product import Product
from models.provider import Provider
from models.warehouse import Warehouse

models = {
    Provider: ProviderView,
    Product: ProductView,
    Warehouse: WarehouseView,
    Container: ContainerView,
    SupplyCard: SupplyCardView,
}


class IndexView(AdminIndexView):
    def is_visible(self) -> bool:
        return False

    @expose('/')
    def index(self):
        return redirect('/admin/supplycard')


def setup_admin(
        app: Flask,
        db: SQLAlchemy,
) -> Admin:
    admin = Admin(
        app,
        name=config_admin.APPLICATION_NAME,
        template_mode=config_admin.ADMIN_TEMPLATE_MODE,
        index_view=IndexView(),
    )
    app.config['FLASK_ADMIN_SWATCH'] = config_admin.FLASK_ADMIN_SWATCH
    for model, View in models.items():
        admin.add_view(View(model, db.session, name=getattr(View, 'name', None)))
    return admin
