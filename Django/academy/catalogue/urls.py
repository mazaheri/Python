from django.urls import path
from catalogue.views import category_products, product_search, user_profile, product_list

urlpatterns = [
    # path('product/list/', product_list, name='product-list'),
    path('category/<int:pk>/', category_products, name='product-detail'),
    path('product/search/', product_search, name='product-search'),
    path('product/user/',user_profile, name='user-profile'),
    path('product/list/', product_list, name='product-list')

]
