from django.urls import path 
from .views import TestingView,GetStudentView,UpdateStudentView

urlpatterns = [
    path('test/',TestingView.as_view(),name='test'),
    path('students/',GetStudentView.as_view(),name='students'),
    path('students/<int:pk>/', UpdateStudentView. as_view(),name='students')
]