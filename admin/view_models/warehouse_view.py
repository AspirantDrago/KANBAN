from admin.view_models.custom_view import CustomView


class WarehouseView(CustomView):
    column_list = ('code', 'title', 'address', 'supply_cards')
    column_editable_list = ('code', 'title', 'address')
    column_display_all_relations = True

    column_labels = dict(
        code='Код склада',
        title='Название',
        address='Расположение',
        supply_cards='KANBAN-карты поставок на данный склад',
    )
    column_searchable_list = ('code', 'title', 'address')
    column_sortable_list = ('code', 'title', 'address')
    name = 'Склады'
