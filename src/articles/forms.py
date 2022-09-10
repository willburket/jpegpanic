from tkinter import Widget
from xml.etree.ElementInclude import include
from django import forms

from .models import Comment


class CommentForm(forms.ModelForm):

    class Meta:
        model = Comment
        fields = [
            'comment',
        ]
        widgets = {
            'comment':forms.Textarea(
                attrs={
                    'placeholder':'Add a comment...',
                    'rows': 1,
                    'cols': 120,
                }
            )
        }


  