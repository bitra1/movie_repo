from django import forms
from testapp.models import MovieModel
class MovieForm(forms.ModelForm):
    moviename = forms.CharField()
    releasedate = forms.DateField(label='Release Date(year-month-day)')
    heroname = forms.CharField()
    heroinename = forms.CharField()
    rating = forms.IntegerField()
    class Meta:
        model =MovieModel
        fields = '__all__'
