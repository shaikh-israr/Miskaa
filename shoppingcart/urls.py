from django.urls import path, re_path
from . import views

urlpatterns = [
    re_path(r'^api/shoppingcart$', views.products_list),
    re_path(r'^api/shoppingcart/(?P<pk>[0-9]+)$', views.products_detail),
    re_path(r'^api/shoppingcart/published$', views.products_list_published)
]
