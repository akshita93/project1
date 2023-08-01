from django.urls import path
from .views import *

urlpatterns = [
    path('sign/', Sign_up.as_view(),name='signup_url'),
    path('loginv/', Login_view.as_view(),name='signin_url'),
    path('logout/', Logout_view.as_view(),name='signout_url')
]
