from django import forms


class ArticleCommentForm(forms.Form):
    name = forms.CharField(max_length="60", required=True)
    comment_msg = forms.CharField(widget=forms.TextInput())
