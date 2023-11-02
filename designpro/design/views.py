from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render
from django.views import generic
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

