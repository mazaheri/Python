from django.http import HttpResponse
from django.shortcuts import render
# from catalogue.models import Product,


# # Create your views here.
# def product_list(request):
#     products = Product.objects.all()
#     context = '<br>'.join([f"{product.title},{product.upc}" for product in products])
#     return HttpResponse(context)
#
# #    products = Product.objects.select_related('category').all()
#



def category_products(request,pk):
    try:
        category = Category.objects.prefetch_related('products').get(id)
    except Category.DoesNotExist:
        return HttpResponse('Category Does not Exist')
    #products = Product.object.filter(category=category)

    products = category.products.all()


    context = '<br>'.join([f"{product.title},{product.upc}" for product in products])
    return HttpResponse(context)