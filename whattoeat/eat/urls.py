from django.urls import path

from . import views

# app_name = 'eat'
urlpatterns = [
    path('', views.index, name='index'),
    # path('eat_result/', views.Eat_resultlView.as_view(), name='eat_result'),
    # path('add_restaurant/', views.Add_restaurantView.as_view(), name='add_restaurant'), # noqash
    # path('view_restaurant/', views.View_restaurantView.as_view(), name='view_restaurant'), # noqash
    path('eat_result/', views.eat_result, name='eat_result'),
    path('add_restaurant/', views.add_restaurant, name='add_restaurant'),
    path('view_restaurant/', views.view_restaurant, name='view_restaurant'),
]
