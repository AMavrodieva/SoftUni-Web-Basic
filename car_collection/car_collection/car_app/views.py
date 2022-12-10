from django.shortcuts import render, redirect

from car_collection.car_app.forms import ProfileCreateForm, CarCreateForm, CarEditForm, CarDeleteForm, ProfileEditForm, \
    ProfileDeleteForm
from car_collection.car_app.models import Profile, Car


def get_profile():
    try:
        return Profile.objects.get()
    except Profile.DoesNotExist:
        return None


def index(request):
    profile = get_profile()
    if profile is None:
        return guest(request)
    context = {
        'profile': profile,
    }
    return render(request, 'common/index.html', context)


def show_catalogue(request):
    cars = Car.objects.all()
    total_cars = cars.count()
    context = {
        'cars': cars,
        'total_cars': total_cars,
    }
    return render(request, 'car/catalogue.html', context)


def guest(request):
    if get_profile() is not None:
        return redirect('index')
    context = {
        'nav_hide_link': True,
    }
    return render(request, 'common/index.html', context)


def create_profile(request):
    if request.method == "GET":
        form = ProfileCreateForm()
    else:
        form = ProfileCreateForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('show catalogue')
    context = {
        'form': form,
    }

    return render(request, 'profile/profile-create.html', context)


def details_profile(request):
    profile = Profile.objects.get()
    cars = Car.objects.all()
    cars_price = sum(c.price for c in cars)
    context = {
        'profile': profile,
        'total_price_car': cars_price,
    }
    return render(request, 'profile/profile-details.html', context)


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
    return render(request, 'profile/profile-edit.html', context)


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
    return render(request, 'profile/profile-delete.html', context)


def create_car(request):
    if request.method == "GET":
        form = CarCreateForm()
    else:
        form = CarCreateForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('show catalogue')
    context = {
        'form': form,
    }
    return render(request, 'car/car-create.html', context)


def details_car(request, pk):
    car = Car.objects.filter(pk=pk).get()
    context = {
        'car': car
    }
    return render(request, 'car/car-details.html', context)


def edit_car(request, pk):
    car = Car.objects.filter(pk=pk).get()
    if request.method == "GET":
        form = CarEditForm(instance=car)
    else:
        form = CarEditForm(request.POST, instance=car)
        if form.is_valid():
            form.save()
            return redirect("show catalogue")
    context = {
        'form': form,
        'car': car,
    }
    return render(request, 'car/car-edit.html', context)


def delete_car(request, pk):
    car = Car.objects.filter(pk=pk).get()
    if request.method == "GET":
        form = CarDeleteForm(instance=car)
    else:
        form = CarDeleteForm(request.POST, instance=car)
        if form.is_valid():
            form.save()
            return redirect("show catalogue")
    context = {
        'form': form,
        'car': car,
    }
    return render(request, 'car/car-delete.html', context)

