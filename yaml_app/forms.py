from django import forms
from django.core.validators import FileExtensionValidator

from yaml_app.models import YamlElement

class UploadModelForm(forms.Form):
    name = forms.CharField(max_length=50)
    yaml_file = forms.FileField(validators=[FileExtensionValidator(allowed_extensions=["yaml"])])

class EditYamlElementForm(forms.ModelForm):
    value = forms.CharField(widget=forms.Textarea)
    #parent = forms.ModelChoiceField(queryset=YamlElement.objects.all())

    class Meta:
        model = YamlElement
        fields = ('value','parent',)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        choices_with_instance = kwargs['instance'].get_root().get_descendants(include_self=True)
        choices_ids = []

        for choice in choices_with_instance:
            if not choice.value:
                choices_ids.append(choice.pk)

        choices = YamlElement.objects.filter(pk__in=choices_ids)

        self.fields["parent"] = forms.ModelChoiceField(queryset=choices,empty_label=None)
