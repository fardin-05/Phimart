from django.urls import path
from product import views

urlpatterns = [
    path('',views.ViewProduct.as_view(), name = 'product_list'),
    path('<int:id>/',views.ViewSpecificProduct.as_view(), name = 'product_list'),
]
