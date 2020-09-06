from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import CreateView
from django.contrib import messages
from .models import CompetitionModel

# Create your views here.


class CompetitionCreate(CreateView):
    template_name = 'competitioncreate.html'
    model = CompetitionModel
    fields = ('name', 'year', 'start_date', 'end_date', 'days')
    success_url = reverse_lazy('shift:competition')

    def get_context_data(self, **kwargs):
        # get_context_data をオーバーライドした例
        # テンプレートに渡すコンテキストに任意の変数を追加できる
        context = super(CompetitionCreate, self).get_context_data(**kwargs)
        # テンプレートに渡すコンテキストに `user_count` という変数を追加
        context['name_suggest'] = CompetitionModel.objects.values_list(
            'name', flat=True)
        return context

    def form_valid(self, form):
        self.object = competition = form.save()
        messages.info(self.request, '{}年{}を登録しました'.format(
            competition.year, competition.name))
        return redirect(self.get_success_url())

    def form_invalid(self, form):
        messages.warning(self.request, 'この大会は既に存在しています')
        return render(self.request, 'competitioncreate.html', context={"form": form})
