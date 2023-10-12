from django.urls import path, include
from .views import IndexView, VisitView

urlpatterns = [
    path('<phone>', IndexView.as_view()),
    path('<phone>/<int:pk>/<latitude>/<longtitude>', VisitView.as_view()),
]