from django.shortcuts import render, HttpResponse, redirect
from .models.product import Product
from .models.category import Category
from .models.customer import Customer
from django.contrib.auth.hashers import make_password, check_password

# Create your views here.
def index(request):
    products = None
    categories = Category.get_all_categories()
    category_id = request.GET.get('category')
    if category_id :
        products = Product.get_all_products_by_id(category_id)
    else:
        products = Product.get_all_products()
    data = {
        'products':products,
        'categories':categories
    }
    print("you are : ", request.session.get('email'))
    return render(request, "index.html", data)

def signup(request):
    print(request.method)
    if request.method == 'POST':  
        first_name = request.POST.get('firstname')
        last_name = request.POST.get('lastname')
        phone = request.POST.get('phone')
        email = request.POST.get('email')
        password = request.POST.get('password')

    

        print(first_name, last_name, phone, email, password)
        customer = Customer(first_name=first_name, last_name=last_name,phone=phone,email=email,password=password)
        customer.password = make_password(customer.password)

        customer.save()
        return redirect("homepage")
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

      