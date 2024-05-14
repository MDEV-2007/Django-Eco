from django.urls import path

from .views import product_detail_view,product_view,category_list


urlpatterns = [
    path('', product_view, name='product-list'),
    path('<slug:slug>/', product_detail_view, name='product-detail'),
    path('search/<slug:slug>/', category_list, name='category-list'),
]