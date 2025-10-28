from django import forms
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth.models import User
from django.utils import timezone

from .models import CalculatePrice, Thermostats, Produce, CommentBlog, Blog, ImageBlog


class CalculatePriceForm(forms.ModelForm):
    TYPE_CHOICES = [
        ('hardwood', 'Деревянный'),
        ('laminate', 'Ламинат'),
        ('tile', 'Плитка'),
        ('vinyl', 'Виниловый'),
        ('carpet', 'Ковровое покрытие'),
        ('cork', 'Пробка'),
        ('concrete', 'Бетон'),
        ('bamboo', 'Бамбук'),
        ('linoleum', 'Линолеум'),
        ('marble', 'Мрамор'),
        ('slate', 'Сланец'),
        ('granite', 'Гранит'),
        ('terrazzo', 'Терраццо'),
        ('rubber', 'Резиновый'),
        ('epoxy', 'Эпоксидный'),
        ('parquet', 'Паркет'),
        ('ceramic', 'Керамический'),
        ('wooden_planks', 'Деревянные доски'),
        ('rubber_tiles', 'Резиновые плитки'),
    ]

    type = forms.ChoiceField(
        choices=TYPE_CHOICES,
        widget=forms.Select(attrs={'class': 'form-control'})
    )
    TYPE_INSTALL = [
        ('yes', 'Да'),
        ('no', 'Нет'),

    ]

    install = forms.ChoiceField(
        choices=TYPE_INSTALL,
        widget=forms.RadioSelect(attrs={'class': 'form-install'}),
    )
    STAGE_CHOICES = [(str(i), str(i)) for i in range(1, 11)]
    stage = forms.ChoiceField(
        choices=STAGE_CHOICES,
        widget=forms.Select(attrs={'class': 'form-control'})
    )
    type_across = forms.ModelChoiceField(
        queryset=Thermostats.objects.all(),
        empty_label="Выберите тип терморегулятора",
        widget=forms.Select(attrs={'class': 'form-control'})
    )
    produce = forms.ModelChoiceField(
        queryset=Produce.objects.all(),
        empty_label="Производитель?",
        widget=forms.Select(attrs={'class': 'form-control'})
    )
    class Meta:
        model = CalculatePrice
        fields = ['subject', 'stage', 'type', 'produce', 'type_across', 'install', 'name', 'phone']
        widgets = {
            'subject': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Площадь обогреваемой поверхности (м2):'}),
            # 'procedure': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Введите процедуру'}),
            # 'stage': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Введите этап'}),
            # 'type': forms.Select(attrs={'class': 'form-control', 'placeholder': 'Введите тип'}),
            # 'produce': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Введите производство'}),
            'type_across': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Введите тип пересечения'}),
            # 'install': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Введите установку'}),
            'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Имя'}),
            'phone': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Телефон'}),
        }
class CustomUserCreationForm(UserCreationForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['username'].widget = forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Логин'})
        self.fields['password1'].widget = forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Пароль'})
        self.fields['password2'].widget = forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Подтверждение пароля'})
        self.fields['email'].widget = forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Email'})
        self.fields['first_name'].widget = forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Фамилия'})
        self.fields['last_name'].widget = forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Имя'})

        for field in self.fields:
         if self[field].errors:
            self.fields[field].widget.attrs['class'] += ' is-invalid'

    class Meta:
        model = User  # Встроенная модель Django
        fields = ['username', 'email', 'first_name', 'last_name', 'password1', 'password2']

    def clean_password2(self):
        """Проверяет, что пароли совпадают."""
        password1 = self.cleaned_data.get("password1")
        password2 = self.cleaned_data.get("password2")

        if password1 and password2 and password1 != password2:
            raise forms.ValidationError("Пароли не совпадают! Повторите ввод.")

        return password2


class CustomAuthenticationForm(AuthenticationForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['username'].widget = forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Логин'})
        self.fields['password'].widget = forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Пароль'})
        for field in self.fields:
         if self[field].errors:
            self.fields[field].widget.attrs['class'] += ' is-invalid'

class CommentBlogForm(forms.ModelForm):
    class Meta:
        model = CommentBlog
        fields = ['text', 'rating']
        widgets = {
            'text': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Введите текст комментария'}),
            'rating': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Оценка'}),
        }

    def __init__(self, *args, user=None, blog=None, **kwargs):
        super().__init__(*args, **kwargs)
        self.user = user
        self.blog = blog

    def save(self, commit=True):
        instance = super().save(commit=False)

        # Привязываем пользователя
        if self.user and self.user.is_authenticated:
            instance.author = f"{self.user.first_name} {self.user.last_name}".strip()
            instance.username = self.user.username

        # Привязываем блог
        if self.blog:
            instance.blog = self.blog
        else:
            raise ValueError("Ошибка: блог не передан в форму!")

        instance.date = timezone.now()

        if commit:
            instance.save()
        return instance

class BlogForm(forms.ModelForm):
    class Meta:
        model = Blog
        fields = ['article', 'text', 'text_two', 'start', 'final']
        labels = {
            'article': 'Название статьи',
            'text': 'Первый абзац',
            'text_two': 'Второй абзац',
            'start': 'Начало статьи',
            'final': 'Конец статьи'
        }
        widgets = {
            'article': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Введите название статьи'}),
            'text': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Введите первый абзац'}),
            'text_two': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Введите второй абзац'}),
            'start': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Введите начало статьи'}),
            'final': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Введите конец статьи'}),
        }


class ImageBlogForm(forms.Form):
    image_1 = forms.ImageField(
        required=False,
        label='Изображение для статьи',
        widget=forms.ClearableFileInput(attrs={
            'accept': 'image/*',
            'class': 'image-input',
            'placeholder': 'Выберите изображение'
        })
    )


class ApplicationForm(forms.ModelForm):
    class Meta:
        model = __import__('{}.models'.format(__name__.split('.')[0]), fromlist=['Applications']).Applications
        fields = ['description', 'part', 'phone']
        widgets = {
            'description': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Короткое описание заявки'}),
            'part': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Название/часть'}),
            'phone': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Телефон'}),
        }

class ThermostatCommentForm(forms.ModelForm):
    class Meta:
        model = __import__('{}.models'.format(__name__.split('.')[0]), fromlist=['ThermostatComment']).ThermostatComment
        fields = ['text', 'rating']
        widgets = {
            'text': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Ваш комментарий'}),
            'rating': forms.NumberInput(attrs={'class': 'form-control', 'min': 1, 'max': 5}),
        }