from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.IndexView.as_view(), name='index'),
    url(r'^create/$', views.CreateView.as_view(), name='create'),
    url(r'^(?P<pk>\d+)/$', views.DetailView.as_view(), name='detail'),
    url(r'^(?P<pk>\d+)/update/$', views.UpdateView.as_view(), name='update'), # /tweet/1/update
    url(r'^(?P<pk>\d+)/delete/$', views.DeleteView.as_view(), name='delete'), # /tweet/1/update
    url(r'^(?P<ecocase_id>[0-9]+)/vote/$', views.vote, name='vote'),
]
