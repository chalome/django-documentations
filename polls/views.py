from django.shortcuts import render,get_object_or_404
from django.http import HttpResponse,HttpResponseRedirect
from django.urls import reverse
from .models import Choice
from .models import Question
from django.template import loader
from django.http import Http404
from django.db.models import F
from django.views import generic
# def index(request):
#     latest_question_list = Question.objects.order_by("-pub_date")[:5]
#     template= loader.get_template("polls/index.html")
#     context = {"latest_question_list":latest_question_list}
#     return HttpResponse(template.render(context,request))

# def index(request):
#     # return HttpResponse("Hello, world. You're at the polls index.")
#     latest_question_list = Question.objects.order_by("-pub_date")[:5]
#     template = loader.get_template("polls/index.html")
#     result = ", ".join([q.question_text for q in latest_question_list])
#     context = {"latest_question_list": latest_question_list}
#     return HttpResponse(template.render(context, request))
    # return HttpResponse(result)

def index(request):
    latest_question_list = Question.objects.order_by("-pub_date")[:5]
    context = {"latest_question_list": latest_question_list}
    return render(request, "polls/index.html", context)

# def detail(request, question_id):
#     try:
#         question=Question.objects.get(pk=question_id)
#     except Question.DoesNotExist:
#         raise Http404("Question does not exist!")
#     return render(request,"polls/details.html",{"question":question})

def detail(request,question_id):
    question = get_object_or_404(Question, pk=question_id)
    return render(request, "polls/details.html", {"question": question})

def not_found(request,exception):
    return render(request,"polls/notFound.html")

def vote(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    try:
        selected_choice = question.choice_set.get(pk=request.POST["choice"])
    except (KeyError, Choice.DoesNotExist):
        # Redisplay the question voting form.
        return render(
            request,
            "polls/details.html",
            {
                "question": question,
                "error_message": "You didn't select a choice.",
            },
        )
    else:
        selected_choice.votes = F("votes") + 1
        selected_choice.save()
        # Always return an HttpResponseRedirect after successfully dealing
        # with POST data. This prevents data from being posted twice if a
        # user hits the Back button.
        return HttpResponseRedirect(reverse("results", args=(question.id,)))

def results(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    return render(request, "polls/results.html", {"question": question})

class IndexView(generic.ListView):
    # model=Question
    context_object_name = 'latest_question_list'
    template_name = 'polls/index.html'
    
    # def get_queryset(self):
    #     return super().get_queryset().order_by("-pub_date")[:5]
    def get_queryset(self):
        return Question.objects.order_by("-pub_date")[:5]

class DetailView(generic.DetailView):
    model = Question
    template_name = 'polls/details.html'
    
class ResultView(generic.DetailView):
    model = Question
    template_name = 'polls/results.html'