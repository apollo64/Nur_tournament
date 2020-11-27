from django.shortcuts import render, redirect

# Create your views here.
from django.views.generic import FormView, CreateView, ListView

from teams.forms import TeamForm
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
class TeamCreateView(FormView):
    template_name = 'index.html'
    form_class = TeamForm
    success_url = 'divisions'

    def form_valid(self, form):
        # This method is called when valid form data has been POSTed.
        # It should return an HttpResponse.
        # form.send_email()
        return redirect('divisions')

# class AuthorCreate(CreateView):
#     model = Team
#     fields = ['name1',  ]


class DivisionTeamView(ListView):
    model = Team
    context_object_name = 'team_division_list'
    template_name = 'divisions.html'

    def get_queryset(self):
        teams_list = Team.objects.get.all
        for t in teams_list[-8:]:
            Division.objects.create(name ="A", name_teams = t['name'])
        for t in teams_list[:8]:
            Division.objects.create(name ="B", name_teams = t['name'])
        data = {"A": [Division.objects.filter(name__iexact="A")],
                "B": [Division.objects.filter(name__iexact="B")]}
        # divisions = ['A', 'B']
        # for data
        return data

