from django.core.exceptions import PermissionDenied
from django.shortcuts import render, redirect
from django.contrib import messages, auth
from django.contrib.auth.models import User
from listings.models import Search

def register(request):
    context = {}
    if request.method == 'POST':
        first_name = request.POST['firstname']
        last_name = request.POST['lastname']
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        password2 = request.POST['password2']

        context = {
            'firstname': first_name,
            'lastname':  last_name,
            'username': username,
            'email': email
        }

        # check passwords
        if password == password2:
            # check username
            if User.objects.filter(username=username).exists():
                messages.error(request, "Username is already taken")
            else:
                if User.objects.filter(email=email).exists():
                    messages.error(request, "E-mail already registered")
                else:
                    # register user
                    user = User.objects.create_user(username=username,
                                                    password=password,
                                                    email=email,
                                                    first_name=first_name,
                                                    last_name=last_name)
                    user.save()
                    messages.success(request, 'Account registered successfully')
                    return redirect('login')
        else:
            messages.error(request, 'Passwords do not match')

    return render(request, 'accounts/register.html', context)

def login(request):
    username = ''
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = auth.authenticate(username=username, password=password)

        if user is not None:
            auth.login(request, user)
            messages.success(request, 'You are now logged in')
            return redirect('index')
        else:
            messages.error(request, 'Invalid credentials')

    return render(request, 'accounts/login.html', {'username': username})

def logout(request):
    if request.method == 'POST':
        auth.logout(request)
        messages.success(request, 'You are now logged out')
        return redirect('index')

def dashboard(request):
    if not request.user.is_authenticated:
        raise PermissionDenied
    user_searches = Search.objects.order_by('-search_date').filter(user=request.user)

    context = {
        'searches': user_searches
    }

    return render(request, 'accounts/dashboard.html', context)
