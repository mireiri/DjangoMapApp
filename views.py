from django.shortcuts import render, redirect, get_object_or_404
from triplog.models import Triplog
from triplog.forms import TripForm
from triplog.create_map import create_map


def index(request):
    all_data = Triplog.objects.all()
    context = {
        'title': '旅行の記録 - 一覧画面',
        'all_data': all_data,
    }
    return render(request, 'triplog/index.html', context)

def new(request):
    tripform = TripForm()
    context = {
        'title' : '旅の記録 - 新規作成画面',
        'tripform': tripform,
    }
    return render(request, 'triplog/new.html', context)

def create(request):
    if request.method == 'POST':
        new_data = TripForm(request.POST)
        if new_data.is_valid():
            new_data.save()
    return redirect('index')

def detail(request, id):
    data = get_object_or_404(Triplog, pk=id)
    map = create_map(data.latitude, data.longitude)
    context = {
        'title': '旅の記録 - 詳細画面',
        'data': data,
        'map': map,
    }
    return render(request, 'triplog/detail.html', context)

def edit(request, id):
    data = get_object_or_404(Triplog, pk=id)
    tripform = TripForm(instance=data)
    context = {
        'title': '旅の記録 - 編集画面',
        'data': data,
        'tripform': tripform,
    }
    return render(request, 'triplog/edit.html', context)

def update(request, id):
    if request.method == 'POST':
        data = get_object_or_404(Triplog, pk=id)
        update_data = TripForm(request.POST, instance=data)
        if update_data.is_valid():
            update_data.save()
    return redirect('index')

def delete(request, id):
    delete_data = get_object_or_404(Triplog, pk=id)
    delete_data.delete()
    return redirect('index')
