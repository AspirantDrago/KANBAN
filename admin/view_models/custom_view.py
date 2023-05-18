from flask_admin.contrib.sqla import ModelView


class CustomView(ModelView):
    can_view_details = True
    create_modal = True
    edit_modal = True
    can_export = True
    can_set_page_size = True