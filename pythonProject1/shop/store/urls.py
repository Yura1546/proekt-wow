from django.urls import path
from . import views
from django.urls import path
from django.contrib.auth import views as auth_views
urlpatterns = [
    path('', views.index, name='index'),  # Головна сторінка
    path('register/', views.register, name='register'),  # Реєстрація
    path('logout/', views.logout_view, name='logout'),  # Вихід
    path('item/<int:item_id>/', views.clothing_item_detail, name='clothing_item_detail'),  # Перегляд товару
    path('cart/', views.view_cart, name='view_cart'),  # Перегляд корзини
    path('add_to_cart/<int:item_id>/', views.add_to_cart, name='add_to_cart'),  # Додавання товару в корзину
    path('checkout/', views.checkout, name='checkout'),
    path('order-success/', views.order_success, name='order_success'),
    path('remove-from-cart/<int:item_id>/', views.remove_from_cart, name='remove_from_cart'),
    path('clothing/', views.clothing_list, name='clothing_list'),
    path('item/<int:item_id>/', views.item_detail, name='item_detail'),
    path('add-to-cart/<int:item_id>/', views.add_to_cart, name='add_to_cart'),
    path('remove-from-cart/<int:item_id>/', views.remove_from_cart, name='remove_from_cart'),
    path('checkout/', views.checkout, name='checkout'),
    path('change-password/', views.change_password, name='change_password'),
    path('filter-by-category/<int:category_id>/', views.filter_clothing_by_category, name='filter_by_category'),
    path('add-to-cart/<int:item_id>/', views.add_to_cart, name='add_to_cart'),
    path('remove-from-cart/<int:item_id>/', views.remove_from_cart, name='remove_from_cart'),
    path('place-order/', views.place_order, name='place_order'),
    path('order-confirmation/<int:order_id>/', views.order_confirmation, name='order_confirmation'),
    path('my-orders/', views.view_orders, name='my_orders'),
    path('my-orders/', views.my_orders, name='my_orders'),
    path('accounts/login/', auth_views.LoginView.as_view(), name='login'),
    path('login/', auth_views.LoginView.as_view(), name='login'),
    path('signup/', views.signup, name='signup'),  # Якщо є сторінка реєстрації
    path('', views.home, name='home'),  # Головна сторінка
    path('signup/', views.signup, name='signup'),
    path('login/', auth_views.LoginView.as_view(), name='login'),
    path('login/', auth_views.LoginView.as_view(), name='login'),
    path('signup/', views.signup, name='signup'),  # Додано шлях для реєстрації
    path('products/', views.product_list, name='product_list'),
    path('', views.clothing_item_list, name='clothing_item_list'),  # Список товарів
    path('item/<int:pk>/', views.clothing_item_detail, name='clothing_item_detail'),  # Деталі конкретного товару
    path('place_order/', views.place_order, name='place_order'),
    path('orders/', views.user_orders, name='user_orders'),  # Це шлях до сторінки замовлень
    path('product/<int:product_id>/', views.product_detail, name='product_detail'),
]
