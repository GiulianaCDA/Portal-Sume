from django.utils.translation import ngettext
from django.contrib import messages

def atualiza_fornecedores(modeladmin, request, fornecedores):

    for fornecedor in fornecedores:
        fornecedor.razao_social = "teste action"
        fornecedor.save()

    modeladmin.message_user(request, ngettext(
        'Nome de fornecedor atualizado',
        'Nomes de fornecedores atualizados',
        len(fornecedores)
    ))

    