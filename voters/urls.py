from django.urls import path
from . import views

urlpatterns = [
    path('', views.indexpage_view, name='landing_page'),
    path('404/', views.page404_view, name='404'),
    path('login/', views.VoterLogin.as_view(), name='voters_login'),
    path('create-account/', views.signup_view, name='voters_signup'),
    path('voters/profile-page/', views.votersprofile_view, name='voters_profile'),
    path('voter-homepage/', views.homepage_view, name='voters_homepage'),
    path('voters/<str:id>=<str:aspirant_name>/', views.electoralpost_view, name='voters_vie'),
    path('elect-your-leaders/<str:pk>/<str:school>', views.voting_view, name='elect_leaders'),
    path('logout/logged-out', views.LogoutVoter.as_view(), name='logout_voters')
]
