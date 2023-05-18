from admin.view_models.custom_view import CustomView


class ContainerView(CustomView):
    column_list = ('code', 'title', 'supply_card')
    column_editable_list = ('code', 'title')
    column_display_all_relations = True

    column_labels = dict(
        code='Код контейнера',
        title='Название',
        supply_card='KANBAN-карты поставок',
    )
    column_searchable_list = ('code', 'title')
    column_sortable_list = ('code', 'title')
    name = 'Контейнеры'
