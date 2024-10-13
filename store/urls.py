from django.urls import path
from .views import index, signup, login, orders, logout

urlpatterns = [
    path('', index, name= 'homepage'),
    path('signup', signup, name='signup'),
    path('login/', login, name='login'),
    path('logout/', logout , name='logout'),
    path('orders',orders, name='orders')
]
