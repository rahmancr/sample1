from django.contrib.messages import success
from django.shortcuts import render
from django.shortcuts import render


from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import login, authenticate
from django.db import IntegrityError
from .models import Product
from django.utils.datastructures import MultiValueDictKeyError

from .models import customer_register


# Create your views here.
def home(request):
    return render(request,'home.html')

# def register(request):
#     if request.method == 'POST':
#         username = request.POST['username']
#         password = request.POST['password']
#         mobile_number = request.POST['phone']
#
#
#         myuser = User.objects.create_user(username, password, mobile_number)
#         myuser.save()
#         return render(request, 'customer_register.html',{'message': 'Registration successful'})
#
#     else:
#         return render(request,'customer_register.html',{'message2': 'something error'})


from django.shortcuts import render, redirect
 # Ensure the correct model import

# def login(request):
#     if request.method == 'POST':
#         username = request.POST['username']
#         password = request.POST['password']
#         try:
#             user = customer_register.objects.cdget(username=username)
#             if user.password == password:
#                 request.session['cusid'] = username
#                 cusid = request.session.get('cusid')
#                 if not cusid:
#                     return redirect('login')
#                 user = customer_register.objects.get(username=cusid)
#                 if 'products' in request.POST:
#                     selected_products = request.POST.getlist('products')
#                     user.history = ','.join(selected_products)
#                     user.save()
#                     products = Product.objects.all()
#                     return render(request, 'userpage.html', { 'u': user.username, 'products': products, 'success_msg': "Products added to history!" })
#
#                 products = Product.objects.all()
#
#                 return render(request, 'userpage.html', {
#                     'u': user.username,
#                     'products': products,
#                     'success_msg': "Login Successful!"
#                 })
#                 return render(request, "userpage.html", {'u': username})
#             else:
#                 return render(request, 'login.html', {'err_msg': "Incorrect Password or Username"})
#         except customer_register.DoesNotExist:
#             return render(request, 'login.html', {'err_msg': "Incorrect Password or Username"})
#     return render(request, 'login.html')





def register(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        mobile_number = request.POST['phone']

        data1 = customer_register.objects.create(username=username, password=password,mobile_number=mobile_number)
        data1.save()
        return render(request, 'customer_register', {'message': "Created "})


    else:
        return render(request, 'customer_register.html', {'message2': 'Something went wrong'})



from django.shortcuts import render, redirect
from .models import customer_register, Product
from django.utils.datastructures import MultiValueDictKeyError

def login(request):
    if request.method == 'POST':
        # Safely get the username and password
        username = request.POST.get('username')
        password = request.POST.get('password')

        if not username or not password:
            return render(request, 'login.html', {'err_msg': "Please enter both username and password."})

        try:
            user = customer_register.objects.get(username=username)
            if user.password == password:
                request.session['cusname'] = username  # Store the username in the session

                if 'products' in request.POST:
                    selected_products = request.POST.getlist('products')

                    # Convert selected products to a comma-separated string and store it in the history field
                    user.history = ','.join(selected_products)
                    user.save()

                    products = Product.objects.all()

                    return render(request, 'userpage.html', {
                        'u': user.username,
                        'products': products,
                        'success_msg': "Products added to history!"
                    })

                # If no products are submitted, display the user page with products
                products = Product.objects.all()

                return render(request, 'userpage.html', {
                    'u': user.username,
                    'products': products,
                    'success_msg': "Login Successful!"
                })
            else:
                return render(request, 'login.html', {'err_msg': "Incorrect Password or Username"})
        except customer_register.DoesNotExist:
            return render(request, 'login.html', {'err_msg': "Incorrect Password or Username"})
    return render(request, 'login.html')


