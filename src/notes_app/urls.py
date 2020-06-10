from django.conf.urls import url
from django.urls import  include
from . import views

app_name = 'notes_app'
urlpatterns = [

    url(r'^$', views.all_notes, name='all_notes'),
    #url(r'^(?P<id>\d+)$', views.detail, name='note_detail'),
    url(r'^(?P<slug>[-\w]+)/$', views.detail, name='note_detail'),
    url(r'^add$', views.note_add, name='add_note'),
    url(r'^(?P<slug>[-\w]+)/edit$', views.edit, name='note_edit'),


]