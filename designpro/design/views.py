from django.contrib.auth import logout
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import redirect
from django.shortcuts import render
from django.views import generic

from .forms import CustomUserCreationForm
from .models import Application


def index(request):
    Applications_title = Application.objects.all()
    Applications_description = Application.description
    Applications_category = Application.category
    return render(request, 'index.html', context={Applications_title: Application.objects.all(),
                                                  Applications_description: Application.description,
                                                  Applications_category: Application.category})


class ApplicationListView(LoginRequiredMixin, generic.ListView):
    model = Application


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
    return redirect('/')


from django.shortcuts import render


def home(request):
    completed_designs = Application.objects.filter(status='C').order_by('-date')[:4]
    in_progress_count = Application.objects.filter(status='P').count()
    return render(request, 'index.html',
                  {'completed_designs': completed_designs, 'in_progress_count': in_progress_count})
