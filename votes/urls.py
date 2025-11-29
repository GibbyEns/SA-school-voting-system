from django.urls import path
from . import views

app_name = 'polls'

urlpatterns = [
    path('vote/<int:poll_id>/', views.vote, name='vote'),
path('survey/<int:poll_id>/', views.survey, name='survey'),
path('results/<int:poll_id>/', views.results, name='results'),
]

