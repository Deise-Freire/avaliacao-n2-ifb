from django.shortcuts import render
from .models import StatusSenha, Senha
from django.http import Http404

# Create your views here.
def index(request):
    try:
        status = StatusSenha.objects.get(nome='Na fila')
    except:
         raise Http404('Status não encontrado')
    senhas = Senha.objects.filter()
    return render(request, 'index.html', {'senhas': senhas})

