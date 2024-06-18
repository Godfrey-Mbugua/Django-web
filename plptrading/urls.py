from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

app_name ='plptrading'

urlpatterns = [
    path('',views.home,name='home'),
    path('product_list/',views.product_list,name ='product_list'),
    path('product/<int:pk>/',views.product_detail,name ='product_detail'),
    path('customer_list/',views.customer_list,name ='customer_list'),
    path('customer/<int:id>/',views.customer_detail,name ='customer_detail'),
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)