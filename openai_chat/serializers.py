from rest_framework import serializers


class ChatGPTSerializer(serializers.Serializer):
    prompt = serializers.CharField()
