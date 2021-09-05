from django import forms
from django.db.models import fields
from . models import Offer, Post
from django.forms import ModelForm


class CreatePostForm(ModelForm):
    class Meta:
        model = Post
        fields = ['have', 'nakad_has', 'wants', 'nakad_wants', 'price']
        labels = {'have': 'მაქვს (ლოკაცია)', 'nakad_has': 'მაქვს(ნაკადი)',
                  'wants': 'მსურს(ლოკაცია)', 'nakad_wants': 'მსურს(ნაკადი)', 'price': 'ფასი'}


class EditPostForm(ModelForm):
    class Meta:
        model = Post
        fields = ['have', 'nakad_has', 'wants',
                  'nakad_wants', 'status', 'price']
        labels = {'have': 'მაქვს (ლოკაცია)', 'nakad_has': 'მაქვს(ნაკადი)',
                  'wants': 'მსურს(ლოკაცია)', 'nakad_wants': 'მსურს(ნაკადი)', 'status': 'სტატუსი', 'price': 'ფასი'}


class MakeOfferForm(ModelForm):
    class Meta:
        model = Offer
        fields = ['offered_loc', 'offered_nakad']


nakad_choices = locations = [('ბეშუმი', 'ბეშუმი'), ('უფლისციხე',
                                                    'უფლისციხე'), ('ფარი', 'ფარი'), ('არჩევითი', 'არჩევითი')]
