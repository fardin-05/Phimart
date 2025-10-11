from django.urls import path
from product import views

urlpatterns = [
    path('',views.ViewCategory.as_view(), name='category_list'),
    path('<int:pk>/',views.ViewSpecificCategory.as_view(), name='view_spesific_category')
]
