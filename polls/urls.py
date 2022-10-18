from django.urls import path
from . import views

urlpatterns = [
    path('polling/<str:pk>=<str:school>/', views.polling_view, name='poll'),
    path('poll-results/', views.results_view, name='poll_results'),
]