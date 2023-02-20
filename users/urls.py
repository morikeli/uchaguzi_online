from django.urls import path
from . import views

urlpatterns = [
    path('', views.indexpage_view, name='landing_page'),
    path('404/', views.page404_view, name='404'),
    path('voters/profile-page/', views.votersprofile_view, name='voters_profile'),
    path('voter-homepage/', views.homepage_view, name='voters_homepage'),
    path('voters/<str:id>/aspirant/profile/<str:aspirant_name>/', views.electoralpost_view, name='voters_vie'),
    path('elect-your-leaders/<str:pk>/<str:school>', views.voting_view, name='elect_leaders'),
    path('polling/<str:pk>/school/polls/<str:school>/', views.polling_view, name='poll'),
    path('poll-results/', views.results_view, name='poll_results'),

    path('official-profile/', views.officials_profile_view, name='official_profile'),
    path('homepage/', views.officials_homepage, name='official_homepage'),
    path('nomination/', views.nominate_aspirants_view, name='nominate_aspirants'),

]
