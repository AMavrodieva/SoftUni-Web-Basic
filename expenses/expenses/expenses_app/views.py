from django.shortcuts import render, redirect

from expenses.expenses_app.forms import ProfileCreateForm, ExpensesCreateForm, ExpensesEditForm, ExpensesDeleteForm, ProfileEditForm, ProfileDeleteForm
from expenses.expenses_app.models import Profile, Expenses


def get_profile():
    try:
        return Profile.objects.get()
    except Profile.DoesNotExist:
        return None


def index(request):
    profile = get_profile()
    if profile is None:
        return create_profile(request)
    expenses = Expenses.objects.all()
    left_budget = profile.budget - sum(e.price for e in expenses)
    context = {
        'profile': profile,
        'expenses': expenses,
        'left_budget': left_budget
    }

    return render(request, 'common/home-with-profile.html', context)


def create_expenses(request):
    if request.method == "GET":
        form = ExpensesCreateForm()
    else:
        form = ExpensesCreateForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')

    context = {
        'form': form,
    }
    return render(request, 'expenses/expense-create.html', context)


def edit_expenses(request, pk):
    expenses = Expenses.objects.filter(pk=pk).get()
    if request.method == "GET":
        form = ExpensesEditForm(instance=expenses)
    else:
        form = ExpensesEditForm(request.POST, instance=expenses)
        if form.is_valid():
            form.save()
            return redirect('index')

    context = {
        'form': form,
        'expenses': expenses,
    }
    return render(request, 'expenses/expense-edit.html', context)


def delete_expenses(request, pk):
    expenses = Expenses.objects.filter(pk=pk).get()
    if request.method == "GET":
        form = ExpensesDeleteForm(instance=expenses)
    else:
        form = ExpensesDeleteForm(request.POST, instance=expenses)
        if form.is_valid():
            form.save()
            return redirect('index')

    context = {
        'form': form,
        'expenses': expenses,
    }
    return render(request, 'expenses/expense-delete.html', context)


def create_profile(request):
    if get_profile() is not None:
        return redirect('index')
    if request.method == "GET":
        form = ProfileCreateForm()
    else:
        form = ProfileCreateForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('index')
    context = {
        'nav_hide_link': True,
        'form': form,
    }
    return render(request, 'common/home-no-profile.html', context)


def show_profile(request):
    profile = Profile.objects.first()
    expenses = Expenses.objects.all()
    total_items = expenses.count()
    left_budget = profile.budget - sum(e.price for e in expenses)
    context = {
        'profile': profile,
        'expenses': expenses,
        'total_items': total_items,
        'left_budget': left_budget,
    }
    return render(request, 'profile/profile.html', context)


def edit_profile(request):
    profile = Profile.objects.first()
    if request.method == "GET":
        form = ProfileEditForm(instance=profile)
    else:
        form = ProfileEditForm(request.POST, request.FILES, instance=profile)
        if form.is_valid():
            form.save()
            return redirect('show profile')
    context = {
        'form': form,
    }
    return render(request, 'profile/profile-edit.html', context)


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
    return render(request, 'profile/profile-delete.html', context)

