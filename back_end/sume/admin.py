from django.contrib import admin

from . import models
from . import actions

class FornecedoresForm(admin.ModelAdmin):
    readonly_fields = ['id_user_cad', 'id_user_alt']
    search_fields = ['razao_social','cnpj','email','telefone']
    list_filter = ['razao_social']
    #actions = [actions.atualiza_fornecedores]
    
    def save_model(self, request, obj, form, change):
        if change:
            obj.id_user_alt = request.user
        else:
            obj.id_user_cad = request.user

        obj.save()
        
class ItensOrcamentoForm(admin.ModelAdmin):
    readonly_fields = ['id_user_cad', 'id_user_alt']
    search_fields = ['qtd','valor_unitario','valor_total']
    list_filter = ['qtd']
    #actions = [actions.atualiza_fornecedores]
    
    def save_model(self, request, obj, form, change):
        if change:
            obj.id_user_alt = request.user
        else:
            obj.id_user_cad = request.user

        obj.save()

class NotasFiscaisForm(admin.ModelAdmin):
    readonly_fields = ['id_user_cad', 'id_user_alt']
    search_fields = ['numero','ano']
    list_filter = ['ano']
    #actions = [actions.atualiza_fornecedores]
    
    def save_model(self, request, obj, form, change):
        if change:
            obj.id_user_alt = request.user
        else:
            obj.id_user_cad = request.user

        obj.save()

class MarcasForm(admin.ModelAdmin):
    readonly_fields = ['id_user_cad', 'id_user_alt']
    search_fields = ['marca']
    list_filter = ['marca']
    #actions = [actions.atualiza_fornecedores]
    
    def save_model(self, request, obj, form, change):
        if change:
            obj.id_user_alt = request.user
        else:
            obj.id_user_cad = request.user

        obj.save()

class ItensNotaFiscalForm(admin.ModelAdmin):
    readonly_fields = ['id_user_cad', 'id_user_alt']
    search_fields = ['qtd', 'valor_unitario', 'produto_servico']
    list_filter = ['produto_servico']
    #actions = [actions.atualiza_fornecedores]
    
    def save_model(self, request, obj, form, change):
        if change:
            obj.id_user_alt = request.user
        else:
            obj.id_user_cad = request.user

        obj.save()

class BensForm(admin.ModelAdmin):
    readonly_fields = ['id_user_cad', 'id_user_alt']
    search_fields = ['tombamento', 'valor_aquisicao']
    #actions = [actions.atualiza_fornecedores]
    
    def save_model(self, request, obj, form, change):
        if change:
            obj.id_user_alt = request.user
        else:
            obj.id_user_cad = request.user

        obj.save()

admin.site.register(models.NaturezasDespesa)
admin.site.register(models.Fornecedores, FornecedoresForm) 
admin.site.register(models.ItensOrcamento, ItensOrcamentoForm)
admin.site.register(models.EstadosBem)
admin.site.register(models.SituacoesUsoBem)
admin.site.register(models.NotasFiscais, NotasFiscaisForm)
admin.site.register(models.Marcas, MarcasForm)
admin.site.register(models.ItensNotaFiscal, ItensNotaFiscalForm)
admin.site.register(models.Bens, BensForm)
