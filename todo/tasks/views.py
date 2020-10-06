from django.shortcuts import render
# Create your views here.
from django.http import HttpResponse

def helloworld(request):
	return HttpResponse('Hello world!')

def taskList(request):
	return render(request, 'tasks/list.html')

def yourName(request, name):
	return render(request, 'tasks/yourname.html', {'name': name})

