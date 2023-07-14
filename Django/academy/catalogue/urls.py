from django.urls import path
from catalogue.views import test

urlpatterns = [
    path('list/', test)
]