from django.urls import path

from . import views

urlpatterns = [
    path('login/', view=views.loginUser, name='login'),
    path('logout', views.logoutUser, name='logout'),
    path('', view=views.ProfileView, name='profiles'),
    path('profile/<str:pk>', view=views.SingleProfileView, name='profile'),
]
