from django.shortcuts import redirect
from django.urls import path
from . import views

from rest_framework.schemas import get_schema_view
from rest_framework.documentation import include_docs_urls

urlpatterns = [

    path('', lambda r: redirect('swagger')),

    path('customer/', views.Customer.as_view()),
    path('personnel/', views.Personnel.as_view()),
    path('asset/', views.Asset.as_view()),
    path('fleetrental/', views.FleetRental.as_view()),
    path('trip/', views.Trip.as_view()),


]
