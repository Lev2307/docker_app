from django import forms
from .models import FLname


class FLnameForm(forms.ModelForm):
    class Meta:
        model = FLname
        fields = ['first_name', 'last_name']

    def save(self, commit=True):
        res = super().save(commit=True)
        def check_mr_start(string):
            if not string.startswith('mr.'):
                return True
            return False
        def check_mr_end(string):
            if string.endswith('mr.'):
                return True
            return False
        
        fname = self.cleaned_data.get('first_name')
        fname = fname.lower()
        new_fname = ''
        if check_mr_start(fname) == True:
            new_fname = 'Mr.' + ' ' + fname
        if check_mr_end(fname) == True:
            fname = fname.replace('mr.', '')
            new_fname = 'Mr.' + ' ' + fname
        res.first_name = new_fname
        res.save()
        return res