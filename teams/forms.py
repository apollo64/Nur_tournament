from django import forms
from django.forms import widgets, formset_factory


# class TeamForm(forms.Form):
#     name1 = forms.CharField(max_length=20, required=True, label='Название команды #1')
#     name2 = forms.CharField(max_length=20, required=True, label='Название команды #2')
#     name3 = forms.CharField(max_length=20, required=True, label='Название команды #3')
#     name4 = forms.CharField(max_length=20, required=True, label='Название команды #4')
#     name5 = forms.CharField(max_length=20, required=True, label='Название команды #5')
#     name6 = forms.CharField(max_length=20, required=True, label='Название команды #6')
#     name7 = forms.CharField(max_length=20, required=True, label='Название команды #7')
#     name8 = forms.CharField(max_length=20, required=True, label='Название команды #8')
#     name9 = forms.CharField(max_length=20, required=True, label='Название команды #9')
#     name10 = forms.CharField(max_length=20, required=True, label='Название команды #10')
#     name11 = forms.CharField(max_length=20, required=True, label='Название команды #11')
#     name12 = forms.CharField(max_length=20, required=True, label='Название команды #12')
#     name13 = forms.CharField(max_length=20, required=True, label='Название команды #13')
#     name14 = forms.CharField(max_length=20, required=True, label='Название команды #14')
#     name15 = forms.CharField(max_length=20, required=True, label='Название команды #15')
#     name16 = forms.CharField(max_length=20, required=True, label='Название команды #16')

class TeamForm(forms.Form):
    name = forms.CharField(
        label='Team Name',
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': 'Enter Team name here'
        }))
    class Meta:
        fields = ('name')
TeamFormset = formset_factory(TeamForm, min_num=2, max_num=2)

