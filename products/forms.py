from django import forms
from django.contrib.auth.models import User
class DocumentForm(forms.Form):
    docfile = forms.FileField(
        label='Select image',
    )
    title = forms.CharField(
        label='title',
    )
    description = forms.CharField(
        label='description',
    )
    active = forms.BooleanField(
        label='active',
    )
    quantity = forms.IntegerField(
        label='quantity',
    )
    zip_Code = forms.CharField(
        label='zip_Code',
    )
    address = forms.CharField(
        label='address',
    )
    date_created = forms.DateTimeField(
        label='date_created',
    )
    date_Update = forms.DateTimeField(
        label='date_Update',
    )
    expire_date = forms.DateTimeField(
        label='expire_date',
    )
