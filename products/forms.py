from django import forms
from .models import Review


class ReviewForm(forms.ModelForm):

    class Meta:
        model = Review
        fields = ('title', 'body',)
        widgets = {
            'title': forms.TextInput(attrs={'placeholder': 'Name'}),
            'body': forms.Textarea(
                attrs={'placeholder': 'Enter description here'}),
        }
