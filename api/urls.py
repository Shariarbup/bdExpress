from django.urls import path

from . import views
urlpatterns = [
    path('', views.CategoryAPIView.as_view()),
    path('<int:pk>/', views.CategoryAPIDetailView.as_view()),
    path('new/', views.CategoryAPINewView.as_view()),
    path('product/', views.ProductAPIView.as_view()),
    path('product/<int:pk>/', views.ProductAPIDetailView.as_view()),
    path('product/new/', views.ProductAPINewView.as_view()),

]
