from django.forms import ModelForm, Textarea, TextInput

from .models import Article

class ArticleCreateForm(ModelForm):
    class Meta:
        model = Article
        fields = [
            'title',
            'slug',
            'body',
            'tags',
            'thumbnail',
        ]
        widgets = {
            'slug': TextInput(attrs={
                'placeholder': 'Leave blank to generate slug automatically',
            }),
            'body': Textarea(attrs={
                'class': 'body-textarea',
            }),
        }
