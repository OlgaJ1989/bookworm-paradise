from django import forms
from .models import Review


class ReviewForm(forms.ModelForm):

    class Meta:
        model = Review
        fields = ('title', 'body',)
        widgets = {
            'title': forms.TextInput(
                attrs={'placeholder': 'Give your review a title'}),
            'body': forms.Textarea(
                attrs={'placeholder': 'Leave your review here'}),
        }
