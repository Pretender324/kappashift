from django.urls import path, include
from .views import CompetitionCreate, timetableupdatefunc, timetablesuggest, timetableregister, entryfunc, HistoryView, HistoryDetail, shiftcreate


app_name = 'shift'
urlpatterns = [
    path('competition/', CompetitionCreate.as_view(), name='competition'),
    path('timetable/<int:pk>', timetableupdatefunc, name='timetable'),
    path('timetable/<int:pk>/suggest', timetablesuggest, name='suggest'),
    path('timetable/<int:pk>/register', timetableregister, name='register'),
    path('entry/<int:pk>', entryfunc, name="entry"),
    path('history', HistoryView.as_view(), name='history'),
    path('history/<int:pk>', HistoryDetail.as_view(), name='historydetail'),
    path('create/<int:pk>', shiftcreate, name='create')
]
