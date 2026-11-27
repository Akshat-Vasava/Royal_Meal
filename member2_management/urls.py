from django.urls import path
from . import views

urlpatterns = [
    path('login/', views.login_view, name='login'),
    path('menu/', views.menu_manage, name='menu_manage'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('orders/', views.order_list, name='order_list'),
    path('categories/', views.category_manage, name='category_manage'),
    path('settings/', views.restaurant_settings, name='restaurant_settings'),
    path('sales-report/', views.sales_report, name='sales_report'),
    path('menu/food-item-form/', views.food_item_form, name='food_item_form'),
    path('categories/category-form/', views.category_form, name='category_form'),
]