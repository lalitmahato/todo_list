from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import authenticate, login
from django.contrib.auth.forms import AuthenticationForm
from .forms import CustomUserCreationForm


def signup_view(request):
    if request.method == 'POST':
        # request.FILES is required for image upload
        form = CustomUserCreationForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, 'Account created successfully! Please login.')
            return redirect('login')  # We will create this URL next
    else:
        form = CustomUserCreationForm()
    context = {
        'form': form
    }
    return render(request, 'users/signup.html', context)


def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                messages.info(request, f"Welcome {username}!")
                return redirect('task_list') # Redirect to dashboard/home in real app
            else:
                messages.error(request, "Invalid username or password.")
        else:
            messages.error(request, "Invalid username or password.")
    else:
        form = AuthenticationForm()
        # Add Bootstrap styling manually for built-in form
        for field in form.fields.values():
            field.widget.attrs['class'] = 'form-control'

    return render(request, 'users/login.html', {'form': form})