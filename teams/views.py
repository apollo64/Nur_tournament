import random

from django.shortcuts import render, redirect

# Create your views here.
from django.views.generic import FormView, CreateView, ListView
from requests import Response

from teams.forms import TeamForm, TeamFormset
from teams.models import Team, Division


# def create_view(request):
#    # if request.method == 'GET':
#    #     form = ArticleForm()
#    #     return render(request, 'create.html', context={'form': form})
#    if request.method == 'POST':
#        form = ArticleForm(data=request.POST)
#        if form.is_valid():
#            data = form.cleaned_data
#            if isinstance(data , dict):
#                for key_name in data.keys():
#                    Team.objects.create(name=data[key_name])
#                    Team.save()
#                if 'team_name' in data.keys():
#                    obj_team = data['team_name']
#                    if isinstance(obj_team, list):
#                        for name in obj_team:
#                            Team.objects.create(name=name, score = 0)
#            return redirect('division_table')
#        else:
#            return render(request, 'index2.html', context={'form': form})
#
# class TeamCreateView(FormView):
#     template_name = 'index.html'
#     form_class = TeamForm
#     success_url = 'divisions'
#
#     def form_valid(self, form):
#         # This method is called when valid form data has been POSTed.
#         # It should return an HttpResponse.
#         # form.send_email()
#
#         # return redirect('divisions')
#         for i in form:
#             Team.objects
#         return Response(status=200)

# class AuthorCreate(CreateView):
#     model = Team
#     fields = ['name1',  ]

def create_teams_normal(request):
    template_name = 'index.html'
    heading_message = 'Welcome to tournament'
    # max_number_teams = 2 cv
    if request.method == 'GET':
        formset = TeamFormset(request.GET or None)
    elif request.method == 'POST':
        formset = TeamFormset(request.POST)
        list_teams = []
        team_a = []
        team_b = []
        if formset.is_valid():
            try:
                # a_div = Division.objects.get_or_create(name="A")
                # b_div = Division.objects.get_or_create(name="A")
                a_div = Division.objects.get(name="A")
                b_div = Division.objects.get(name="B")
            except:
                Division(name = "A").save()
                Division(name = "B").save()
                a_div = Division.objects.get(name="A")
                b_div = Division.objects.get(name="B")
            for form in formset:
                name = form.cleaned_data.get('name')
                list_teams.append(name)
                random.shuffle(list_teams)
                team_a = list_teams[:9]
                team_b = list_teams[9:]
            for form in formset:
                # extract name from each form and save
                name = form.cleaned_data.get('name')
                # save book instance
                if name:
                    if name in team_a:
                        Team(name=name, division=a_div).save()
                    else:
                        Team(name=name, division=b_div).save()
                    # redirect('divisions')
            # once all books are saved, redirect to book list view

            return redirect('divisions')
    return render(request, template_name, {
        'formset': formset,
        'heading': heading_message,
    })


class DivisionTeamView(ListView):
    model = Team
    context_object_name = 'team_division_list'
    template_name = 'divisions.html'
    queryset = Team.objects.all()
