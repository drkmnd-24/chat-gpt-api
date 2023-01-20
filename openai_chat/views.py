from .serializers import ChatGPTSerializer

from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.permissions import AllowAny

import openai


class ChatGPTAPIView(APIView):
    serializer_class = ChatGPTSerializer
    permission_classes = [AllowAny]
    """ChatGPT POST Method"""
    def post(self, request):
        serializer = ChatGPTSerializer(data=request.data)
        if serializer.is_valid():
            openai.api_key = "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"
            prompt = serializer.validated_data['prompt']
            response = openai.Completion.create(
                engine="text-davinci-002",
                prompt=prompt,
                max_tokens=1024,
                n=1,
                stop=None,
                temperature=0.5,
            )
            message = response.choices[0].text
            return Response({"message": message}, status=200)
        return Response(serializer.errors, status=400)
