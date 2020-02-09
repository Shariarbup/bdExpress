from django.urls import path
from . import views
app_name='shop'
urlpatterns=[
    path('',views.product_list,name='product_list'),
    path('s/',views.search,name='search'),
    path('<str:category_slug>',views.product_list,name='product_list_by_category'),
    path('<int:id>/<str:slug>/',views.product_details,name='product_detail'),
]