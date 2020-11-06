from .views import RegisterAPI, UserProfileAPI, LoginAPI, UserAPI, ChangePasswordView
from knox import views as knox_views
from django.urls import path, include
from . import views

urlpatterns = [
    path('/logout/', knox_views.LogoutView.as_view(), name='logout'),
    path('/logoutall/', knox_views.LogoutAllView.as_view(), name='logoutall'),
    path('/users/<user_id>/profile/', UserProfileAPI.as_view()),
    # path('<int:id>/edit/', users_edit, name="users_edit"),
    # path('add/', users_add, name="users_add"),
    # path('<int:id>/delete/', users_delete, name="users_delete"),
    path('/register/', RegisterAPI.as_view(), name='register'),
    path('/login/', LoginAPI.as_view(), name='login'),
    path('/user/', UserAPI.as_view(), name='user'),
    path('/change-password/', ChangePasswordView.as_view(), name='change-password'),
    path('/products/', views.products.as_view(), name='products'),
    path('/all-products', views.product_list , name='al-products'),
]