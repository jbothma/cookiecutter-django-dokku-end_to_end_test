from django.contrib import admin
from django.urls import include, path

from . import views


urlpatterns = [
    path("", views.Index.as_view(), name="index"),
    path("initial_app", include("end_to_end_test.initial_app.urls"),),
    path("admin/", admin.site.urls),
]
