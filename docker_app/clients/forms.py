from django import forms
from .models import FLname

class FLnameForm(forms.ModelForm):
    class Meta:
        model = FLname
        fields = ['first_name', 'last_name']

    def save(self, commit=False):
        form = super(FLnameForm, self).save(commit=False)
        print(form)
        # fname = self.cleaned_data.get('first_name')
        # if not 'Mr' in fname:
        #     fname = 'Mr ' + fname
        return form