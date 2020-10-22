from django.shortcuts import render

# Create your views here.
from django.http.response import JsonResponse
from rest_framework.parsers import JSONParser 
from rest_framework import status
 
from .models import Products
from .serializers import ProductsSerializer
from rest_framework.decorators import api_view


@api_view(['GET', 'POST', 'DELETE'])
def products_list(request):
    # GET list of products, POST a new Products, DELETE all products
    if request.method == 'GET':
        products = Products.objects.all()
        
        title = request.GET.get('title', None)
    
        if title is not None:
            products = products.filter(title__icontains=title)
        
        products_serializer = ProductsSerializer(products, many=True)
        return JsonResponse(products_serializer.data, safe=False)
        # 'safe=False' for objects serialization
    
    elif request.method == 'POST':
        products_data = JSONParser().parse(request)
        products_serializer = ProductsSerializer(data=products_data)
    
        if products_serializer.is_valid():
            products_serializer.save()
            return JsonResponse(products_serializer.data, status=status.HTTP_201_CREATED) 
        return JsonResponse(products_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    if request.method == 'GET': 
        products_serializer = ProductsSerializer(Products) 
        return JsonResponse(products_serializer.data) 
 
    
    
    elif request.method == 'DELETE':
        count = Products.objects.all().delete()
        return JsonResponse({'message': '{} products were deleted successfully!'.format(count[0])}, status=status.HTTP_204_NO_CONTENT)
@api_view(['GET', 'PUT', 'DELETE'])
def products_detail(request, pk):
    # find Products by pk (id)
    try: 
        products = Products.objects.get(pk=pk) 
    except Products.DoesNotExist: 
        return JsonResponse({'message': 'The Products does not exist'}, status=status.HTTP_404_NOT_FOUND) 
 
    # GET / PUT / DELETE Products
    if request.method == 'GET': 
        products_serializer = ProductsSerializer(tutorial) 
        return JsonResponse(products_serializer.data)
    
    elif request.method == 'PUT': 
        products_data = JSONParser().parse(request) 
        products_serializer = ProductsSerializer(Products, data=products_data) 
        if products_serializer.is_valid(): 
            products_serializer.save() 
            return JsonResponse(products_serializer.data) 
        return JsonResponse(products_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    elif request.method == 'DELETE': 
        Products.delete() 
        return JsonResponse({'message': 'Products was deleted successfully!'}, status=status.HTTP_204_NO_CONTENT)
    
    
        
@api_view(['GET'])
def products_list_published(request):
    products = Products.objects.filter(published=True)
        
    if request.method == 'GET': 
        products_serializer = ProductsSerializer(products, many=True)
        return JsonResponse(products_serializer.data, safe=False)