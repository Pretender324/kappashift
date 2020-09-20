from django.urls import path, include
from .views import CompetitionCreate, timetableupdatefunc, timetablesuggest

app_name = 'shift'
urlpatterns = [
    path('competition/', CompetitionCreate.as_view(), name='competition'),
    path('timetable/<int:pk>', timetableupdatefunc, name='timetable'),
    path('timetable/<int:pk>/suggest', timetablesuggest, name='suggest')
]
