from django.conf.urls import url
from . import views

urlpatterns = [
    # path('test/', views.contact_home, name='contact'),
    url(r'^create/', views.create_contract, name='create_contract'),
    url(r'^notes/', views.create_notes, name='create_notes'),
    url(r'^api/contact$', views.contact_list),
    url(r'^api/contact/(?P<pk>[0-9]+)$', views.contact_update),
    url(r'^api/contactbyType$', views.contact_lists_by_type),
    # url(r'^api/tutorials/(?P<pk>[0-9]+)$', views.tutorial_detail),
    # url(r'^api/tutorials/published$', views.tutorial_list_published)
]
