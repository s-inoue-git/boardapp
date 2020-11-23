from django.shortcuts import render, redirect
from .models import BoardModel
from django.views.generic import CreateView
from django.urls import reverse_lazy

def hello_func(request):
    return render(request, 'hello.html', {'say': 'Hello World!!'})

def list_func(request):
    object_list = BoardModel.objects.all()
    return render(request, 'list.html', {'object_list': object_list})

def detail_func(request, pk):
    object = BoardModel.objects.get(pk=pk)
    return render(request, 'detail.html', {'object': object})

class BoardCreate(CreateView):
    template_name = 'create.html'
    model = BoardModel
    fields = ('title', 'author', 'content', 'images')
    success_url = reverse_lazy('list')

def good_func(request, pk):
    object = BoardModel.objects.get(pk=pk)
    object.good += 1
    object.save()
    return redirect('list')

