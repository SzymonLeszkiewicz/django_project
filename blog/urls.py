from django.urls import path
from . import views #kropka oznacz nasz katalog ?

urlpatterns = [
    path('', views.home, name='blog-home'),
    path('about/', views.about, name='blog-about'),
    path('kontakt/', views.kontakt, name='blog-kontakt')
]
