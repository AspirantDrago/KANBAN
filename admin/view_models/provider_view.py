from wtforms.validators import Email, URL
from wtforms.fields import EmailField, URLField
from wtforms_alchemy import PhoneNumberField

from admin.view_models.custom_view import CustomView


class ProviderView(CustomView):
    column_list = ('title', 'products', 'address', 'email', 'phone', 'site')
    column_editable_list = ('title', 'description', 'address')
    column_display_all_relations = True

    form_overrides = dict(
        phone=PhoneNumberField,
        email=EmailField,
        site=URLField,
    )
    form_args = dict(
        email=dict(validators=[Email('Некорректный адрес электронной почты')]),
        site=dict(validators=[URL('Некорректный URL')]),
        phone=dict(region='RU')
    )

    column_labels = dict(
        title='Название',
        description='Описание',
        products='Изделия',
        email='E-mail',
        phone='Номер телефона',
        address='Адрес',
        site='Сайт',
    )
    column_searchable_list = ('title', 'description', 'address')
    column_sortable_list = ('title',)
    column_formatters = dict(
        site=CustomView.link_blank_formatter,
        phone=CustomView.link_tel_formatter,
        email=CustomView.link_mail_formatter,
    )
    name = 'Поставщики'
