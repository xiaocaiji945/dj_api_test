from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, Http404, HttpResponseRedirect
from django.template import loader
from django.urls import reverse
from django.views import generic

from .models import Tags, Ttttt


class IndexView(generic.ListView):
    template_name = 'interface/index.html'
    context_object_name = 'latest_question_list'

    def get_queryset(self):
        """Return the last five published questions."""
        return Tags.objects.order_by('-create_at')[:5]


class DetaiView(generic.DetailView):
    model = Tags
    template_name = 'interface/detail.html'


class ResultView(generic.DetailView):
    model = Tags
    template_name = 'interface/results.html'


# # Create your views here.
# def index(request):
#     latest_question_list = Tags.objects.order_by('-create_at')[:5]
#     context = {'latest_question_list': latest_question_list}
#     return render(request, 'interface/index.html', context)
#
#     # latest_question_list = Tags.objects.order_by('-create_at')[:5]
#     # template = loader.get_template('interface/index.html')
#     # context = {
#     #     'latest_question_list': latest_question_list,
#     # }
#     # return HttpResponse(template.render(context, request))
#
#     # output = ', '.join([q.name for q in latest_question_list])
#     # return HttpResponse(output)
#     # return HttpResponse("You'redsxc
#     # looking at tag %s." )
#
#
# def detail(request, tag_id):
#     question = get_object_or_404(Tags, pk=tag_id)
#     return render(request, 'interface/detail.html', {'question': question})
#
#     # return HttpResponse("You're looking at tag %s." % tag_id)
#     # try:
#     #     question = Tags.objects.get(pk=tag_id)
#     # except Tags.DoesNotExist:
#     #     raise Http404("Tags does not exist")
#     # return render(request, 'interface/detail.html', {'question': question})
#
#
# def results(request, tag_id):
#     # response ="You're looking at the results of tag %s."
#     # return HttpResponse(response % tag_id)
#     question = get_object_or_404(Tags, pk=tag_id)
#     # return render(request, 'interface/results.html', {'question': question})
#     return render(request, 'interface/results.html', {'question': question})


def vote(request, tag_id):
    # return HttpResponse("You're voting on tag %s." % tag_id)
    question = get_object_or_404(Tags, pk=tag_id)
    try:
        selected_ttttt = question.ttttt_set.get(pk=request.POST['ttttt'])
    except (KeyError, Ttttt.DoesNotExist):
        # Redisplay the question voting form.
        return render(request, 'interface/detail.html', {
            'question': question,
            'error_message': "You didn't select a ttttt1.",
        })
    else:
        selected_ttttt.votes += 1
        selected_ttttt.save()
        # Always return an HttpResponseRedirect after successfully dealing
        # with POST data. This prevents data from being posted twice if a
        # user hits the Back button.
        return HttpResponseRedirect(reverse('interface:results', args=(question.id,)))
