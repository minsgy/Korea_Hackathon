from django.urls import path
from . import views

urlpatterns = [
    path("create/", views.create_contest, name="contest_create"),
    path("list/", views.display_contest_list, name="contest_list"),
    path("delete/<int:contest_id>/", views.delete_contest, name="contest_delete"),
    path(
        "detail/<int:contest_id>/", views.display_contest_detail, name="contest_detail"
    ),
    path("update/<int:contest_id>/", views.update_contest, name="contest_update"),
    path("confirm/", views.register_in_team, name="confirm"),
    path(
        "register/<int:role_id>/<int:contest_id>",
        views.register_into_team,
        name="register",
    ),
    path("deny/", views.deny, name="deny"),
    path("expulsion/", views.expulsion, name="expulsion"),
]
