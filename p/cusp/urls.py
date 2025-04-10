from django.urls import path
from . import views


urlpatterns = [
    path("", views.index, name="index"),
    path("get-quotation", views.quote, name="quote"),

]


