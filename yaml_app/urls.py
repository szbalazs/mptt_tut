from django.urls import re_path
from yaml_app.views import (ModelList, EditYamlElementView,
                            show_model, upload_model, delete_element)

urlpatterns = [
    re_path(r'^models/$',ModelList.as_view(),name='model_list'),
    re_path(r'^(?P<pk>\d+)/view/$',show_model,name='model_tree'),
    re_path(r'^upload/$',upload_model,name="upload_model"),
    re_path(r'^element/(?P<pk>\d+)/edit/$',EditYamlElementView.as_view(),name="edit_element"),
    re_path(r'^element/(?P<pk>\d+)/delete/$',delete_element,name="delete_element"),
]
