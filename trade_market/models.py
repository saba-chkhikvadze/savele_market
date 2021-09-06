from django.db import models
from django.contrib.auth.models import User
from django.db.models.deletion import CASCADE
from django.db.models.expressions import Case
from django.db.models.fields import CharField, EmailField, IntegerField
from django.db.models.fields.related import OneToOneField
from django.db.models.signals import post_save

locations = [('ბეშუმი', 'ბეშუმი'), ('უფლისციხე',
                                    'უფლისციხე'), ('ფარი', 'ფარი'), ('არჩევითი', 'არჩევითი')]
thread = [('1', '1'), ('2', '2'), ('3', '3')]
statuses = [('აქტიური', 'აქტიური'), ('დასრულებული', 'დასრულებული')]
uni_choices = [('ფრიუნი', 'ფრიუნი'), ('აგრუნი', 'აგრუნი')]


class Post(models.Model):
    author = models.ForeignKey(User, on_delete=CASCADE, null=True)
    have = CharField(max_length=50, choices=locations, null=True)
    nakad_has = CharField(max_length=50, choices=thread, null=True)
    wants = CharField(max_length=50, choices=locations, null=True)
    nakad_wants = CharField(max_length=50, choices=thread, null=True)
    price = IntegerField(default=0)
    status = CharField(max_length=50, choices=statuses, default='აქტიური')


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=CASCADE)
    name = CharField(max_length=50, null=True)
    last_name = CharField(max_length=50, null=True)
    email = EmailField(null=True)
    uni = CharField(max_length=50, choices=uni_choices)

    def profile_setup(self):
        return (self.name != None and self.last_name != None and self.email != None and self.user != None)

    def __str__(self):
        return f'{self.user.username} - {self.id}'


def create_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)


post_save.connect(create_profile, User)


class Offer(models.Model):
    post = models.ForeignKey(Post, on_delete=CASCADE)
    locations = [('ბეშუმი', 'ბეშუმი'), ('უფლისციხე',
                                        'უფლისციხე'), ('ფარი', 'ფარი'), ('არჩევითი', 'არჩევითი')]
    thread = [('1', '1'), ('2', '2'), ('3', '3')]
    author = models.ForeignKey(User, on_delete=CASCADE)
    offered_loc = CharField(max_length=50, choices=locations)
    offered_nakad = CharField(max_length=50, choices=thread)

    def __str__(self):
        return f'{self.author.username}, {self.id}'
