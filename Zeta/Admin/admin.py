from django.contrib import admin
from .models import stud_profile,stud_detail,Trainer_profile,Trainer_detail,Referrer_profile,Referrer_leads

# Register your models here.
admin.site.register(stud_profile)
admin.site.register(stud_detail) 
admin.site.register(Trainer_profile) 
admin.site.register(Trainer_detail) 
admin.site.register(Referrer_profile) 
admin.site.register(Referrer_leads) 