from django.http import HttpResponse, Http404
from django.shortcuts import get_object_or_404, render
from django.template import loader
from django.urls import reverse
from django.views import generic
from .models import EcoCase, ESM


class IndexView(generic.ListView):
    '''
        Display five lastest ecocases by pub_date.
    '''
    template_name = 'ecocases/index.html'
    context_object_name = 'latest_ecocase_list'

    def get_queryset(self):
        """Return the last five added ecocase. """
        return EcoCase.objects.order_by('-pub_date')[:5]


class DetailView(generic.DetailView):
    '''
        Display ecocase by ecocase_id
    '''
    model = EcoCase
    template_name = 'ecocases/detail.html'


# def index(request):
#     '''
#         Display five lastest ecocases by pub_date.
#     '''
#     latest_ecocase_list = EcoCase.objects.order_by('-pub_date')[:5]
#     context = {'latest_ecocase_list': latest_ecocase_list}
#     return render(request, 'ecocases/index.html', context)


# def detail(request, ecocase_id):
#     '''
#         Display ecocase by ecocase_id
#     '''
#     ecocase = get_object_or_404(EcoCase, pk=ecocase_id)
#     return render(request, 'ecocases/detail.html', {'ecocase': ecocase})
