from django.urls import path
from . import views

urlpatterns = [
    path('login/', views.user_login_view, name='user_login'),
    path('create-account/', views.voters_signup_view, name='signup'),
    path('create-official-account/', views.officials_signup_view, name='official_signup'),
    path('logged-out', views.LogoutUser.as_view(), name='logout_user')

]