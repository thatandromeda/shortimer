from django import forms
from django.contrib.auth.models import User

from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit


class ProfileUpdateForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(ProfileUpdateForm, self).__init__(*args, **kwargs)
        self.fields['home_url'] = forms.URLField(required=False)
        self.helper = FormHelper(self)
        self.helper.add_input(Submit('save', 'Save'))

    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email')
