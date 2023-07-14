from django.urls import path
from blog.views import post_list, categories_list, post_detail

urlpatterns = [
    path('list/', post_list),
    path('detail/<str:post_title>', post_detail),
    path('categories/', categories_list),
    path('archive/<int:year>', post_list),
    path('archive/<int:year>/<int:month>', post_list),

]