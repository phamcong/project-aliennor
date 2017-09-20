import os
from django.http import HttpResponse, HttpResponseRedirect, Http404
from django.shortcuts import get_object_or_404, render
from django.views.generic.edit import FormView
from django.template import loader
from django.conf import settings
from django.core.files.storage import FileSystemStorage
from django.urls import reverse
from django.views import generic
from django.core.urlresolvers import reverse_lazy

from .models import EcoCase, ESM
from .forms import EcoCaseForm

from pprint import pprint


class IndexView(generic.ListView):
    '''
        Display five lastest ecocases by pub_date.
    '''
    template_name = 'ecocases/index.html'
    context_object_name = 'latest_ecocase_list'

    def get_queryset(self):
        """Return the last five added ecocase. """
        return EcoCase.objects.order_by('-timestamp')[:5]


class DetailView(generic.DetailView):
    '''
        Display ecocase by ecocase_id
    '''
    model = EcoCase
    template_name = 'ecocases/detail.html'


# class CreateView(generic.CreateView):
#     '''
#         Create new ecocase
#     '''
#     model = EcoCase
#     template_name = 'ecocase/post_ecocase.html'
#     form_class = EcoCaseForm

class CreateView(FormView):
    form_class = EcoCaseForm
    template_name = 'ecocases/create.html'
    success_url = reverse_lazy('ecocases:index')

    def post(self, request, *args, **kwargs):
        # uploaded_dir = settings.MEDIA_ROOT + 'ecocases/'
        # # uploaded_dir = os.path.join(settings.MEDIA_ROOT, '/ecocases/')
        # print('media_root: '+ settings.MEDIA_ROOT)
        # print('upload_dir:', uploaded_dir)
        # uploaded_file_urls = []

        # form_class = self.get_form_class()
        # form = self.get_form(form_class)          
        # uploaded_files = request.FILES.getlist('ecocase_images')       
        
        # if form.is_valid():
        #     joined_title = '_'.join(form.cleaned_data['ecocase_title'].split(' '))
        #     for count, x in enumerate(uploaded_files):
        #         def save_uploaded_file(f, uploaded_file_url):
        #             print('upload_file_url:' + uploaded_file_url)
        #             with open(uploaded_file_url, 'wb+') as destination:
        #                 for chunk in f.chunks():
        #                     destination.write(chunk)
        #         uploaded_file_url = uploaded_dir + joined_title + '_' + str(count) + '.' + x.name.split('.')[-1]
        #         print('upload_file_url2:' + uploaded_file_url)
        #         save_uploaded_file(x, uploaded_file_url)
        #         uploaded_file_urls.append(uploaded_file_url)
            
        #     print(uploaded_file_urls)

        #     ecocase = EcoCase(ecocase_title=form.cleaned_data['ecocase_title'],
        #                     ecocase_description=form.cleaned_data['ecocase_description'],
        #                     ecocase_characters=form.cleaned_data['ecocase_characters'],
        #                     ecocase_image_urls=';'.join(uploaded_file_urls)
        #                     )
        #     ecocase.save()

        #     return self.form_valid(form)
        # else:
        #     return self.form_invalid(form)
        form_class = self.get_form_class()
        form = self.get_form(form_class)
        images = request.FILES.getlist('ecocase_images')
        fs = FileSystemStorage(location=os.path.join(settings.BASE_DIR, 'media/ecocases'))
        image_url_list = []
        if form.is_valid():
            joined_title = '_'.join(form.cleaned_data['ecocase_title'].split(' '))

            for count, x in enumerate(images):
                image_extension = x.name.split('.')[-1]
                new_image_name = joined_title + '_' + str(count) + '.' + image_extension
                uploaded_image = fs.save(new_image_name, x)
                image_url_list.append('../media/ecocases/'+new_image_name)

            ecocase = EcoCase(ecocase_title=form.cleaned_data['ecocase_title'],
                              ecocase_description=form.cleaned_data['ecocase_description'],
                              ecocase_characters=form.cleaned_data['ecocase_characters'],
                              ecocase_image_urls=';'.join(image_url_list)
                              )
            ecocase.save()

            print(image_url_list)

            return self.form_valid(form)
        else:
            return self.form_invalid(form)

# def post_ecocase(request):
#     if request.method == 'POST':
#         form = request.POST
#         images = request.FILES.getlist('ecocase_images')
#         f_s = FileSystemStorage()

#         if form.is_valid():
#             joined_title = form.cleaned_data['ecocase_title'].join('_')
#             uploaded_image_urls = []
#             for count, x in enumerate(images):
#                 new_image_name = joined_title + '_' + str(count)
#                 uploaded_image = f_s.save(new_image_name, x)
#                 uploaded_image_urls.append(f_s.url(uploaded_image))
#                 # def process(f):
#                 #     newfilename = joined_title + '_' + str(count)

#                 #     with open('/media/ecocases/images/' + joined_title + '_' + str(count), 'wb+') as destination:
#                 #         for chunk in f.chunks():
#                 #             destination.write(chunk)
#                 # process(x)
#             ecocase = EcoCase(ecocase_title = form.cleaned_data['title'],
#                             ecocase_description = form.cleaned_data['description'],
#                             ecocase_characters = form.cleaned_data['characters'],
#                             ecocase_images = images,
#                             ecocase_image_urls = uploaded_image_urls,
#             )
#             ecocase.save()
#     return render(request, 'ecocases/post_ecocase.html', 'form')

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