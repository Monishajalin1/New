from django import forms
from .models import Post



class PostAddForm(forms.ModelForm):
    # inside the PostAddform class, there is an inner class called meta
    #this is a standard django convension to include meta data abput the form
    class Meta:
     #in meta,we specify which model the form is for add the fields.
    #this form is to designed  to interact with the fields of the post model
        model=Post
        # This line lists the fields from the post model that should be included in the
        fields=('post_title','post_description','post_shortname','post_image')


class PostEditForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('post_title','post_description','post_shortname','post_image')


class MyLoginForm(forms.Form):
    username=forms.CharField()
    password=forms.CharField(widget=forms.PasswordInput)
