from django.shortcuts import render, redirect

from notes.notes_app.forms import ProfileForm, NoteCreateForm, NoteEditForm, NoteDeleteForm
from notes.notes_app.models import Profile, Note


def get_profile():
    try:
        return Profile.objects.get()
    except Profile.DoesNotExist:
        return None


def index(request):
    profile = get_profile()
    notes = Note.objects.all()
    if profile is None:
        return guest(request)
    context = {
        'profile': profile,
        'notes': notes,
    }
    return render(request, 'home-with-profile.html', context)


def add_note(request):
    if request.method == "GET":
        form = NoteCreateForm()
    else:
        form = NoteCreateForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')
    context = {
        'form': form,
    }
    return render(request, 'note-create.html', context)


def edit_note(request, pk):
    note = Note.objects.filter(pk=pk).get()
    if request.method == "GET":
        form = NoteEditForm(instance=note)
    else:
        form = NoteEditForm(request.POST, instance=note)
        if form.is_valid():
            form.save()
            return redirect('index')
    context = {
        'form': form,
        'note': note,
    }
    return render(request, 'note-edit.html', context)


def delete_note(request, pk):
    note = Note.objects.filter(pk=pk).get()
    if request.method == "GET":
        form = NoteDeleteForm(instance=note)
    else:
        form = NoteDeleteForm(request.POST, instance=note)
        if form.is_valid():
            form.save()
            return redirect('index')
    context = {
        'form': form,
        'note': note,
    }
    return render(request, 'note-delete.html', context)


def details_note(request, pk):
    note = Note.objects.filter(pk=pk).get()
    context = {
        'note': note
    }
    return render(request, 'note-details.html', context)


def guest(request):
    if get_profile() is not None:
        return redirect('index')
    if request.method == "GET":
        form = ProfileForm()
    else:
        form = ProfileForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')
    context = {
        'nav_hide_link': True,
        'form': form
    }
    return render(request, 'home-no-profile.html', context)


def show_profile(request):
    profile = get_profile()
    notes = Note.objects.all().count()
    context = {
        'profile': profile,
        'notes': notes,
    }
    return render(request, 'profile.html', context)


def delete_profile(request):
    profile = Profile.objects.first()
    notes = Note.objects.all()

    profile.delete()
    notes.delete()
    return redirect('index')
