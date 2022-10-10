from django.urls import path
from . import views

urlpatterns = [
    path('login/', views.VoterLogin.as_view(), name='voters_login'),
    path('create-account/', views.signup_view, name='voters_signup'),
    path('voters/profile-page/', views.votersprofile_view, name='voters_profile'),

    path('logout/logged-out', views.LogoutVoter.as_view(), name='voters_logout')
]
