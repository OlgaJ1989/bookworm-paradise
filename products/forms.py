from django import forms
from .models import Review, Book, Genre


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


class BookForm(forms.ModelForm):

    class Meta:
        model = Book
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        genres = Genre.objects.all()
        friendly_names = [(g.id, g.get_friendly_name()) for g in genres]

        self.fields['genre'].choices = friendly_names
        self.fields['genre'].widget.attrs['class'] = 'add-form-input'
        self.fields['price'].widget.attrs['class'] = 'add-form-input'
        self.fields['rating'].widget.attrs['class'] = 'add-form-input'
        self.fields['image_url'].widget.attrs['class'] = 'add-form-input'
        
