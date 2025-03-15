from django.urls import path
from . import views

app_name= 'users'

urlpatterns = [
    path('', views.sign_in, name='signin'),
    path('signup/', views.sign_up, name='signup'),
    path('logout/', views.logout_user, name='logout'),
    
]
