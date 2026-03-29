from django.urls import path
from . import views

urlpatterns = [
    path('', views.contact, name='contact'), # General contact page
    path('submit/', views.contact, name='contact_submit'), # Submission path
    path('subscribe/', views.subscribe, name='subscribe'), # Newsletter path
]
