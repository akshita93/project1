from django.urls import path
from .views import *

urlpatterns = [
    path('ev/', Employee_view.as_view(),name='employee_url'),
    path('ehv/', show_view.as_view(),name='show_url'),
    path('uv/<int:pk>/', update_view.as_view(),name='update_url'),
    path('dv/<int:pk>/', delete_view.as_view(),name='delete_url')
]

