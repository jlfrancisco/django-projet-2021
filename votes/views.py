from django.shortcuts import render, get_object_or_404
from django.http import Http404, HttpResponseRedirect
from django.urls import reverse

from .models import Question

def index(request):
    dernieres_questions = Question.objects.order_by('-pub_date')[:5]
    output = ', '.join([q.question_text for q in dernieres_questions])
    return render(request, 'votes/index.html', {'dernieres_questions': dernieres_questions})

def detail(request, question_id):
    # try:
    #     question = Question.objects.get(pk=question_id)
    # except Question.DoesNotExist:
    #     raise Http404("La question #%s n'existe pas" % question_id)
    question = get_object_or_404(Question, pk=question_id)
    return render(request, 'votes/detail.html', {'question': question})


def results(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    return render(request, 'votes/resultats.html', {'question': question})


def vote(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    try:
        selected_choice = question.choice_set.get(pk=request.POST['choice'])
    except (KeyError, Choice.DoesNotExist):
        # Redisplay the question voting form.
        return render(request, 'votes/detail.html', {
            'question': question,
            'error_message': "Faites un bon choix svp!",
        })
    else:
        selected_choice.votes += 1
        selected_choice.save()
        # Always return an HttpResponseRedirect after successfully dealing
        # with POST data. This prevents data from being posted twice if a
        # user hits the Back button.
        return HttpResponseRedirect(reverse('results', args=(question.id,)))