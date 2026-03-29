from django.urls import path
from . import views

urlpatterns = [
    path('', views.category_index, name='category_index'),
    path('results/', views.product_list, name='product_list'), # Fallback for search/filter results
    path('category/<slug:slug>/', views.category_detail, name='category_detail'),
    path('<slug:slug>/', views.product_detail, name='product_detail'),
]
