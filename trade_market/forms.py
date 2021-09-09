from django import forms
from django.db.models import fields
from django.db.models.base import Model
from . models import Offer, Post, Profile
from django.forms import ModelForm, widgets


class CreatePostForm(ModelForm):
    class Meta:
        model = Post
        fields = ['have', 'nakad_has', 'wants', 'nakad_wants', 'price']
        labels = {'have': 'მაქვს (ლოკაცია)', 'nakad_has': 'მაქვს(ნაკადი)',
                  'wants': 'მსურს(ლოკაცია)', 'nakad_wants': 'მსურს(ნაკადი)', 'price': 'ფასი'}
        widgets = {
            'have': forms.Select(attrs={'class': 'form-control', 'placeholder': 'მაქვს'}),
            'nakad_has': forms.Select(attrs={'class': 'form-control', 'placeholder': 'მაქვს (ნაკადი)'}),
            'wants': forms.Select(attrs={'class': 'form-control', 'placeholder': 'ვეძებ'}),
            'nakad_wants': forms.Select(attrs={'class': 'form-control', 'placeholder': 'ვეძებ (ნაკადს)'}),
            'price': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'ფასი'}),
        }


class EditPostForm(ModelForm):
    class Meta:
        model = Post
        fields = ['have', 'nakad_has', 'wants',
                  'nakad_wants', 'status', 'price']
        labels = {'have': 'მაქვს (ლოკაცია)', 'nakad_has': 'მაქვს(ნაკადი)',
                  'wants': 'მსურს(ლოკაცია)', 'nakad_wants': 'მსურს(ნაკადი)', 'status': 'სტატუსი', 'price': 'ფასი'}
        widgets = {
            'have': forms.Select(attrs=({'class': 'form-control'})),
            'nakad_has': forms.Select(attrs=({'class': 'form-control'})),
            'wants': forms.Select(attrs=({'class': 'form-control'})),
            'nakad_wants': forms.Select(attrs=({'class': 'form-control'})),
            'status': forms.Select(attrs=({'class': 'form-control'})),
            'price': forms.TextInput(attrs=({'class': 'form-control'})),

        }


class MakeOfferForm(ModelForm):
    class Meta:
        model = Offer
        fields = ['offered_loc', 'offered_nakad']
        widgets = {
            'offered_loc': forms.Select(attrs=({'class': 'form-control'})),
            'offered_nakad': forms.Select(attrs=({'class': 'form-control'}))
        }


nakad_choices = locations = [('ბეშუმი', 'ბეშუმი'), ('უფლისციხე',
                                                    'უფლისციხე'), ('ფარი', 'ფარი'), ('არჩევითი', 'არჩევითი')]


class SetupProfileForm(ModelForm):
    class Meta:
        model = Profile
        fields = ['name', 'last_name', 'email',  'uni']
        widgets = {
            'name': forms.TextInput(attrs=({'class': 'form-control'})),
            'last_name': forms.TextInput(attrs=({'class': 'form-control'})),
            'email': forms.TextInput(attrs=({'class': 'form-control'})),
            'uni': forms.TextInput(attrs=({'class': 'form-control'}))
        }
