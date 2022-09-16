from django import forms
from .models import Firstlastname
from .tasks import mr_save_task


class FirstlastnameForm(forms.ModelForm):
    class Meta:
        model = Firstlastname
        fields = ['first_name', 'last_name']

    def mr_save(self):
        return mr_save_task.delay(self.cleaned_data['first_name'])

    def save(self, commit=True):
        res = super().save(commit=True)
        new_fname = self.mr_save()
        print(new_fname)
        res.first_name = new_fname
        res.save()
        return res