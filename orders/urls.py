from django.urls import path
from . import views

urlpatterns = [
    path('enquiry-cart/', views.enquiry_cart, name='enquiry_cart'),
    path('cart/add/<int:product_id>/', views.add_to_cart, name='add_to_cart'),
    path('cart/remove/<int:product_id>/', views.remove_from_cart, name='remove_from_cart'),
    path('submit-enquiry/', views.submit_enquiry, name='submit_enquiry'),
]
