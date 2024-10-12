from django.shortcuts import render
from rest_framework import viewsets
from .models import Tweet
from .serializers import TweetSerializer

# Create your views here.
class TweetViewSet(viewsets.ModelViewSet):
    # Tweetモデルからすべてのオブジェクトを取得
    queryset = Tweet.objects.all()

    serializer_class = TweetSerializer

