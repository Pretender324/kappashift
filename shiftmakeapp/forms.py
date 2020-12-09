from django import forms


class TimetableForm(forms.Form):
    sex = forms.ChoiceField(choices=(('M', '男'), ('W', '女')))
    distance = forms.IntegerField()
    style = forms.ChoiceField(choices=(('Fr', 'Fr'), ('Ba', 'Ba'), (
        'Br', 'Br'), ('Fly', 'Fly'), ('IM', 'IM'), ('FR', 'FR'), ('MR', 'MR')))
    start_time = forms.TimeField()
