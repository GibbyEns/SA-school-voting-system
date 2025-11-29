from django.urls import path
from . import views

app_name = 'polls'

urlpatterns = [
    path('', views.welcome, name='welcome'),
    path('survey/<int:poll_id>/', views.survey, name='survey'),
    path('vote/', views.vote, name='vote'),  # <-- fixed
    path('results/<int:poll_id>/', views.results, name='results'),
    path('thankyou/', views.thank_you, name='thank_you'),
]

