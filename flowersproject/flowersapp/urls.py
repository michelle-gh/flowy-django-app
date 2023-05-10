from django.urls import path

from . import views

urlpatterns = [
    path('', views.home, name="home"),
    path("create/", views.create, name="create"),
    path("update/<int:flower_id>", views.update, name="update"),
    path('details/', views.detail, name='detail'),
    path('details/<int:flower_id>/', views.detail, name='detail_with_id'),
    path('get_flowers/', views.get_flowers, name='get_flowers'),

]