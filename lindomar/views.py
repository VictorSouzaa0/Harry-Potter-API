from django.shortcuts import render
from rest_framework import views
from rest_framework.response import Response
from .models import *
from .serializers import *

class SpellAPIView(views.APIView):

    #Post -> cadastrar dados na API
    def post(self, request):

        #Armazernar os dados que estão e, JSON
        spellJson = request.data 

        # Transformando o JSON em python
        spellSerialized = SpellSerializer(data=spellJson)

        #Verificar se os dados estão corretos
        spellSerialized.is_valid(raise_exception=True)

        spellSerialized.save()
        
        return Response(status=201, data=spellSerialized.data)