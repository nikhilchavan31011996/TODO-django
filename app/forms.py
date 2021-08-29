from django.forms import ModelForm, fields
from app.models import TODO

class TODOform(ModelForm):
    class Meta:
        model = TODO  ##for what we are creating model.that is 'TODO'
        fields = ['title','status','priority']
