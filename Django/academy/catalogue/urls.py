from django.urls import path
from catalogue.views import  category_products

urlpatterns = [
    # path('product/list/', product_list, name='product-list'),
    path('category/<int:pk>/', category_products, name='product-detail')
]
