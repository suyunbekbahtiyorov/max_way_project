from django.shortcuts import render, redirect
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required
from .forms import *
from . import services


def login_required_decorator(func):
    return login_required(func, login_url='login_page')


@login_required_decorator
def logout_page(request):
    logout(request)
    return redirect("login_page")


def login_page(request):
    if request.POST:
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, password=password, username=username)
        if user is not None:
            login(request, user)
            return redirect("home_page")

    return render(request, 'dashboard/login.html')


@login_required_decorator
def home_page(request):
    categories = services.get_category()
    products = services.get_product()
    users = services.get_user()
    ctx = {
        'counts': {
            'categories': len(categories),
            'products': len(products),
            'users': len(users),
        }
    }
    return render(request, 'dashboard/index.html', ctx)


@login_required_decorator
def category_create(request):
    model = Category()
    form = CategoryForm(request.POST or None, instance=model)
    if request.POST and form.is_valid():
        form.save()
        return redirect('category_list')
    ctx = {
        "model": model,
        "form": form
    }
    return render(request, 'dashboard/category/form.html', ctx)


@login_required_decorator
def category_edit(request, pk):
    model = Category.objects.get(pk=pk)
    form = CategoryForm(request.POST or None, instance=model)
    if request.POST and form.is_valid():
        form.save()
        return redirect('category_list')
    ctx = {
        "model": model,
        "form": form
    }
    return render(request, 'dashboard/category/form.html', ctx)


@login_required_decorator
def category_delete(request, pk):
    model = Category.objects.get(pk=pk)
    model.delete()
    return redirect('category_list')


@login_required_decorator
def category_list(request):
    categories = services.get_category()
    print(categories)
    ctx = {
        "categories": categories
    }
    return render(request, 'dashboard/category/list.html', ctx)


@login_required_decorator
def product_create(request):
    model = Product()
    form = ProductForm(request.POST, request.FILES, instance=model)
    if request.POST and form.is_valid():
        form.save()
        return redirect('product_list')
    ctx = {
        "model": model,
        "form": form
    }
    return render(request, 'dashboard/product/form.html', ctx)


@login_required_decorator
def product_edit(request, pk):
    model = Product.objects.get(pk=pk)
    form = ProductForm(request.POST or None, instance=model)
    if request.POST and form.is_valid():
        form.save()
        return redirect('product_list')
    ctx = {
        "model": model,
        "form": form
    }
    return render(request, 'dashboard/product/form.html', ctx)


@login_required_decorator
def product_delete(request, pk):
    model = Product.objects.get(pk=pk)
    model.delete()
    return redirect('product_list')


@login_required_decorator
def product_list(request):
    products = services.get_product()
    print(products)
    ctx = {
        "products": products
    }
    return render(request, 'dashboard/product/list.html', ctx)


@login_required_decorator
def user_create(request):
    model = Customer()
    form = UserForm(request.POST or None)
    if request.POST and form.is_valid():
        form.save()
        return redirect('user_list')
    ctx = {
        'model': model,
        'form': form
    }
    return render(request, 'dashboard/user/form.html', ctx)


@login_required_decorator
def user_edit(request, pk):
    model = Customer.objects.get(pk=pk)
    form = UserForm(request.POST, instance=model)
    if request.POST and form.is_valid():
        form.save()
        return redirect('user_list')
    ctx = {
        'model': model,
        'form': form
    }
    return render(request, 'dashboard/user/form.html', ctx)


@login_required_decorator
def user_delete(request, pk):
    model = Customer.objects.get(pk=pk)
    model.delete()
    return redirect("category_list")


@login_required_decorator
def user_list(request):
    users = Customer.objects.all()
    print(users)
    ctx = {
        'users': users
    }
    return render(request, "dashboard/user/list.html", ctx)

@login_required_decorator
def order_list(request):
    orders = Order.objects.all()
    ctx = {
        'orders':orders
    }
    return render(request, "dashboard/order/list.html",ctx)

@login_required_decorator
def orderproduct_list(request,id):
    productorders = services.get_product_by_order(id=id)
    ctx = {
        'productorders': productorders
    }
    return render(request, "dashboard/productorder/list.html", ctx)

@login_required_decorator
def customer_order_list(request,id):
    customer_orders = services.get_order_by_user(id=id)
    ctx = {
        'customer_orders': customer_orders
    }
    return render(request, "dashboard/customer_order/list.html", ctx)

