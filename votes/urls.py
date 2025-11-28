from django.urls import path
from . import views

urlpatterns = [
    path('', views.welcome, name='welcome'),  # Home page
    path('survey/', views.survey, name='survey'),  # Survey page
    path('polls/', views.poll_list, name='poll_list'),  # List of all polls
    path('polls/<int:poll_id>/', views.poll_detail, name='poll_detail'),  # Poll vote page
    path('polls/<int:poll_id>/vote/', views.vote, name='vote'),  # Handle vote submission
    path('polls/<int:poll_id>/results/', views.poll_results, name='poll_results'),  # Poll results
]
