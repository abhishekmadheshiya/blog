from django import forms
from .models import Comment


class CommentForm(forms.ModelForm):
    content = forms.CharField(widget=forms.Textarea(attrs={'rows': 3}), label='Add a comment')

    class Meta:
        model = Comment
        fields = ['content']
