from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import login, authenticate
from .models import Product
from .forms import SignupForm
from django.contrib.auth.views import LogoutView
# Home / Product List

def product_list_page(request):
    products = Product.objects.all()
    return render(request, "website/products/product_list.html", {"products": products})

# Product Detail
def product_detail(request, pk):
    product = get_object_or_404(Product, pk=pk)
    return render(request, "website/products/product_detail.html", {"product": product})

# Cart
def cart_view(request):
    cart = request.session.get("cart", {})
    cart_items = []
    total = 0

    for pk, quantity in cart.items():
        product = get_object_or_404(Product, pk=pk)
        subtotal = product.price * quantity
        cart_items.append({
            "product": product,
            "quantity": quantity,
            "subtotal": subtotal,
        })
        total += subtotal

    return render(request, "website/products/cart.html", {
        "cart_items": cart_items,
        "total": total,
    })

def add_to_cart(request, pk):
    cart = request.session.get("cart", {})
    if str(pk) in cart:
        cart[str(pk)] += 1
    else:
        cart[str(pk)] = 1
    request.session["cart"] = cart
    return redirect("cart")

def remove_from_cart(request, pk):
    cart = request.session.get("cart", {})
    if str(pk) in cart:
        del cart[str(pk)]
        request.session["cart"] = cart
    return redirect("cart")

def signup_user(request):
    if request.method == "POST":
        form = SignupForm(request.POST)
        if form.is_valid():
            user = form.save()  # Password is hashed automatically
            login(request, user)  # Log the user in immediately
            return redirect("home")  # Redirect to product list
    else:
        form = SignupForm()
    return render(request, "website/common/signup.html", {"form": form})
class LogoutNoCsrfView(LogoutView):
    # Allow GET requests for logout (not recommended for production)
    http_method_names = ['get', 'post']
# Custom Login View
def login_user(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect("home")  # Redirect to product list
        else:
            error = "Invalid username or password."
            return render(request, "website/common/login.html", {"error": error})
    return render(request, "website/common/login.html")
