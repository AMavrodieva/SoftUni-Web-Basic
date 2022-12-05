from django.shortcuts import render, redirect

from games_play_app.games.models import Profile, Game
from games_play_app.games.forms import ProfileCreateForm, GameCreateForm, GameEditForm, GameDeleteForm, ProfileEditForm, \
    ProfileDeleteForm


def get_profile():
    try:
        return Profile.objects.get()
    except Profile.DoesNotExist as ex:
        return None


def index(request):
    profile = get_profile()
    if profile is None:
        return guest(request)
    return render(request, 'common/home-page.html')


def show_dashboard(request):
    games = Game.objects.all()
    context = {
        'games': games
    }
    return render(request, 'common/dashboard.html', context)


def create_game(request):
    if request.method == "GET":
        form = GameCreateForm()
    else:
        form = GameCreateForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('show dashboard')
    context = {
        'form': form
    }
    return render(request, 'game/create-game.html', context)


def details_game(request, pk):
    game = Game.objects.filter(pk=pk).get()
    context = {
        'game': game
    }
    return render(request, 'game/details-game.html', context)


def edit_game(request, pk):
    game = Game.objects.filter(pk=pk).get()
    if request.method == "GET":
        form = GameEditForm(instance=game)
    else:
        form = GameEditForm(request.POST, instance=game)
        if form.is_valid():
            form.save()
            return redirect('show dashboard')
    context = {
        'form': form,
        'game': game,
    }
    return render(request, 'game/edit-game.html', context)


def delete_game(request, pk):
    game = Game.objects.filter(pk=pk).get()
    if request.method == "GET":
        form = GameDeleteForm(instance=game)
    else:
        form = GameDeleteForm(request.POST, instance=game)
        if form.is_valid():
            form.save()
            return redirect('show dashboard')

    context = {
        'form': form,
        'game': game,
    }
    return render(request, 'game/delete-game.html', context)


def guest(request):
    if get_profile() is not None:
        return redirect('index')

    context = {
        'hide_nav_link': True,
    }
    return render(request, 'common/home-page.html', context)


def create_profile(request):
    if request.method == "GET":
        form = ProfileCreateForm()
    else:
        form = ProfileCreateForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')
    context = {
        'form': form,
        'hide_nav_link': True
    }
    return render(request, 'account/create-profile.html', context)


def details_profile(request):
    profile = Profile.objects.get()
    games = Game.objects.all()
    total_games = len(games)
    try:
        avg_rating = sum(game.rating for game in games) / total_games
    except ZeroDivisionError:
        avg_rating = 0.0

    context = {
        'profile': profile,
        'total_games': total_games,
        'avg_rating': avg_rating

    }
    return render(request, 'account/details-profile.html', context)


def edit_profile(request):
    profile = Profile.objects.get()
    if request.method == "GET":
        form = ProfileEditForm(instance=profile)
    else:
        form = ProfileEditForm(request.POST, instance=profile)
        if form.is_valid():
            form.save()
            return redirect('details profile')
    context = {
        'form': form,
    }
    return render(request, 'account/edit-profile.html', context)


def delete_profile(request):
    profile = Profile.objects.get()
    if request.method == "GET":
        form = ProfileDeleteForm(instance=profile)
    else:
        form = ProfileDeleteForm(request.POST, instance=profile)
        if form.is_valid():
            form.save()
            return redirect('index')
    context = {
        'form': form,
    }
    return render(request, 'account/delete-profile.html', context)
