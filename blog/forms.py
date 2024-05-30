
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm
from django import forms
from django.contrib.auth.models import User

from .models import Post,Category,Comment


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('name','content','price','category','photo','published')
        widgets = {
            'name':forms.TextInput(attrs={
                'class':'form-control',
                'placeholder':"Mahsulot nomi",
                'style':'margin-top: 10px;'
            }),
            'content':forms.Textarea(attrs={
                'class':'form-control',
                'placeholder':"Mahsulot haqida batafsil",
                'style':'margin-top: 10px;'
            }),
            'price':forms.TextInput(attrs={
                'class':'form-control',
                'placeholder':"Mahsulot narxi",
                'style':'margin-top: 10px;'
            }),
            'category':forms.Select(attrs={
                'class':'form-select',
                'style':'margin-top: 10px;'
            }),
            'photo': forms.FileInput(attrs={
                'class': 'form-control',
                'placeholder': 'Rasm',
                'style': 'margin-top: 10px',
                'style':'margin-top: 10px;'
            }),

            'published':forms.CheckboxInput(attrs={
                'class': 'form-check-input',
                'style':'margin-top: 10px;'

            })
        }



class Category_form(forms.ModelForm):
    class Meta:
        model = Category
        fields = ('title',)


class LoginForm(AuthenticationForm):
    username = forms.CharField(max_length=50,widget=forms.TextInput(attrs={
        'class': 'form-control'
    }))
    password = forms.CharField(widget=forms.PasswordInput(attrs={
       'class': 'form-control'
    }))

class RegisterForm(UserCreationForm):
    username = forms.CharField(max_length=50,widget=forms.TextInput(attrs={
        'class': 'form-control'
    }))
    email = forms.CharField(widget=forms.EmailInput(attrs={
        'class': 'form-control'
    }))
    password1 = forms.CharField(widget=forms.PasswordInput(attrs={
        'class': 'form-control',
        'placeholder': 'Parolni kiriting!'
    }))
    password2 = forms.CharField(widget=forms.PasswordInput(attrs={
        'class': 'form-control',
        'placeholder': 'Parolni takrorlang!'
    }))
    class Meta:
        model = User
        fields = ('username','email')

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('text',)

    widgets = {
       'text': forms.Textarea(attrs={
           'class':'form-control'
       })
    }