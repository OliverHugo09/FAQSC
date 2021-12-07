from rest_framework import serializers
from FAQ_model.models import FAQ, Categoria

#Serializers FAQ

class FAQSerializer(serializers.ModelSerializer):

    infocategorias = serializers.SerializerMethodField('contentCategoria')

    def contentCategoria(self, data):
        categorias = Categoria.objects.get(categoria=data.categorias)
        if (categorias != None):
            return {'categoria': categorias.categoria}
        else:
            return {'categoria': ''}
            
    class Meta:
        model=FAQ
        fields=('id','titulo','descripcion','infocategorias')
        