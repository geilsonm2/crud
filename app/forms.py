from django.forms import ModelForm
from app.models import Cursos

# Create the form class.
class CursosForm(ModelForm):
    class Meta:
        model = Cursos
        fields = ['curso', 'tempoD']

#class ArticleForm(ModelForm):
  #  class Meta:
   #     model = Article
     #   fields = ['email', 'senha']