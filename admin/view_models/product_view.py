from admin.view_models.custom_view import CustomView


class ProductView(CustomView):
    column_list = ('product_code', 'title', 'description', 'provider', 'supply_cards')
    column_editable_list = ('product_code', 'title', 'description')
    column_display_all_relations = True

    column_labels = dict(
        product_code='Код изделия',
        title='Название',
        description='Описание',
        provider='Поставщик',
        supply_cards='KANBAN-карты поставок',
    )
    column_searchable_list = ('product_code', 'title', 'description')
    column_sortable_list = ('product_code', 'title')
    name = 'Изделия'
