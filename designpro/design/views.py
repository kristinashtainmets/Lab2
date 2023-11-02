from django.contrib.auth import logout
from django.shortcuts import redirect
from django.shortcuts import render


from .forms import CustomUserCreationForm


# Эта функция будет отвечать за отображение начальной страницы
def index(request):
    # Здесь мы используем функцию render, чтобы отобразить наш шаблон index.html
    return render(request, 'index.html')


def register(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)  # Используйте свою собственную форму регистрации
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = CustomUserCreationForm()  # Используйте свою собственную форму регистрации
    return render(request, 'registration/register.html', {'form': form})


def logout_view(request):
    logout(request)
    return redirect('/')

from django.shortcuts import render
from .models import DesignRequest

def home(request):
    completed_designs = DesignRequest.objects.filter(status='C').order_by('-timestamp')[:4]
    in_progress_count = DesignRequest.objects.filter(status='P').count()
    return render(request, 'index.html', {'completed_designs': completed_designs, 'in_progress_count': in_progress_count})

