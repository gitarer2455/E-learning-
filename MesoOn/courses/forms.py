from django import forms
from django.contrib.auth.models import User
from .models import Klasa, Lendet, Lesson



class KlasaForm(forms.ModelForm):
    class Meta:
        model = Klasa
        fields = '__all__'
        help_texts = {
            'title': 'Eg. Class 11 or Computer Class',
            'description': 'Enter a short description of the class',
            'image': 'You can put a picture of the class or you can leave it blank'
        }

class LendaForm(forms.ModelForm):
    class Meta:
        model = Lendet
        fields = ['krijues','slug', 'Title', 'klasa', 'pershkrimi', 'images']
        help_texts = {
            'Title': 'lesson 1',
            'pershkrimi':'Enter a short description of the subject',
            'klasa':'Create simlplified step',
            'images':'You can put a picture of the item or you can leave it blank'
        }
        labels = {
            'Title':'Title create'
        }
        widgets = {'krijues': forms.HiddenInput(), 'slug': forms.HiddenInput()}


class MesimiForm(forms.ModelForm):
    class Meta:
        model = Lesson 
        fields = ['slug','Title', 'lenda', 'video_id', 'pozicioni', ]
        help_texts = {
            'Title':'የcource ርዕስ አስገባ',
            'lenda':'ይህ ትምህርት የሚገኝበትን ርዕሰ ጉዳይ ይምረጡ',
            'video_id':'Place your ID and upload videos to Youtube (<a href="/media/youtube_help.png">link</a>)',
            'pozicioni':'የቦታ ቁጥሩን ወይም የማስተማሪያውን ቅደም ተከተል ያስገቡ '
        }
        widgets = {
            'slug': forms.HiddenInput()
        }