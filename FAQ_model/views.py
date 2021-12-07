from FAQ_model.models import FAQ
from FAQ_model.serializers import FAQSerializer
from rest_framework import generics
from rest_framework.response import Response
from django.shortcuts import render, get_object_or_404

'''API CON FILTROS DEPARTAMENTOS'''
class FaqData(generics.ListAPIView):

    def get(self, request):
        # Se toma el id del departamento al que pertenece el usuario
        idgroup = request.user.groups.values_list('id').first()
        # Filtra el modelo por departamento
        faq = FAQ.objects.filter(departamento=(idgroup))
        serializer = FAQSerializer(faq, many=True)
        return Response(serializer.data)