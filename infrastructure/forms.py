from django import forms

from infrastructure.models import Table


class TableForm(forms.Form):
    # class Meta:
    #     model = Table
    #     fields = ['size', 'time', 'owner_name', 'owner_number']
    size = forms.IntegerField(required=True)
    # time = forms.DateTimeField(required=True)
    owner_name = forms.CharField(max_length=15, required=True)
    owner_number = forms.CharField(max_length=12, required=True)
