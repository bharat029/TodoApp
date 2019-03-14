from django.urls import path, re_path
from . import views

app_name = 'schedule'

urlpatterns = [
    path('', views.index, name='index'),
    path('add/', views.ScheduleCreate.as_view(), name='add'),
    path('<int:pk>/update/', views.ScheduleUpdate.as_view(), name='update'),
    path('<int:pk>/delete/', views.ScheduleDelete.as_view(), name='delete')
]