from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse

from .models import Greeting, Hello

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
