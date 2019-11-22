from django.urls import path

from wc_app3 import views

urlpatterns = [

    path('get_user/', views.get_user),



]