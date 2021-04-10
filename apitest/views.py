from django.shortcuts import render
from django.http import JsonResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import ItemSerializer
from .models import Items

# Create your views here.
@api_view(['GET'])
def apiOverView(request):
    api_url={
        'List':'/item-list/',
        'Detail View':'/item-detail/<str:pk>',
        'Create':'/item-create/',
        'Update':'/task-update/<str:pk>',
        'Delete':'/task-delete/<str:pk>'
    }
    return Response(api_url)


@api_view(['GET'])
def itemList(request):
    items = Items.objects.all()
    serializer = ItemSerializer(items,many=True)
    return Response(serializer.data)

@api_view(['GET'])
def itemDetail(request,pk):
    items = Items.objects.get(itemId=pk)
    serializer = ItemSerializer(items,many=False)
    return Response(serializer.data)

@api_view(['POST'])
def itemCreate(request):
    serializer = ItemSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)

@api_view(['POST'])
def itemUpdate(request,pk):
    items = Items.objects.get(itemId=pk)
    serializer = ItemSerializer(instance=items,data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)

@api_view(['DELETE'])
def itemDelete(request,pk):
    items = Items.objects.get(itemId=pk)
    items.delete()
    return Response('Item successfully deleted')