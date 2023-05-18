from flask import Flask
from flask_admin import Admin
from flask_sqlalchemy import SQLAlchemy

from admin import config_admin

models = {

}


def setup_admin(
        app: Flask,
        db: SQLAlchemy,
) -> Admin:
    admin = Admin(
        app,
        name=config_admin.APPLICATION_NAME,
        template_mode=config_admin.ADMIN_TEMPLATE_MODE
    )
    app.config['FLASK_ADMIN_SWATCH'] = config_admin.FLASK_ADMIN_SWATCH
    for model, View in models.items():
        admin.add_view(View(model, db.session, name=getattr(View, 'name', None)))
    return admin
