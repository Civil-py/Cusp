from django.urls import path
from . import views
from django.views.generic import TemplateView


urlpatterns = [
    path("", views.index, name="index"),
    path("get-quotation", views.quote, name="quote"),
    path('sitemap.xml', TemplateView.as_view(template_name='cusp/sitemap.xml', content_type='application/xml')),

]


