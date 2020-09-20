from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import CreateView
from django.contrib import messages
from .models import CompetitionModel, ShiftModel

# Create your views here.


class CompetitionCreate(CreateView):
    template_name = 'competitioncreate.html'
    model = CompetitionModel
    fields = ('name', 'year', 'start_date', 'end_date', 'days')
    success_url = reverse_lazy('shift:timetable')

    def get_success_url(self, pk):
        return reverse_lazy('shift:timetable', kwargs={'pk': pk})

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
        return redirect(self.get_success_url(pk=competition.id))

    def form_invalid(self, form):
        messages.warning(self.request, 'この大会は既に存在しています')
        return render(self.request, 'competitioncreate.html', context={"form": form})


def timetableupdatefunc(request, pk):
    suggest = CompetitionModel.objects.all()
    return render(request, 'timetable.html', {'suggest': suggest, 'pk': pk})


def timetablesuggest(request, pk):
    if request.method == 'POST':
        competition = request.POST['competition']
        print(competition)
        object_list = ShiftModel.objects.filter(competition__id=competition)
    suggest = CompetitionModel.objects.all()
    print(object_list)
    return render(request, 'timetable.html', {'suggest': suggest, 'pk': pk, 'object_list': object_list})
