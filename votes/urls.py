from django.urls import path
from . import views

urlpatterns = [
    path('', views.welcome, name='welcome'),                       # Home page
    path('survey/<int:poll_id>/', views.survey, name='survey'),    # Show poll to vote
    path('vote/<int:poll_id>/', views.vote, name='vote'),          # Process vote
    path('results/<int:poll_id>/', views.results, name='results'), # Show results
    path('thankyou/', views.thank_you, name='thank_you'),          # Optional thank you page
]
