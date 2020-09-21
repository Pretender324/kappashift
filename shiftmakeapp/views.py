from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import CreateView
from django.contrib import messages
from .models import CompetitionModel, ShiftModel, EventModel

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
        object_list = ShiftModel.objects.filter(competition__id=competition)
    suggest = CompetitionModel.objects.all()
    return render(request, 'timetable.html', {'suggest': suggest, 'pk': pk, 'object_list': object_list})


def timetableregister(request, pk):
    if request.method == 'POST':
        sex = request.POST.getlist('sex')
        distance = request.POST.getlist('distance')
        style = request.POST.getlist('style')
        start_time = request.POST.getlist('start_time')
        competition = CompetitionModel.objects.get(pk=pk)
        ShiftModel.objects.filter(competition=competition).delete()
        for item in zip(sex, distance, style, start_time):
            event = EventModel.objects.filter(
                sex=item[0], distance=item[1], style=item[2]).get()
            p = ShiftModel(competition=competition,
                           event=event, start_time=item[3])
            p.save()
        return redirect('shift:entry')


def entryfunc(request):
    return render(request, 'entry.html')
