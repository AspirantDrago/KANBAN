from admin.view_models.custom_view import CustomView


class SupplyCardView(CustomView):
    column_list = ('code', 'product', 'count', 'container', 'warehouse_to')
    column_editable_list = ('count',)
    column_display_all_relations = True

    column_labels = dict(
        code='Код',
        product='Изделие',
        count='Количество',
        container='Контейнер',
        warehouse_to='Склад назначения',
    )
    # column_searchable_list = ()
    # column_sortable_list = ()
    name = 'KANBAN-карты поставок'
