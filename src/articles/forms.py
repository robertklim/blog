from django.forms import ModelForm, TextInput

from .models import Article

class ArticleCreateForm(ModelForm):
    class Meta:
        model = Article
        fields = [
            'title',
            'slug',
            'body',
            'thumbnail',
        ]
        widgets = {
            'slug': TextInput(attrs={
                'placeholder': 'Leave blank to generate slug automatically',
            }),
        }
