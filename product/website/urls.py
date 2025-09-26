from django.urls import path, include
from . import views
from django.contrib.auth import views as auth_views
from django.contrib.auth.views import LogoutView
from .views import LogoutNoCsrfView
urlpatterns = [
    # Home → Product List
    path("", views.product_list_page, name="home"),

    # Product Detail
    path("products/<int:pk>/", views.product_detail, name="product_detail"),

    # Cart
    path("cart/", views.cart_view, name="cart"),
    path("cart/add/<int:pk>/", views.add_to_cart, name="add_to_cart"),
    path("cart/remove/<int:pk>/", views.remove_from_cart, name="remove_from_cart"),

    # Authentication
    path("login/", views.login_user, name="login"),
    path('logout/', LogoutNoCsrfView.as_view(next_page='home'), name='logout'),
    path("signup/", views.signup_user, name="signup"),

    # API routes
    path("api/", include("website.api.urls")),
]
