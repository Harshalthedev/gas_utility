from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from .forms import AdminRegistrationForm # type: ignore
from .models import AdminUser  # Use AdminUser instead of default User

# Home/Login Page
def authlogin(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('customer_dashboard')
        else:
            messages.error(request, 'Username or Password Invalid!')

    return render(request, 'index.html')

# Logout
def authlogout(request):
    logout(request)
    messages.success(request, 'Logout Successfully!')
    return redirect('login')

# User Registration
def registration(request):
    if request.method == 'POST':
        username = request.POST.get('name')
        email = request.POST.get('email')
        password = request.POST.get('password')
        confirm_password = request.POST.get('confirm_password')

        if password == confirm_password:
            if AdminUser.objects.filter(username=username).exists():
                messages.error(request, 'Username already exists')
            elif AdminUser.objects.filter(email=email).exists():
                messages.error(request, 'Email already exists')
            else:
                user = AdminUser.objects.create_user(username=username, password=password, email=email)
                user.save()
                return redirect('customer_login')
        else:
            messages.error(request, 'Passwords do not match!')

    return render(request, 'registration.html')

# Customer Dashboard
def customer_dashboard(request):
    return render(request, 'customer_dashboard.html')

# Forget Password
def forgetpassword(request):
    return render(request, 'forget.html')

# customer_login
def customer_login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)
        if user is not None:  # Removed `usertype` check
            login(request, user)
            return redirect('customer_dashboard')
        else:
            messages.error(request, 'Invalid Customer Credentials!')

    return render(request, 'customer_login.html')
    return render(request, 'customer_login.html')
# Admin Registration View
def admin_register(request):
    if request.method == 'POST':
        form = AdminRegistrationForm(request.POST)
        if form.is_valid():
            admin_user = form.save(commit=False)
            admin_user.set_password(form.cleaned_data['password'])  # Hash password
            admin_user.save()
            messages.success(request, "Admin registered successfully!")
            return redirect('admin_login')
        else:
            messages.error(request, "Error in registration! Please check the form.")
    else:
        form = AdminRegistrationForm()
    return render(request, 'admin_register.html', {'form': form})

# Admin Login View
def admin_login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)

        if user is not None and hasattr(user, 'usertype') and user.usertype == 'admin':
            login(request, user)
            return redirect('admin_dashboard')
        else:
            messages.error(request, "Invalid credentials!")

    return render(request, 'admin_login.html')

# Admin Dashboard View
def admin_dashboard(request):
    return render(request, 'admin_dashboard.html')

# Admin Logout View
def admin_logout(request):
    logout(request)
    messages.success(request, "Logged out successfully!")
    return redirect('admin_login')