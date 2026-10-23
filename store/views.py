from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404

from carts.models import CartItem
from category.models import Category
from store.models import Product
from carts.views import _cart_id
from django.core.paginator import EmptyPage,PageNotAnInteger,Paginator


def store(request, category_slug=None):
    if category_slug is not None:
        category = get_object_or_404(Category, slug=category_slug)
        products = Product.objects.filter(category=category, is_available=True)
        paginator = Paginator(products, 4)
        page = request.GET.get('page')
        page_products = paginator.get_page(page)
    else:
        products = Product.objects.filter(is_available=True)
        paginator = Paginator(products, 4)
        page = request.GET.get('page')
        page_products = paginator.get_page(page)

    product_count = products.count()



    context = {
        'products': page_products,
        'product_count': product_count,

    }
    return render(request, 'store/store.html', context)



def product_detail(request, category_slug, product_slug):
    try:
        single_product = Product.objects.get(category__slug=category_slug, slug=product_slug)
        in_cart =CartItem.objects.filter(cart__cart_id=_cart_id(request), product=single_product).exists()


    except Exception as e:
        raise e
    context = {
        'single_product': single_product,
        'in_cart': in_cart,
        
    }
    return render(request, 'store/product_detail.html', context)