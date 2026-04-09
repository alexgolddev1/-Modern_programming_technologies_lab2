from django.urls import path

from . import views

urlpatterns = [
    path("", views.home_view, name="home"),
    path("orders/", views.order_list_view, name="order_list"),
    path("orders/new/", views.order_create_view, name="order_create"),
    path("orders/<int:pk>/edit/", views.order_update_view, name="order_update"),
    path("orders/<int:pk>/delete/", views.order_delete_view, name="order_delete"),
]
