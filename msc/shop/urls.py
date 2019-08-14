from . import views
from django.urls import path

urlpatterns = [
    path('', views.index),
    path('about/', views.about),
    path('contact/', views.ContactView),
    path('tracker/', views.tracker),
    path('search/', views.search),
    path('products/<int:myid>', views.productview),
    path('checkout/', views.checkout),
]