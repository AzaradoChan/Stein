from django import forms as f

class SetorForm(f.Form):
    nome = f.CharField(max_length=50)