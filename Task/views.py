from django.shortcuts import render
from .serializers import TaskSerializer
from .models import Task
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view
# Create your views here.

@api_view(['GET', 'POST'])
def TaskAPI(request):
    try:
        tasks=Task.objects.all()
    except Task.DoesNotExist:
        return Response(status=status.HTTP_400_BAD_REQUEST)

    if request.method == 'GET':
        serialized_data = TaskSerializer(tasks, many=True)
        return Response(serialized_data.data, status=status.HTTP_200_OK)

    elif request.method == 'POST':
        serialized_data=TaskSerializer(data=request.GET)
        if serialized_data.is_valid():
            serialized_data.save()
            return Response(serialized_data.data, status=status.HTTP_201_CREATED)

@api_view(['GET', 'PUT', 'DELETE'])
def TaskDetails(request,id):
    try:
        get_task=Task.objects.get(id=id)
    except Task.DoesNotExist:
        return Response(status=status.HTTP_400_BAD_REQUEST)
    
    if request.method == 'GET':
        serialized_data=TaskSerializer(get_task)
        return Response(serialized_data.data, status=status.HTTP_200_OK)
    elif request.method == 'PUT':
        serialized_data=TaskSerializer(get_task, data=request.GET)
        if serialized_data.is_valid():
            serialized_data.save()
            return Response(serialized_data.data, status=status.HTTP_200_OK)
    elif request.method == 'DELETE':
        get_task.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)