from django.shortcuts import render, redirect
from .models import League, Team, Player

from . import team_maker

def index(request):
	context = {
		"leagues": League.objects.all(),
		"teams": Team.objects.all(),
		"players": Player.objects.all(),
		'baseball': League.objects.filter(name__contains='baseball'),
		'women': League.objects.filter(name__contains='women'),
		'hockey': League.objects.filter(name__contains='hockey'),
		'footballNot': League.objects.exclude(name__contains='footbal'),
		'conference': League.objects.filter(name__contains='conference'),
		'atlantic': League.objects.filter(name__contains='atlantic'),
		"dallas": Team.objects.filter(location__contains='dallas'),
		"raptors": Team.objects.filter(team_name__contains='raptors'),
		"city": Team.objects.filter(location__contains='city'),
		"tteams": Team.objects.filter(team_name__startswith='T'),
		"order": Team.objects.all().order_by('location'),
		"order2": Team.objects.all().order_by('-team_name'),
		"edwards": Player.objects.filter(last_name__contains='Edwards'),
		"joshuas": Player.objects.filter(first_name__contains='Joshua'),
		"edwards2": Player.objects.filter(last_name__contains='Edwards').exclude(first_name__contains='Joshua'),
		"alexWyatt": Player.objects.filter(first_name__contains='Alexander') | Player.objects.filter(first_name__contains='Wyatt'),
	}
	return render(request, "leagues/index.html", context)

def make_data(request):
	team_maker.gen_leagues(10)
	team_maker.gen_teams(50)
	team_maker.gen_players(200)

	return redirect("index")