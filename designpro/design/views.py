from django.contrib.auth import logout, authenticate, login
from django.contrib.auth.forms import AuthenticationForm

from django.shortcuts import redirect
from django.shortcuts import render
from django.views import generic
from django.views.generic import ListView

from .forms import CustomUserCreationForm
from .models import Application


class ApplicationListView(ListView):
    model = Application
    template_name = 'aplication_list.html'
    context_object_name = 'application'


def register(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = CustomUserCreationForm()
    return render(request, 'registration/register.html', {'form': form})


def logout_view(request):
    logout(request)
    return redirect('index')


def home(request):
    completed_designs = Application.objects.filter(status='C').order_by('-date')[:4]
    in_progress_count = Application.objects.filter(status='P').count()
    return render(request, 'index.html',
                  {'completed_designs': completed_designs, 'in_progress_count': in_progress_count})


def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('index')
    else:
        form = AuthenticationForm()
    return render(request, 'registration/login.html', {'form': form})
