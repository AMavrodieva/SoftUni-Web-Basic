from django.shortcuts import render, redirect

from library.online_library.models import Profile, Book
from library.online_library.forms import ProfileCreateForm, BookAddForm, BookEditForm, ProfileEditForm, \
    ProfileDeleteForm


def get_profile():
    try:
        return Profile.objects.get()
    except Profile.DoesNotExist:
        return None


def index(request):
    profile = get_profile()
    books = Book.objects.all()
    if profile is None:
        return guest(request)
    context = {
        'profile': profile,
        'books': books
    }
    return render(request, 'home-with-profile.html', context)


def add_book(request):
    if request.method == "GET":
        form = BookAddForm()
    else:
        form = BookAddForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')
    context = {
        'form': form
    }
    return render(request, 'add-book.html', context)


def edit_book(request, pk):
    book = Book.objects.filter(pk=pk).get()
    if request.method == "GET":
        form = BookEditForm(instance=book)
    else:
        form = BookEditForm(request.POST, instance=book)
        if form.is_valid():
            form.save()
            return redirect('index')
    context = {
        'book': book,
        'form': form,
    }
    return render(request, 'edit-book.html', context)


def details_book(request, pk):
    book = Book.objects.filter(pk=pk).get()

    context = {
        'book': book,
    }
    return render(request, 'book-details.html', context)


def delete_book(request, pk):
    book = Book.objects.filter(pk=pk).get()
    book.delete()
    return redirect('index')


def guest(request):
    if get_profile() is not None:
        return redirect('index')
    if request.method == "GET":
        form = ProfileCreateForm()
    else:
        form = ProfileCreateForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')
    context = {
        'hide_nav_link': True,
        'form': form
    }
    return render(request, 'home-no-profile.html', context)


def show_profile(request):
    profile = get_profile()
    context = {
        'profile': profile,
    }
    return render(request, 'profile.html', context)


def edit_profile(request):
    profile = get_profile()
    if request.method == "GET":
        form = ProfileEditForm(instance=profile)
    else:
        form = ProfileEditForm(request.POST, instance=profile)
        if form.is_valid():
            form.save()
            return redirect('show profile')
    context = {
        'form': form,
    }

    return render(request, 'edit-profile.html', context)


def delete_profile(request):
    profile = Profile.objects.first()
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
    return render(request, 'delete-profile.html', context)


