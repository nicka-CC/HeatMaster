from django import forms
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth.models import User

from .models import CalculatePrice, Thermostats, Produce


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
        ('yes', 'Установка'),
        ('no', 'Нет'),

    ]

    install = forms.ChoiceField(
        choices=TYPE_INSTALL,
        widget=forms.Select(attrs={'class': 'form-control'})
    )
    STAGE_CHOICES = [(str(i), str(i)) for i in range(1, 11)]
    stage = forms.ChoiceField(
        choices=STAGE_CHOICES,
        widget=forms.RadioSelect(attrs={'class': 'form-check-input'})
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