from django import forms
from django.forms import RadioSelect

from .models import Review


class ReviewForm(forms.ModelForm):

    class Meta:
        model = Review
        fields = ('name', 'rating', 'review')
        widgets = {
            'name': forms.TextInput(
                attrs={
                    'type': 'text',
                    'class': 'form-control',
                    'id': 'name',
                    'aria-describedby': 'nameHelp',
                    'placeholder': 'Представтесь',
                    'name': 'name',
                    'data-cip-id': 'name'
                }
            ),
            'rating': RadioSelect(
                choices=[
                    (1, '1'), (2, '2'), (3, '3'), (4, '4'), (5, '5')
                ]
            ),
            'review': forms.Textarea(
                attrs={
                    'class': 'form-control',
                    'id': 'content',
                    'placeholder': 'Содержание',
                    'name': 'description'
                }
            ),

        }

