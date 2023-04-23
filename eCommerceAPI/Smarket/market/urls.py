from django.urls import path
from market import views
from .views import *
#from .views import UserListCreateView, UserRetrieveUpdateDestroyView, CategoryListCreateView, CategoryRetrieveUpdateDestroyView, ProductListCreateView, ProductRetrieveUpdateDestroyView, OrderListCreateView, OrderRetrieveUpdateDestroyView, CheckoutListView, ProductSearch
from rest_framework_simplejwt.views import (TokenObtainPairView,TokenRefreshView)


urlpatterns = [
    path('home/', views.home),
    path('user/<u_id>', views.getUser),
    path('users/', views.getUsers),
    path('new/', views.newUser),
    path('edit/<u_id>', views.editUser),
    path('delete/<u_id>', views.deleteUser)
    
]



"""from django.urls import path
from market import views

urlpatterns = [
    path('home/', views.home),
    path('user/<u_id>', views.getUser),
    path('users/', views.getUsers),
    path('new/', views.newUser),
    path('edit/<u_id>', views.editUser),
    path('delete/<u_id>', views.deleteUser)
    
]
"""