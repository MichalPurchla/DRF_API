from django.urls import path
from . import views


urlpatterns = [
    path('', views.ProductListCreateAPIView.as_view()),
    path('<int:pk>/', views.ProductDetailAPIView.as_view()),
    path('second_method/', views.product_alt_view),
    path('second_method/<int:pk>/', views.product_alt_view),
    path('<int:pk>/update/', views.ProductUpdateAPIView.as_view()),
    path('<int:pk>/delete/', views.ProductDeleteAPIView.as_view()),
    # path('list/', views.ProductListAPIView.as_view()),
    # path('<int:pk>', views.product_detail_view),
]