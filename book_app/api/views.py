from rest_framework.decorators import api_view
from django.http import JsonResponse,HttpResponse
from django.shortcuts import render
from .serializers import BookSerializer
from book_app.models import Book
from rest_framework.parsers import JSONParser


@api_view(['GET', 'POST'])
def book_list(request):
    if request.method == 'GET':
        all_book= Book.objects.all()
        serializer= BookSerializer(all_book,many=True)
        return JsonResponse(serializer.data, safe=False)
    if request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = BookSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)

@api_view(['GET', 'POST','DELETE'])
def book_detail(request,pk):
    if request.method == 'GET':
        book = Book.objects.get(pk=pk)
        serializer = BookSerializer(book)
        return JsonResponse(serializer.data)

    if request.method == 'PUT':
        data = JSONParser().parse(request)
        book = Book.objects.get(pk=pk)
        serializer = BookSerializer(book, data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data)
        return JsonResponse(serializer.errors, status=400)

    if request.method == 'DELETE':
        book = Book.objects.get(pk=pk)
        book.delete()
        return HttpResponse(status=204)