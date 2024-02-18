# views.py
from django.shortcuts import render, redirect,get_object_or_404
from .forms import ProductForm
from .models import Product
from django.contrib.auth import authenticate, login
from django.contrib import messages
from django.contrib.auth.forms import AuthenticationForm
from django.shortcuts import render, redirect
from django.contrib.auth import login
from .forms import SignUpForm

from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
from django.shortcuts import redirect

def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('user_login')  # Redirect to your home page or any other desired page
    else:
        form = SignUpForm()
    return render(request, 'registration/signup.html', {'form': form})
# views.py

from django.shortcuts import render, redirect, get_object_or_404
from .models import Product
from .forms import ProductForm

@login_required
def update_product(request, product_id):
    product = get_object_or_404(Product, id=product_id)

    if request.method == 'POST':
        form = ProductForm(request.POST, instance=product)
        if form.is_valid():
            form.save()
            return redirect('product_list')  # Redirect to the product list view after updating
    else:
        form = ProductForm(instance=product)

    return render(request, 'update_product.html', {'form': form, 'product': product})

@login_required
def add_product(request):
    if request.method == 'POST':
        form = ProductForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('product_list')  # Redirect to a view that displays a list of products
    else:
        form = ProductForm()

    return render(request, 'add_product.html', {'form': form})

@login_required
def product_list(request):
    products = Product.objects.all()
    return render(request, 'product_list.html', {'products': products})

@login_required
def delete_product(request, product_id):
    product = get_object_or_404(Product, id=product_id)

    if request.method == 'POST':
        product.delete()
        return redirect('product_list')  # Redirect to a view that displays a list of products

    return render(request, 'delete_product.html', {'product': product})

def user_login(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(request, username=username, password=password)
            if user:
                login(request, user)
                messages.success(request, f'Welcome, {username}!')
                return redirect('product_list') 
            else:
                messages.error(request, 'Invalid username or password.')
        else:
            messages.error(request, 'Invalid username or password.')
    else:
        form = AuthenticationForm()
    return render(request, 'registration/login.html', {'form': form})




def logout_view(request):
    logout(request)
    return redirect('user_login')  

