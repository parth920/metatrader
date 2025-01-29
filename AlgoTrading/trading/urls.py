from django.urls import path
from . import views




urlpatterns = [
    path('', views.login_view, name='login'),
    path('trading/<int:account_id>/', views.trading_params_view, name='trading_params'),
    path('get_open_orders/', views.get_open_orders, name='get_open_orders'),
    path('get_current_prices/', views.get_current_prices_view, name='get_current_prices'),
    path('verify-pin/', views.verify_pin, name='verify_pin'),
    path('admin_login/', views.admin_login, name='admin_login'),
    

    
    
]