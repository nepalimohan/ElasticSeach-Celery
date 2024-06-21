from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework import viewsets
from rest_framework.response import Response


from elasticsearch_dsl.query import MultiMatch
from .documents import ProductDocument

from .models import Product
from .serializers import ProductSerializer

# Create your views here.
class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    
class ProductSearch(APIView):
    def get(self, request):
        q = request.GET.get('q')
        if q:
            #fuzziness - results similar words as well
            query = MultiMatch(query=q, fields=['name', 'description'], fuzziness="AUTO")
            search = ProductDocument.search().query(query)
            response = search.execute()
            print(response)
            serializer = ProductSerializer(response.hits, many=True)
            return Response(serializer.data)
        return Response([])