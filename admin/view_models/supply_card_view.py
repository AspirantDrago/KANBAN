from wtforms import BooleanField

from admin.view_models.custom_view import CustomView


class SupplyCardView(CustomView):
    column_list = ('url', 'product', 'count', 'container', 'warehouse_to', 'completed', 'created_datetime', 'completed_datetime')
    column_editable_list = ('count',)
    column_display_all_relations = True

    form_extra_fields = {
        'completed': BooleanField('Завершено'),
    }

    form_excluded_columns = ('created_datetime', 'completed_datetime')

    column_labels = dict(
        url='Карточка',
        product='Изделие',
        count='Количество',
        container='Контейнер',
        warehouse_to='Склад назначения',
        completed='Завершено',
        created_datetime='Время создания',
        completed_datetime='Время завершения',
    )
    column_searchable_list = ('url', 'created_datetime', 'completed_datetime')
    column_sortable_list = ('url', 'created_datetime', 'completed_datetime')
    column_filters = ('product', 'container', 'warehouse_to', 'completed')
    column_formatters = dict(
        url=CustomView.link_formatter,
    )
    name = 'KANBAN-карты поставок'
