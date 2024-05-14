from django.shortcuts import render,get_object_or_404


from .models import Category,ProductProxy

def product_view(request):
    products = ProductProxy.objects.all()
    return render(request, 'shop/product.html', {'products': products})


def product_detail_view(request, slug):
    product = get_object_or_404(ProductProxy, slug=slug)
    return render(request, 'app/product_detail.html', {'product': product})


def category_list(request, slug):
    category = get_object_or_404(Category, slug=slug)
    products = ProductProxy.objects.select_related('category').filter(category=category)

    return render(request, 'app/category_list.html', {'category': category})