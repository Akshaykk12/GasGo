from django.shortcuts import render, HttpResponse, redirect
from .models.product import Product
from .models.category import Category
from .models.customer import Customer
from .models.orders import Order
from django.contrib.auth.hashers import make_password, check_password
from django.views import View

# Create your views here.


from django.shortcuts import render, redirect
from .models import Product, Category

def index(request):
    if 'customer_id' not in request.session:
        return redirect('login')
    categories = Category.get_all_categories()
    products = None
    category_id = request.GET.get('category')
    
    if category_id:
        products = Product.get_all_products_by_id(category_id)
    else:
        products = Product.get_all_products()
    
    if request.method == "POST":
        product_id = request.POST.get('product')
        address = request.POST.get('address')
        phone = request.POST.get('phone')
        customer_id = request.session.get('customer_id')
        price = Product.get_price_of_a_product(product_id)

        order = Order(customer = Customer(id = customer_id),
                      product = Product(id = product_id),
                      price = price,
                      address = address,
                      phone = phone,
                      quantity = 1
                      )
        order.save()

        return redirect('homepage')
    data = {
        'products': products,
        'categories': categories
    }
    
    return render(request, "index.html", data)


def signup(request):
    if request.method == 'POST':  
        first_name = request.POST.get('firstname')
        last_name = request.POST.get('lastname')
        phone = request.POST.get('phone')
        email = request.POST.get('email')
        password = request.POST.get('password')

        customer = Customer(first_name=first_name, last_name=last_name,phone=phone,email=email,password=password)
        customer.password = make_password(customer.password)

        customer.save()
        return redirect("login")
    return render(request, 'signup.html')

def login(request):
    error_message = None
    if request.method == "POST":
        email = request.POST.get('email')
        password = request.POST.get('password')
        customer = Customer.get_customer_by_email(email)
        
        if customer:
            flag = check_password(password, customer.password)
            if flag:

                request.session['customer_id'] = customer.id
                request.session['email'] = customer.email
                return redirect("homepage")
            else:
                error_message = "Password Invalid"
        else:
            error_message = "Email Invalid"
    return render(request, 'login.html', {"error": error_message})

def logout(request):
    request.session.flush() 
    return redirect('login')

def orders(request):
    if 'customer_id' not in request.session:
        return redirect('login')
    customer = request.session.get('customer_id')
    orders = Order.get_orders_by_customer(customer)
    orders = orders.reverse()
    return render(request, 'orders.html', { 'orders' : orders })
      