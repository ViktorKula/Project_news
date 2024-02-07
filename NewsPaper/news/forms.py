from django import forms
from django.core.exceptions import ValidationError

from .models import Post



class PostForm(forms.ModelForm):
    post_text = forms.CharField(min_length=5)


    class Meta:
        model = Post
        fields = [
            'post_author',
            'post_title',
            'post_category',
            'post_text'

        ]

    def clean(self):
        cleaned_data = super().clean()
        head_name = cleaned_data.get("post_title")
        article_text = cleaned_data.get("post_text")

        if head_name == article_text:
            raise ValidationError(
                "Название не должно быть идентично посту."
            )

        return cleaned_data

