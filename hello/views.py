from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse

from .models import Greeting, Hello, Video, Pessoa
from .forms import PessoaForm

import requests

# Create your views here.
def index(request):
   # return HttpResponse('Hello n!')
    return render(request, "index.html")
#def index(request):
  #  r = requests.get('http://httpbin.org/status/418')
   # print(r.text)
  #  return HttpResponse('<pre>' + r.text + '</pre>')

def db(request):

    greeting = Greeting()
    greeting.save()

    greetings = Greeting.objects.all()

    return render(request, "db.html", {"greetings": greetings})


def lucasteste(request):
   # return HttpResponse('Hello n!')
    return render(request, "lucasteste.html")

def list(request):
    tasksSelect = Hello.objects.all()
    return render(request, "list.html", {'taskView1': tasksSelect})

def taskView(request, id):
    task = get_object_or_404(Hello, pk=id)
    return render(request, "tasks/task.html", {'task': task})

def videos(request):
    videoSelect = Video.objects.all()
    return render(request, "videos.html", {'video': videoSelect})

def pessoa(request):
    return render(request, "pessoa.html")

def newPessoa(request):
    if request.method == 'POST':
        form = PessoaForm(request.POST)

        if form.is_valid():
            pessoa = form.save()
            return redirect('/pessoa')

    else:
        form = PessoaForm()
        return render(request, "newPessoa.html", {'form': form})