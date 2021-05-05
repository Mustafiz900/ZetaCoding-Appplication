from django import forms
from .models import stud_profile,stud_detail

class SaveProfile(forms.ModelForm):
    class Meta:
        model = stud_profile
        fields = ['stud_name','stud_email','stud_college','stud_address','stud_phone']

class SaveDetail(forms.ModelForm):
    class Meta:
        model = stud_detail
        fields = ['stud_course','stud_domain','stud_fees','stud_batch']