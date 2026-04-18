from django import forms
from django.core.exceptions import ValidationError
from django.core.validators import MinLengthValidator, MaxLengthValidator
from django.utils.deconstruct import deconstructible


from .models import Category, Husband

@deconstructible
class RussianValidator:
    ALLOWED_CHARS = "АБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЬЪЭЮЯабвгдеёжзийклмнопрстуфхцчшщьъэюя0123456789- "
    code = 'russian'

    def __init__(self, message=None):
        self.message = message if message else "Должны присутствовать только русские символы, дефис и пробел."

    def __call__(self, value, *args, **kwargs):
        if not (set(value) <= set(self.ALLOWED_CHARS)):
            raise ValidationError(self.message)


class AddPostForm(forms.Form):

    title = forms.CharField(label='Заголовок:', max_length=255, min_length=3,
                            widget=forms.TextInput(attrs={'class':'form-input'}),
                            validators=[RussianValidator()],
                            error_messages={
                                'min_length':'Слишком короткий заголовок',
                                'required':'Без заголовка никак'
                            })
    slug = forms.SlugField(label="URL", max_length=255,
                           validators=[
                               MinLengthValidator(5, message='Минимум 5 символов'),
                               MaxLengthValidator(100, message='Максимум 100 символов')
                           ])
    content = forms.CharField(label='Контент', widget=forms.Textarea(attrs={'cols':50,'rows':5}), required=False)
    is_published = forms.BooleanField(required=False, initial=True, label='Статус')
    cat = forms.ModelChoiceField(queryset=Category.objects.all(), empty_label='Категория не выбрана', label='Категории')
    husband = forms.ModelChoiceField(queryset=Husband.objects.all(), required=False, empty_label='Не замужем', label='Муж')
