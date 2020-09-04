from django.shortcuts import render, redirect
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.contrib import messages
from django.contrib.auth.views import LoginView
from django.urls import reverse_lazy
from .models import MemberModel
import logging

# Create your views here.


class KappaLogin(LoginView):
    template_name = 'login.html'


class MemberView(ListView):
    template_name = 'member.html'
    model = MemberModel

    def get_queryset(self):
        return MemberModel.objects.order_by('-grade')


class MemberCreate(CreateView):
    model = MemberModel
    template_name = 'create.html'
    fields = ('first_name', 'last_name', 'sex', 'grade', 'member_type')
    success_url = reverse_lazy('create')

    def form_valid(self, form):
        self.object = member = form.save()
        messages.info(self.request, '{}を登録しました'.format(
            member.last_name + member.first_name))
        return redirect(self.get_success_url())


class MemberUpdate(UpdateView):
    model = MemberModel
    template_name = 'update.html'
    fields = ('first_name', 'last_name', 'sex', 'grade', 'member_type')
    success_url = reverse_lazy('member')


class MemberDelete(DeleteView):
    model = MemberModel
    template_name = 'delete.html'
    success_url = reverse_lazy('member')


def topfunc(request):
    return render(request, 'top.html')
