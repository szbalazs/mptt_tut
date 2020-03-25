from django.shortcuts import render, redirect,get_object_or_404
from django.views.generic import ListView, UpdateView
from django.urls import reverse_lazy

import yaml

from yaml_app.models import YamlModel, YamlElement, save_model_elements
from yaml_app.forms import UploadModelForm, EditYamlElementForm


# Create your views here.
class ModelList(ListView):
    model = YamlModel
    template_name = 'yaml_app/model_list.html'
    context_object_name = 'YAML_model_list'

class EditYamlElementView(UpdateView):
    model = YamlElement
    form_class = EditYamlElementForm
    template_name = 'yaml_app/element_edit.html'
    success_url = reverse_lazy('model_list')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        root = context["object"].get_root()
        model = YamlModel.objects.get(elements = root)

        context["model"] = model

        return context

def show_model(request, pk):
    model = YamlModel.objects.get(id=pk)
    return render(request,"yaml_app/model_tree.html", {'name': model.model_name, 'tree': model.elements.get_descendants(include_self=True)})

def delete_element(request,pk):
    element = get_object_or_404(YamlElement, pk=pk)
    root = element.get_root()
    model = YamlModel.objects.get(elements = root)

    if request.method == 'POST':
        element_is_root = False

        if root == element:
            element_is_root = True

        element.delete()

        if element_is_root:
            model.delete()
            return redirect('model_list')

        return redirect('model_tree',pk=model.pk)

    return render(request,'yaml_app/element_delete.html', {'model': model, 'element': element})

def upload_model(request):

    if request.method == 'POST':
        form = UploadModelForm(request.POST, request.FILES)

        if form.is_valid():
            f = yaml.load(form.cleaned_data['yaml_file'].read(),Loader=yaml.FullLoader)
            model_name = form.cleaned_data['name']

            yaml_dict = {model_name: f}

            save_model_elements(yaml_dict)

            return redirect('model_list')

    form = UploadModelForm
    return render(request,'yaml_app/upload.html',{"form": form})
