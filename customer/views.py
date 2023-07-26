from django.shortcuts import render
from .models import Customer
# Create your views here.


def customer_home(request):
    return render(request, 'customer/customer_home.html')


def store(request):
    return render(request, 'customer/store.html')


def product_detail(request):
    return render(request, 'customer/product_detail.html')


def cart(request):
    return render(request, 'customer/cart.html')


def place_order(request):
    return render(request, 'customer/place_order.html')


def order_complete(request):
    return render(request, 'customer/order_complete.html')


def dashboard(request):
    return render(request, 'customer/dashboard.html')


def seller_register(request):
    return render(request, 'customer/seller_register.html')


def seller_login(request):
    return render(request, 'customer/seller_login.html')


def customer_signup(request):
    message = ''
    if request.method == 'POST':  # when user submit the form
        # here fname is the name attribute given in form input
        # fetching values from form data and storing in variable
        first_name = request.POST['fname'] 
        last_name = request.POST['lastname']
        email = request.POST['email']
        gender = request.POST['gender']
        city = request.POST['city']
        country = request.POST['country']
        password = request.POST['password']

        
        # to insert a data in a database table using ORM, we need to 
        # 1. Create an object of the model class and passing values to class properties
        customer = Customer(first_name = first_name, last_name = last_name, gender = gender, email = email, 
                            city = city, country = country, password = password)
        
        # 2. call object.save() method
        # here save() is a method in ORM that is equivalent to 'insert into tablename' query
        customer.save()
        message = 'Registration Succesful'

        # now passing response message to html in a dictionary format


    return render(request, 'customer/customer_signup.html', {'message': message})


def customer_login(request):
    return render(request, 'customer/customer_login.html')


def forgot_password_customer(request):
    return render(request, 'customer/forgot_password_customer.html')


def forgot_password_seller(request):
    return render(request, 'customer/forgot_password_seller.html')