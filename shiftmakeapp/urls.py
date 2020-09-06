from django.urls import path, include
from .views import CompetitionCreate

app_name = 'shift'
urlpatterns = [
    path('competition/', CompetitionCreate.as_view(), name='competition'),
]
