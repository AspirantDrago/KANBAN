from datetime import date

from flask_admin.contrib.sqla import ModelView, typefmt
from markupsafe import Markup


def datetime_format(view, value):
    return value.strftime('%H:%M:%S %d.%m.%Y')


class CustomView(ModelView):
    can_view_details = True
    create_modal = True
    edit_modal = True
    can_export = True
    can_set_page_size = True
    column_display_all_relations = True

    MY_DEFAULT_FORMATTERS = dict(typefmt.BASE_FORMATTERS)
    MY_DEFAULT_FORMATTERS.update({
        date: datetime_format
    })
    column_type_formatters = MY_DEFAULT_FORMATTERS

    def link_formatter(cls, context, model, name):
        # `self` is current administrative view
        # `context` is instance of jinja2.runtime.Context
        # `model` is model instance
        # `name` is property name
        return Markup(f'<a href="{getattr(model, name)}">{getattr(model, name)}</a>')

    def link_blank_formatter(cls, context, model, name):
        return Markup(f'<a href="{getattr(model, name)}" target="_blank"><i class="bi bi-box-arrow-up-right"></i> {getattr(model, name)}</a>')

    def link_tel_formatter(cls, context, model, name):
        return Markup(f'<a href="tel:{getattr(model, name)}"><i class="bi bi-telephone-fill"></i> {getattr(model, name)}</a>')

    def link_mail_formatter(cls, context, model, name):
        return Markup(f'<a href="mailto:{getattr(model, name)}"><i class="bi bi-envelope-fill"></i> {getattr(model, name)}</a>')
