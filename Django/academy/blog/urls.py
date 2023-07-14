from django.urls import path
from views import test

urlpatterns = [
    path('list/', test),
    path('detail/hello-world', test),
    path('categories/list/', test),

]