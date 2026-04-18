from django import forms
from .models import Category, Husband


class AddPostForm(forms.Form):

    title = forms.CharField(label='Заголовок:', max_length=255, widget=forms.TextInput(attrs={'class':'form-input'}))
    slug = forms.SlugField(label="URL", max_length=255)
    content = forms.CharField(label='Контент', widget=forms.Textarea(attrs={'cols':50,'rows':5}), required=False)
    is_published = forms.BooleanField(required=False, initial=True, label='Статус')
    cat = forms.ModelChoiceField(queryset=Category.objects.all(), empty_label='Категория не выбрана', label='Категории')
    husband = forms.ModelChoiceField(queryset=Husband.objects.all(), required=False, empty_label='Не замужем', label='Муж')
