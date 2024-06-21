from django.urls import path, include

from rest_framework.routers import DefaultRouter
from . import views

router = DefaultRouter()
# router.register()
router.register(r'products', views.ProductViewSet, basename='product')


urlpatterns = [
    path('', include(router.urls)),
    path('product/search/', views.ProductSearch.as_view(), name='product_search')
]
