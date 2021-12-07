from FAQ_model.models import FAQ
from FAQ_model.serializers import FAQSerializer
from rest_framework import generics
from rest_framework.response import Response
from django.shortcuts import render, get_object_or_404

'''TEMPLATES DE PRUEBA'''
from django.views.generic import TemplateView

class AboutView(TemplateView):
    template_name = "about.html"

class ApiView(TemplateView):
    template_name = "api.html"



'''API CON FILTROS DEPARTAMENTOS'''
class FaqData(generics.ListAPIView):

    def get(self, request):
        # Se toma el id del departamento al que pertenece el usuario
        idgroup = request.user.groups.values_list('id').first()
        # Filtra el modelo por departamento
        faq = FAQ.objects.filter(departamento=(idgroup))
        serializer = FAQSerializer(faq, many=True)
        return Response(serializer.data)


class FaqDataDetail(generics.ListAPIView):
    
    def get_object(self, pk):
        faq = get_object_or_404(FAQ, pk=pk)
        return faq

    def get(self, request, pk):
        faq = self.get_object(pk)
        serializer = FAQSerializer(faq)
        return Response(serializer.data)