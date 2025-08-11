from django.urls import path
from . import views

app_name = 'terms'

urlpatterns = [
    path('termini-e-condizioni/', views.terms_view, name='terms'),
    path('privacy/', views.privacy_view, name='privacy'),
    path('cookie/', views.cookies_view, name='cookies'),
]
