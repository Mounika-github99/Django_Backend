from django.urls import path
from . import veiws as views
from rest_framework.authtoken import views as drf_views # <-- This correctly aliases the REST Framework views

urlpatterns = [
    path('token/', drf_views.obtain_auth_token, name='api_token_auth'),
    path('products/', views.product_list, name='product-list'),        # GET all products
    path('products/create/', views.product_create, name='product-create'),  # POST
    path('products/update/<int:pk>/', views.product_update, name='product-update'),  # PUT
    path('products/delete/<int:pk>/', views.product_delete, name='product-delete'),  # DELETE
]