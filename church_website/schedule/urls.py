from django.urls import path
from .views import ScheduleListView, ScheduleCreateView, ScheduleDeleteView, ScheduleDetailView, ScheduleUpdateView

app_name = 'schedule'

urlpatterns = [
    path('', ScheduleListView.as_view(), name='schedule'),
    path('create', ScheduleCreateView.as_view(), name='schedule_create'),
    path('<slug:slug>', ScheduleDetailView.as_view(), name='schedule_detail'),
    path('<slug:slug>/update', ScheduleUpdateView.as_view(), name='schedule_update'),
    path('<slug:slug>/delete', ScheduleDeleteView.as_view(), name='schedule_delete')
]
