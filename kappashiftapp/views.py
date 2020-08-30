from django.shortcuts import render
from django.views.generic import ListView
from django.contrib.auth.views import LoginView
from django.urls import reverse_lazy
from .models import MemberModel

# Create your views here.


class KappaLogin(LoginView):
    template_name = 'login.html'
    reverse_lazy('top')


class MemberView(ListView):
    template_name = 'member.html'
    model = MemberModel


def topfunc(request):
    return render(request, 'top.html')
