from rest_framework.decorators import api_view
from django.http import HttpResponse
from django.shortcuts import render
from .serializers import BookSerializer
from book_app.models import Book
from rest_framework.parsers import JSONParser
from rest_framework.response import Response

@api_view(['GET', 'POST'])
def book_list(request):
    if request.method == 'GET':
        all_book= Book.objects.all()
        serializer= BookSerializer(all_book,many=True)
        return Response(serializer.data)
    if request.method == 'POST':
        
        serializer = BookSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)

@api_view(['GET', 'PUT','DELETE'])
def book_detail(request,pk):
    if request.method == 'GET':
        book = Book.objects.get(pk=pk)
        serializer = BookSerializer(book)
        return Response(serializer.data)

    if request.method == 'PUT':
        
        book = Book.objects.get(pk=pk)
        serializer = BookSerializer(book, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=400)

    if request.method == 'DELETE':
        book = Book.objects.get(pk=pk)
        book.delete()
        return HttpResponse(status=204)