from django.db import models

# Create your models here.
# Here "stud" stands for student

class stud_profile(models.Model):                     # For student personal details
    stud_id = models.AutoField(primary_key=True)
    stud_name = models.CharField(max_length=50)
    stud_email = models.CharField(max_length=50)
    stud_college = models.CharField(max_length=50)
    stud_address = models.CharField(max_length=100)
    stud_phone = models.IntegerField()

    def __str__(self):
        return self.stud_name

class stud_detail(models.Model):                      # For student Course details
    Stud_id = models.ForeignKey(stud_profile, on_delete=models.CASCADE, primary_key=True, default=None)
    stud_course = models.CharField(max_length=80)
    stud_domain = models.CharField(max_length=80)
    stud_fees = models.IntegerField()
    stud_batch = models.IntegerField()

    # def __str__(self):
    #     return self.stud_id
    





# Here "tr" stands for Trainer
class Trainer_profile(models.Model):                     # For Trainer personal details
    tr_id = models.AutoField(primary_key=True,default=None)
    tr_name = models.CharField(max_length=50)
    tr_email = models.CharField(max_length=50)
    tr_address = models.CharField(max_length=100)
    tr_phone = models.IntegerField()

    def __str__(self):
        return self.tr_name

class Trainer_detail(models.Model):                      # For Trainer work details
    Tr_id = models.ForeignKey(Trainer_profile,on_delete=models.CASCADE,primary_key=True,default=1)
    task_assigned = models.CharField(max_length=80)
    task_completed = models.CharField(max_length=80)
    task_assgn_date = models.DateTimeField(blank=True)
    task_complete_date = models.DateTimeField(blank=True)
    tr_batch = models.IntegerField()

    # def __str__(self):
    #     return self.Tr_id






# Here Rf stands for Referrer
class Referrer_profile(models.Model):                     # For Referrer personal details
    Rf_id = models.AutoField(primary_key=True,default=None)
    Rf_name = models.CharField(max_length=50)
    Rf_email = models.CharField(max_length=50)
    Rf_address = models.CharField(max_length=100)
    Rf_phone = models.IntegerField()

    def __str__(self):
        return self.Rf_name

class Referrer_leads(models.Model):                      # For Referrer Leads details
    RF_id = models.ForeignKey(Referrer_profile,on_delete=models.CASCADE,primary_key=True,default=None)
    Rf_stud_name = models.CharField(max_length=80)
    Rf_stud_college = models.CharField(max_length=80)
    Rf_stud_phone = models.IntegerField()

    # def __str__(self):
    #     return self.Tr_id
