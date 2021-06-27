from django import forms
from musician_app import models


class MusicianForm ( forms.ModelForm ) :
  class Meta :
    model = models.Musician
    fields = "__all__"
    # exclude = ['first_name'] for remove any fields
    # fields = ('first_name',) to keep fields by chosen
class AlbumForm (forms.ModelForm):
  release_date = forms.DateField(widget=forms.TextInput(attrs={'type': 'date'}))

  class Meta:
    model = models.Album
    fields = "__all__"