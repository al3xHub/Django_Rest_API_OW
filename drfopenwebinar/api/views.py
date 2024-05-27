import json
from typing import Any
from django.utils.decorators import method_decorator
from django.http import HttpRequest, JsonResponse
from django.http.response import HttpResponse as HttpResponse
from django.shortcuts import render
from django.views import View
from django.views.decorators.csrf import csrf_exempt
from .models import Task

# Create your views here.
class TaskView(View):
    
    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)
    
    def get(self, request, pk=0):
        if pk > 0:   
            tasks = list(Task.objects.filter(id=pk).values())
            if tasks:
                task = tasks[0]
                datos = {'message':'done!', 'tasks': task}
            else:
                datos = {'message':'There is no taks available with that ID'}
            return JsonResponse(datos)
        else:
            tasks = list(Task.objects.values())
            if tasks:
                datos = {'message':'done!', 'tasks': tasks}
            else:
                datos = {'message':'There is no taks available'}
            return JsonResponse(datos)
        
            
    def post(self, request):
        jd = json.loads(request.body)
        
        Task.objects.create(
            title = jd['title'],
            description = jd['description'],
        )
        
        datos = {'message':'No data available'}
        return JsonResponse(datos)
    
    def put(self, request, pk=0):
        jd = json.loads(request.body)
        tasks = list(Task.objects.filter(id=pk).values())
        
        if tasks:
            task = Task.objects.get(id=pk)
            task.title = jd['title']
            task.description = jd['description']
            task.complete= jd['complete']
            task.save()
            datos = {'message':'Done!'}
        else:
            datos = {'message': 'List not found'}
        return JsonResponse(datos)
        
    def delete(self, request, pk=0):
        tasks = list(Task.objects.filter(id=pk).values())
        if tasks:
            Task.objects.filter(id=pk).delete()
            datos = {'message':'deleted succesfully'}
        else:
            datos = {'message':'Not found'}
        return JsonResponse(datos)
        