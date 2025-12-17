from django.urls import path
from . import views

urlpatterns = [
    path("periods/", views.PeriodlistCreate.as_view(), name="period-list"),
    path("periods/delete/<int:pk>/", views.PeriodDelete.as_view(), name="delete-period"),
]
