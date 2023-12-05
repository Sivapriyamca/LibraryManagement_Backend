from django.shortcuts import render

# Create your views here.
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from django.http.response import JsonResponse
from BookApp.serializers import BookSerializer
from BookApp.models import Book

@csrf_exempt
def bookApi(request,id=0):
    if request.method=='GET':
        book = Book.objects.all()
        book_serializer=BookSerializer(book,many=True)
        return JsonResponse(book_serializer.data,safe=False)
    elif request.method=='POST':
        book_data=JSONParser().parse(request)
        book_serializer=BookSerializer(data=book_data)
        if book_serializer.is_valid():
            book_serializer.save()
            return JsonResponse("Added Successfully")
        return JsonResponse("Failed to Add",safe=False)
    elif request.method=='PUT':
        book_data=JSONParser().parse(request)
        book=Book.objects.get(id=id)
        book_serializer=BookSerializer(book,data=book_data)
        if book_serializer.is_valid():
            book_serializer.save()
            return JsonResponse("Updated Successfully",safe=False)
        return JsonResponse("Failed to Update")
    elif request.method=='DELETE':
        book=Book.objects.get(id=id)
        book.delete()
        return JsonResponse("Deleted Successfully",safe=False)
