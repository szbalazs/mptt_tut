from mptt.forms import (TreeNodeChoiceField, TreeNodeMultipleChoiceField,
                        TreeNodePositionField)
from django import forms

from tutorial.models import Genre

class GenreForm(forms.Form):
    genre_choice = TreeNodeChoiceField(queryset=Genre.objects.all(),level_indicator= '+--')
    genre_m_choice = TreeNodeMultipleChoiceField(queryset=Genre.objects.all(),level_indicator= '--')
