from django.shortcuts import render
from sume import serializers
from rest_framework import viewsets
from . import models
from rest_framework.response import Response
from django.contrib.auth.models import User


class FornecedoresView(viewsets.ModelViewSet):
    queryset = models.Fornecedores.objects.all()
    serializer_class = serializers.FornecedorSerializer

class NaturezasDespesaView(viewsets.ModelViewSet):
    queryset = models.Fornecedores.objects.all()
    serializer_class = serializers.NaturezasDespesaSerializer

class EstadosBemView(viewsets.ModelViewSet):
    queryset = models.EstadosBem.objects.all()
    serializer_class = serializers.EstadosBemSerializer

class MarcasView(viewsets.ModelViewSet):
    queryset = models.Marcas.objects.all()
    serializer_class = serializers.MarcasSerializer

class SituacoesUsoBemView(viewsets.ModelViewSet):
    queryset = models.SituacoesUsoBem.objects.all()
    serializer_class = serializers.SituacoesUsoBemSerializer

class ItensOrcamentoView(viewsets.ModelViewSet):
    queryset = models.ItensOrcamento.objects.all()
    serializer_class = serializers.ItensOrcamentoSerializer

class NotasFiscais(viewsets.ModelViewSet):
    queryset = models.NotasFiscais.objects.all()
    serializer_class = serializers.NotasFiscaisSerializer

class ItensNotaFiscal(viewsets.ModelViewSet):
    queryset = models.ItensNotaFiscal.objects.all()
    serializer_class = serializers.ItensNotaFiscalSerializer

class BensView(viewsets.ModelViewSet):
    queryset = models.Bens.objects.all()
    serializer_class = serializers.BensSerializer

    # Método GET
    def list(self, request):
        bens = models.Bens.objects.all()                   
                                                        
        lista_bens = []

        for bem in bens:
            bem_serializer = serializers.BensSerializer(bem).data
            
            # Marca
            marca = models.Marcas.objects.filter(id_marca=bem_serializer['id_marca'])
            bem_serializer['marca'] = serializers.MarcasSerializer(marca, many=True).data[0]['marca']
            
            # ItensNotaFiscal
            nota_fiscal = models.ItensNotaFiscal.objects.filter(id_item_nota_fiscal=bem_serializer['id_item_nota_fiscal'])
            bem_serializer['qtd'] = serializers.ItensNotaFiscalSerializer(nota_fiscal, many=True).data[0]['qtd']
            bem_serializer['valor_unitario'] = serializers.ItensNotaFiscalSerializer(nota_fiscal, many=True).data[0]['valor_unitario']
            bem_serializer['produto'] = serializers.ItensNotaFiscalSerializer(nota_fiscal, many=True).data[0]['produto_servico']

            # EstadosBem
            estado = models.EstadosBem.objects.filter(id_estado_bem=bem_serializer['id_estado_bem'])
            bem_serializer['estado'] = serializers.EstadosBemSerializer(estado, many=True).data[0]['estado_bem']
            
            # SituacaoUsoBem
            situacao = models.SituacoesUsoBem.objects.filter(id_situacao_uso_bem=bem_serializer['id_situacao_uso_bem'])
            bem_serializer['situacao'] = serializers.SituacoesUsoBemSerializer(situacao, many=True).data[0]['situacao_uso_bem']

            lista_bens.append(bem_serializer)

        return Response(lista_bens)

    # Método POST
    def create(self, request):
        fornecedor = models.Fornecedores.objects.get(razao_social=request.data['fornecedor'])
        nota = models.NotasFiscais.objects.get(numero=request.data['nota_fiscal'])
        estado = models.EstadosBem.objects.get(estado_bem=request.data['estado'])


        marca = {
            'marca': request.data['marca'],
            'id_user_cad': User.objects.all(),
            'dt_cad': request.data['data_cadastro']
        }

        marca_obj = models.Marcas.objects.create(**marca)

        bem = {
            'id_item_nota_fiscal': nota,
            'tombamento': request.data['tombamento'],
            'id_estado_bem': estado,
            'valor_aquisicao': request.data['valor_unitario'],
            'id_marca': marca_obj,
            'data_lim_garantia': request.data['inicio_garantia'],
            'data_fim_garantia': request.data['termino_garantia'],
            'data_inicio_uso': request.data['data_cadastro'],
            'observacoes': request.data['observacoes'],
            'id_user_cad': User.objects.all(),
            'dt_cad': request.data['data_cadastro']
        }

        bem_obj = models.Bens.objects.create(**bem)

        return Response({'message':'Bem criado com sucesso!'}, status=201)
