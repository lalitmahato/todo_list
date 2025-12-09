from django.shortcuts import render, redirect
from django.contrib import messages
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

    return render(request, 'users/signup.html', {'form': form})