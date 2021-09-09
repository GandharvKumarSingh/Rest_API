from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view
from crud.serializers import StudentSerializer
from crud.models import Student

# Create your views here.


@api_view(['GET'])
def studentList(request):
    query = Student.objects.all()
    serializer = StudentSerializer(query, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def studentDetail(request, pk):
    query = Student.objects.get(id=pk)
    serializer = StudentSerializer(query, many=False)
    return Response(serializer.data)


@api_view(['POST'])
def studentCreate(request):
    serializer = StudentSerializer(data=request.data)

    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)


@api_view(['POST'])
def studentUpdate(request, pk):
    query = Student.objects.get(id=pk)
    serializer = StudentSerializer(instance=query, data=request.data)

    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)


@api_view(['DELETE'])
def studentDelete(request, pk):
    query = Student.objects.get(id=pk)
    query.delete()

    return Response('DELETED')
