from django.shortcuts import render
# Create your views here.
from django.http import HttpResponse

def helloworld(request):
	return HttpResponse('world')


def taskList(request):
	return render(request, 'tasks/list.html')

