from rest_framework import serializers
from .models import Tweet

class TweetSerializer(serializers.ModelSerializer):
    # シリアライザクラスの設定を行う内部クラス、Meta
    class Meta:
        model = Tweet

        fields = ["id", "user", "content", "created_at"]