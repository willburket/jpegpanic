from tkinter import Widget
from django import forms

from .models import Comment


class CommentForm(forms.ModelForm):

    class Meta:
        model = Comment
        exclude = [
            'user',
           'likes',
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


        



        
        
        