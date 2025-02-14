from django.urls import path
from .views import authlogin, authlogout, customer_login, admin_login, registration, forgetpassword, customer_dashboard,admin_register,admin_dashboard, admin_logout

urlpatterns = [
    path('', authlogin, name='login'),  # Login page at root URL `/`
    path('logout/', authlogout, name='logout'),
    path('customer_login/', customer_login, name='customer_login'),  # `/customer_login/`
    path('admin_login/', admin_login, name='admin_login'),  # `/admin_login/`
    path('admin_register/', admin_register, name='admin_register'),
    path('admin_dashboard/', admin_dashboard, name='admin_dashboard'),
    path('admin_logout/', admin_logout, name='admin_logout'),
    path('registration/', registration, name='registration'),
    path('customer_dashboard/', customer_dashboard, name='customer_dashboard'),
    path('forget-password/', forgetpassword, name='forget_password'),
]
