from django.http import HttpResponse
from django.template import loader
from django.shortcuts import render, get_object_or_404
##a importação do modulo get_objects_or_404 é um atalho para a renderização de modelos de erro
##quando o objeto buscado não faz parte da base ainda
##a implementação segue o exmeplo que ficara em utilização, ambos os demais serão comentados.

from django.http import Http404

from .models import Question

#a importação de novos modulos se faz necessario para renderizar os templates


##criadas as views das paginas de detalhes, resulktados, index e vote.
##As mesmas são referenciadas nas telas de Urls, para que sejam renderizadas de forma correta.

def index(request):
    lasted_question_list = Question.objects.order_by('-pub_date')[:5]
    template = loader.get_template('polls/index.html')
    context = {
        'lasted_question_list': lasted_question_list,
    }

    return HttpResponse(template.render(context, request))

##é possível substituir o template, com o retorno da resposta Http, pela função de render, que é mais enxuta de certa forma
## a sintaxe seria a seguinte

##def index(request):
    ##lasted_question_list = Qestion.objects.order_by('-pub_date')[:5]
    ##context = {'lasted_question_list': lasted_question_list}
    ##return render(request, 'polls/index.html',context)

##nesse caso, a visão da index foi gerada dentro da propria função, e esse problema é conhecido como
##um problema de design
##a resolução desse problema pode ser a utilização dos templates em python.

def detail(request, question_id):
    ##a implementação do try catch simula um tratamento de exceção caso a question não exista na base de dados.
    ##try:
        ##question = Question.objects.get(pk=question_id)
    ##except:
        ##raise Http404('Question does not exist.')
    #caso a funcao detail consiga carregar os dados passados pelo id da questão solicitada, então ele renderiza o template
    #caso contrario, é renderizado uma tela de erro 404, de pagina nao encontrda, padrão django.
    ##return render(request, 'polls/detail.html', {'question': question})

    question = get_object_or_404(Question, pk=question_id)
    ##a linha acima faz a busca do id passado dentro da lista de Question, caso haja ele faz o processo de renderização
    ##caso não, ele faz o render de uma tela de erro padrão do 404
    return render(request, 'polls/detail.html', {'question': question})
    #quando a pagina não é renderizada, a mensagem padrão é algo parecido com 'No question matches the given query"

def results(request, question_id):
    response = "You're looking at the results of question %s."
    return HttpResponse(response % question_id)


def vote(request, question_id):
    return HttpResponse("You're voting on question %s." %question_id)


#a pasta templates sempre é carregada pela DjangoTemplates, onde são carregados e renderizados.
