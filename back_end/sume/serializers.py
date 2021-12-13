from rest_framework import serializers
from . import models


class FornecedorSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Fornecedores
        fields = '__all__'

class NaturezasDespesaSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.NaturezasDespesa
        fields = '__all__'

class EstadosBemSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.EstadosBem
        fields = '__all__'

class MarcasSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Marcas
        fields = '__all__'

class SituacoesUsoBemSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.SituacoesUsoBem
        fields = '__all__'

class ItensOrcamentoSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.ItensOrcamento
        fields = '__all__' 

class BensSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Bens
        fields = '__all__' 

class NotasFiscaisSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.NotasFiscais
        fields = '__all__' 

class ItensNotaFiscalSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.ItensNotaFiscal
        fields = '__all__' 