from django.http import HttpResponse, Http404
from django.shortcuts import get_object_or_404, render
from django.template import loader
from .models import EcoCase, ESM

def index(request):
    '''
        Display five lastest ecocases by pub_date.
    '''
    latest_ecocase_list = EcoCase.objects.order_by('-pub_date')[:5]
    context = {'latest_ecocase_list': latest_ecocase_list}
    return render(request, 'ecocases/index.html', context)

def detail(request, ecocase_id):
    '''
        Display ecocase by ecocase_id
    '''
    ecocase = get_object_or_404(EcoCase, pk=ecocase_id)
    return render(request, 'ecocases/detail.html', {'ecocase': ecocase})