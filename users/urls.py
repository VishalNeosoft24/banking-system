from django.urls import path
from . import views

urlpatterns = [
    path("test", view=views.test_view, name="test_view")
]