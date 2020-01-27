from django.shortcuts import render
from .models import Blog
from rest_framework.viewsets import ModelViewSet
from .serializers import BlogSerializer
# Create your views here.


class BlogViewSet(ModelViewSet):
    serializer_class = BlogSerializer
    queryset = Blog.objects.all()

