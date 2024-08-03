from django.contrib import admin
from testapp.models import MovieModel
# Register your models here.
class MovieAdmin(admin.ModelAdmin):
    list_display = ['moviename','releasedate','heroname','heroinename','rating']

admin.site.register(MovieModel,MovieAdmin)
