from django.contrib import admin
from django.urls import path
from webapp.views import index_view, product_detail_view

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index_view, name='index'),
    path('product/<int:pk>', product_detail_view, name='product_detail')
]
