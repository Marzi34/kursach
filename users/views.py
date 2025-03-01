from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from .forms import CustomUserCreationForm, CustomAuthenticationForm, UserProfileForm
from .models import Client
from django.contrib.auth import login, authenticate
from django.contrib.auth import views as auth_views
from django.contrib import messages

from .models import CustomUser


def register(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            client = Client(user=user)
            client.save()
            return redirect('/')
        else:
            print(form.errors)
    else:
        form = CustomUserCreationForm()
    return render(request, 'accounts/register.html', {'form': form})

def login_view(request):
    if request.method == 'POST':
        form = CustomAuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('/')
    else:
        form = CustomAuthenticationForm()
    return render(request, 'accounts/login.html', {'form': form})

class CustomLogoutView(auth_views.LogoutView):
    def get(self, request, *args, **kwargs):
        messages.success(request, "Вы успешно вышли из системы.")
        return super().dispatch(request, *args, **kwargs)

@login_required
def profile_view(request):
    current_user = request.user

    if request.method == 'POST':
        form = UserProfileForm(request.POST, instance=current_user)
        if form.is_valid():
            form.save()
            return redirect('profile')
    else:
        form = UserProfileForm(instance=current_user)

    edit_mode = request.GET.get('edit', 'false') == 'true'

    return render(request, 'accounts/profile.html', {'form': form, 'edit_mode': edit_mode,})
