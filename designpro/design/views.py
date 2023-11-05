from django.contrib.auth import logout, authenticate, login
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic.edit import DeleteView
from django.urls import reverse_lazy
from django.shortcuts import redirect
from django.shortcuts import render
from django.urls import reverse
from django.views.generic import ListView
from django.views import View

from .forms import CustomUserCreationForm
from .models import Application
from django.views.generic.edit import CreateView


class ApplicationListView(ListView):
    model = Application
    template_name = 'aplication_list.html'
    context_object_name = 'application'

    def get_queryset(self):
        status = self.request.GET.get('status', 'all')
        if status != 'all':
            return Application.objects.filter(status=status)
        return Application.objects.all()


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


class ProfileView(LoginRequiredMixin, View):
    def get(self, request):
        return render(request, 'profile.html')


class CreateRequestView(LoginRequiredMixin, CreateView):
    model = Application
    fields = ['title', 'description', 'category', 'photo_file']
    template_name = 'create_request.html'

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)

    def get_success_url(self):
        return reverse('profile')


def form_valid(self, form):
    form.instance.user = self.request.user
    return super().form_valid(form)

class ApplicationDeleteView(LoginRequiredMixin, DeleteView):
    model = Application
    template_name = 'application_confirm_delete.html'
    success_url = reverse_lazy('profile')

    def get_queryset(self):
        owner = self.request.user
        return self.model.objects.filter(user=owner)
