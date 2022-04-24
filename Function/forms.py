from django.forms import ModelForm
from .models import *
from django import forms


class PictureForm(ModelForm):
    name = forms.CharField(label='',
                           widget=forms.TextInput(attrs={"class": "input-field", "placeholder": "Название фото"}))
    url = forms.CharField(label='',
                          widget=forms.TextInput(
                              attrs={"class": "input-field", "placeholder": "URL"}))
    description = forms.CharField(label='',
                                  widget=forms.TextInput(
                                      attrs={"class": "input-field", "placeholder": "Описание фото"}))

    tags = forms.MultipleChoiceField(label='', widget=forms.SelectMultiple(attrs={"class": "choice-field"}), choices=[
    (item.pk, item) for item in MedlTag.objects.all()])

    class Meta:
        model = MedlPicture
        fields = ['name', 'url', 'description', 'tags', 'author']
        widgets = {'author': forms.HiddenInput}

    picture = forms.BooleanField(widget=forms.HiddenInput, initial=True)

    def __int__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['name'].label = ''


class SearchForm(ModelForm):
    name = forms.CharField(label='', required=False,
                           widget=forms.TextInput(attrs={"class": "input-field", "placeholder": "Название фото"}))

    tags = forms.MultipleChoiceField(label='', widget=forms.SelectMultiple(attrs={"class": "choice-field"}), choices=[
    (item.pk, item) for item in MedlTag.objects.all()], required=False)

    author = forms.CharField(label='', required=False,
                           widget=forms.TextInput(attrs={"class": "input-field", "placeholder": "Автор"}))
    class Meta:
        model = MedlPicture
        fields = ['name', 'tags', 'author']


class TagForm(ModelForm):
    tagname = forms.CharField(label='',
                              widget=forms.TextInput(attrs={"class": "input-field", "placeholder": "Название тэга"}))
    description = forms.CharField(label='',
                                  widget=forms.TextInput(
                                      attrs={"class": "input-field", "placeholder": "Описание тэга"}))

    class Meta:
        model = MedlTag
        fields = ['tagname', 'description', 'author']
        widgets = {'author': forms.HiddenInput}

    tag = forms.BooleanField(widget=forms.HiddenInput, initial=True)
