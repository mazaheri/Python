from django.contrib.auth.decorators import login_required, user_passes_test, permission_required
from django.http import HttpResponse
from django.shortcuts import render
from django.views.decorators.http import require_http_methods, require_GET, require_POST

from catalogue.models import Product
from catalogue.utils import check_is_active, check_is_staff


# from catalogue.models import Product,


# # Create your views here.
# def product_list(request):
#     products = Product.objects.all()
#     context = '<br>'.join([f"{product.title},{product.upc}" for product in products])
#     return HttpResponse(context)
#
# #    products = Product.objects.select_related('category').all()
#

def category_products(request, pk):
    try:
        category = Category.objects.prefetch_related('products').get(id)
    except Category.DoesNotExist:
        return HttpResponse('Category Does not Exist')
    # products = Product.object.filter(category=category)

    products = category.products.all()

    context = '<br>'.join([f"{product.title},{product.upc}" for product in products])
    return HttpResponse(context)


def product_search(request):
    title = request.GET.get('q')

    products = Product.objects.filter(
        is_active=True,
        title__icontains=title,
        title__istartswith=title,

    )
    context = '<br>'.join([f"{product.title},{product.upc}" for product in products])
    return HttpResponse(f"Search page: <br> {context}")


def user_profile(request):
    return HttpResponse(f"Hello {request.user.username}")


def product_list(request):
    context = dict()
    context ['products'] = Product.objects.select_related('category').all()
    return render(request, template_name= 'catalogue/product_list.html', context=context)



