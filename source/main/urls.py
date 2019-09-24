from django.contrib import admin
from django.urls import path
from webapp.views import index_view, product_detail_view, product_create_view, product_update_view,product_delete_view, \
    product_search_view, product_by_category_view
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index_view, name='index'),
    path('product/<int:pk>', product_detail_view, name='product_detail'),
    path('product/add', product_create_view, name ='product_create'),
    path('product/update/<int:pk>', product_update_view, name='product_update'),
    path('product/delete/<int:pk>', product_delete_view, name='product_delete'),
    path('search/', product_search_view, name='product_search'),
    path('products/<category>/', product_by_category_view, name='product_category')
]
