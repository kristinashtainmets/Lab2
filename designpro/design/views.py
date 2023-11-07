from django.contrib.auth import logout, authenticate, login
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.mixins import UserPassesTestMixin
from django.shortcuts import redirect
from django.shortcuts import render
from django.urls import reverse, reverse_lazy
from django.views.generic import ListView
from django.views import View
from .forms import ChangeRequestStatusForm
from .forms import CustomUserCreationForm
from .models import Application, Category

from django.views.generic.edit import CreateView, DeleteView, UpdateView


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


class ProfileView(LoginRequiredMixin, ListView):
    model = Application
    template_name = 'profile.html'
    context_object_name = 'applications'

    def get_queryset(self):
        return Application.objects.filter(user=self.request.user)


class CreateRequestView(LoginRequiredMixin, CreateView):
    model = Application
    fields = ['title', 'description', 'category', 'photo_file']
    template_name = 'create_request.html'

    def form_valid(self, form):
        form.instance.user = self.request.user
        form.save()
        return super().form_valid(form)

    def get_success_url(self):
        return reverse('profile')


def form_valid(self, form):
    form.instance.user = self.request.user
    return super().form_valid(form)


class DeleteRequestView(LoginRequiredMixin, DeleteView):
    model = Application
    success_url = reverse_lazy('profile')
    template_name = 'application_delete.html'

class AdminDashboardView(UserPassesTestMixin, View):
    def test_func(self):
        return self.request.user.is_superuser

    def get(self, request):
        all_requests = Application.objects.all()
        categories = Category.objects.all()
        return render(request, 'admin_dashboard.html', {'requests': all_requests, 'categories': categories})

class CategoryCreateView(LoginRequiredMixin, UserPassesTestMixin, CreateView):
    model = Category
    fields = ['name']
    template_name = 'category_new.html'
    success_url = reverse_lazy('admin_dashboard')

    def test_func(self):
        return self.request.user.is_superuser

class CategoryDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Category
    template_name = 'category_delete.html'
    success_url = reverse_lazy('admin_dashboard')

    def test_func(self):
        return self.request.user.is_superuser


class ChangeRequestStatusView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Application
    form_class = ChangeRequestStatusForm
    template_name = 'change_request_status.html'
    success_url = reverse_lazy('admin_dashboard')

    def test_func(self):
        return self.request.user.is_superuser

    def post(self, request, *args, **kwargs):
        self.object = self.get_object()
        form = self.get_form()
        if form.is_valid():
            return self.form_valid(form)
        else:
            return self.form_invalid(form)

    def form_valid(self, form):
        print(self.request.FILES)
        form = ChangeRequestStatusForm(self.request.POST, self.request.FILES, instance=self.object)
        form.save()
        return super().form_valid(form)
