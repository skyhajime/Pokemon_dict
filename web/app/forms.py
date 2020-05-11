from django import forms
from .models import Item


class ItemForm(forms.ModelForm):
    class Meta:
        model = Item
        fields = ('name','no','type1','type2','ability1','ability2','hidden_ability','h','a','b','c','d','s', 'memo')
        widgets = {
                    'name': forms.TextInput(attrs={'placeholder':'例：フシギダネ'}),
                    'no': forms.NumberInput(attrs={'min':1}),
                    'type1': forms.TextInput(),
                    'type2': forms.TextInput(),
                    'ability1': forms.TextInput(),
                    'ability2': forms.TextInput(),
                    'hidden_ability': forms.TextInput(),
                    'h': forms.NumberInput(attrs={'min':1}),
                    'a': forms.NumberInput(attrs={'min':1}),
                    'b': forms.NumberInput(attrs={'min':1}),
                    'c': forms.NumberInput(attrs={'min':1}),
                    'd': forms.NumberInput(attrs={'min':1}),
                    's': forms.NumberInput(attrs={'min':1}),
                    'memo': forms.Textarea(attrs={'rows':4}),
                  }

