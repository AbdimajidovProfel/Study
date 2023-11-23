from django.shortcuts import render, redirect
from django.db.models import Q
from .models import *
from .forms import *


def index(request):
    cats = Category.objects.all()
    rms = RoomModel.objects.all()
    if request.GET.get('search'):
        rms = RoomModel.objects.filter(Q(title__icontains=request.GET.get("search"))|
                                       Q(content__icontains=request.GET.get('search')))
    context = {"rms": rms, 'cats': cats}
    return render(request, 'index.html', context)


def by_category(request, cat_id):
    rms = RoomModel.objects.filter(category=cat_id)
    context = {"rms": rms}
    return render(request, 'category.html', context)


def create_room(request):
    form = RoomForm()

    if request.method == "POST":
        form = RoomForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    context = {'form': form}
    return render(request, 'room_form.html', context)


def update_room(request, pk):
    room = RoomModel.objects.get(id=pk)
    form = RoomForm(instance=room)

    if request.method == "POST":
        form = RoomForm(request.POST, instance=room)

        if form.is_valid():
            form.save()
            return redirect('home')
    context = {'form': form}
    return render(request, 'room_form.html', context)


def delete_room(request, pk):
    room = RoomModel.objects.get(id=pk)
    if request.method == "POST":
        room.delete()
        return redirect('home')
    context = {"obj": room}
    return render(request, 'room_delete.html', context)


def create_topic(request):
    form = RoomForm(request.POST)

    if request.method == "POST":
        form = RoomForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')

        context = {'form': form}
        return render(request, 'room_form.html', context)