import os
import openai

from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated


openai.organization = "org-bHHZvypLUlPQWeXCWrwEd8nt"
openai.api_key = os.getenv("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")
openai.Model.list()


class GetChatResponse(APIView):

    def post(self, request):
        serializer = openai.Model.serializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors)
