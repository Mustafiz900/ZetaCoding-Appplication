from django.shortcuts import render,redirect
from django.http import JsonResponse
from django.contrib import messages
from django.contrib.auth import authenticate,login,logout
from .models import stud_profile,stud_detail,Trainer_profile,Trainer_detail,Referrer_profile,Referrer_leads
from django.db.models import Q
from Admin.forms import SaveProfile,SaveDetail
from rest_framework.views import APIView
from rest_framework.response import Response

# Create your views here.
def index(request):
    stud = stud_profile.objects.count()
    trnr = Trainer_profile.objects.count()
    refr = Referrer_profile.objects.count()
    content = {'stud':stud,'trnr':trnr,'refr':refr}
    return render(request,'Admin.html',content)
    
# For rendering graphs to Admin.html page
def GraphData(request,id=None):
    data = []
    Student = stud_profile.objects.get(stud_id=id)
    # Think how to get the details

    for i in detail:
        detaildata.append({i.stud_course})
    print(data)
    return JsonResponse(data, safe=False)




# Creating views for student model:-

def student(request):
    # Getting the student profile details
    allprofiles = stud_profile.objects.all()
    contents = {'allprofiles':allprofiles}
    return render(request,'student.html',contents)

def student_details(request, id=None):
    # rendering details corresponding to student ID
    alldetails = stud_detail.objects.get(Stud_id=id)
    detail = {'alldetails':alldetails}
    return render(request,'student_details.html',detail)



def Add_student(request):
    # Handling student details post request
    if request.method=='POST':
        name = request.POST['name']
        email = request.POST['email']
        college = request.POST['college']
        course = request.POST['course']
        domain = request.POST['domain']
        fees = request.POST['fees']
        batch = request.POST['batch']
        phone = request.POST['phone']
        address = request.POST['address']

        
        profile = stud_profile(stud_name=name,stud_email=email,stud_college=college,stud_address=address,stud_phone=phone)
        profile.save()

        details = stud_detail(stud_course=course,stud_domain=domain,stud_fees=fees,stud_batch=batch)
        details.save()

        messages.warning(request,"Data Entered Successfully") # For notification message
        return redirect('Add_student')

    return render(request,'Add_student.html')


# For deleting a student row
def student_delete(request, id=None):
    alldelete = stud_profile.objects.get(stud_id=id)
    alldelete.delete()
    messages.warning(request,"One Item Deleted") # For notification message
    return redirect('/Admin/student')


# For updating a student row
def student_edit(request, id=None):
    if request.method=='POST':
        name = request.POST['name']
        email = request.POST['email']
        college = request.POST['college']
        course = request.POST['course']
        domain = request.POST['domain']
        fees = request.POST['fees']
        batch = request.POST['batch']
        phone = request.POST['phone']
        address = request.POST['address']
        
        profile = stud_profile(stud_id=id,stud_name=name,stud_email=email,stud_college=college,stud_address=address,stud_phone=phone)
        profile.save()

        detail = stud_detail(Stud_id=stud_profile(stud_id=id),stud_course=course,stud_domain=domain,stud_fees=fees,stud_batch=batch)
        detail.save()

        messages.warning(request,"One Item Updated") # For notification message
        return redirect('/Admin/student')

    allprofile = stud_detail.objects.get(Stud_id=id)
    return render(request,'Edit_student.html',{'allprofile':allprofile})


# Searching in student model
def student_search(request):
    if request.method == 'POST':
        query = request.POST['search']

        if query:
            match = stud_detail.objects.filter(Q(Stud_id__stud_name__icontains = query) | Q(Stud_id__stud_college__icontains = query) | Q(stud_course__icontains = query))

            if match:
                return render(request,'student_search.html',{'query':match})
            else:
                messages.error(request,"No Results Found.")
        else:
            return redirect('/Admin/student')

    return render(request,'student_search.html')






#Creating Views for Trainer Model
def trainer(request):
    # Getting the Trainer details
    # Trprofiles = Trainer_profile.objects.all()
    Trdetail = Trainer_detail.objects.all()
    contents = {'Trdetail':Trdetail}
    return render(request,'trainer.html',contents)

def trainer_details(request, id=None):
    # rendering details corresponding to Trainer ID
    Trdetails = Trainer_detail.objects.get(Tr_id=id)
    detail = {'Trdetails':Trdetails}
    return render(request,'trainer_details.html',detail)


def Add_trainer(request):
    # Handling Trainer details post request
    if request.method=='POST':
        name = request.POST['name']
        email = request.POST['email']
        address = request.POST['address']
        phone = request.POST['phone']
        task_assgn = request.POST['task_assgn']
        task_cmpltd = request.POST['task_compltd']
        task_assgn_date = request.POST['task_assgn_date']
        task_cmpltd_date = request.POST['task_compltd_date']
        batch = request.POST['batch']

        
        Tr_profile = Trainer_profile(tr_name=name,tr_email=email,tr_phone=phone,tr_address=address)
        Tr_profile.save()

        Tr_details = Trainer_detail(task_assigned=task_assgn,task_completed=task_cmpltd,task_assgn_date=task_assgn_date,task_complete_date=task_cmpltd_date,tr_batch=batch)
        Tr_details.save()

        messages.warning(request,"Data Entered Successfully") # For notification message
        return redirect('Add_trainer')

    return render(request,'Add_trainer.html')

#For deleting a trainer row
def trainer_delete(request, id=None):
    alldelete = Trainer_profile.objects.get(tr_id=id)
    alldelete.delete()
    messages.warning(request,"One Item Deleted") # For notification message
    return redirect('/Admin/trainer')


# For updating a Trainers row
def trainer_edit(request, id=None):
    if request.method=='POST':
        name = request.POST['name']
        email = request.POST['email']
        address = request.POST['address']
        phone = request.POST['phone']
        task_assgn = request.POST['task_assgn']
        task_cmpltd = request.POST['task_compltd']
        task_assgn_date = request.POST['task_assgn_date']
        task_cmpltd_date = request.POST['task_compltd_date']
        batch = request.POST['batch']
        
        Tr_profile = Trainer_profile(tr_id=id,tr_name=name,tr_email=email,tr_phone=phone,tr_address=address)
        Tr_profile.save()

        Tr_details = Trainer_detail(Tr_id=Trainer_profile(tr_id=id),task_assigned=task_assgn,task_completed=task_cmpltd,task_assgn_date=task_assgn_date,task_complete_date=task_cmpltd_date,tr_batch=batch)
        Tr_details.save()

        messages.warning(request,"One Item Updated") # For notification message
        return redirect('/Admin/trainer')

    Trprofile = Trainer_detail.objects.get(Tr_id=id)
    return render(request,'Edit_trainer.html',{'Trprofile':Trprofile})

# Searching in Trainer model
def trainer_search(request):
    if request.method == 'POST':
        Trquery = request.POST['Trsearch']

        if Trquery:
            match = Trainer_detail.objects.filter(Q(Tr_id__tr_name__icontains = Trquery) | Q(task_assigned__icontains = Trquery) ) 

            if match:
                return render(request,'trainer_search.html',{'Trquery':match})
            else:
                messages.error(request,"No Results Found.")
        else:
            return redirect('/Admin/trainer')

    return render(request,'trainer_search.html')





#Creating Views for Referrer Model
def referrer(request):
    # Getting the Referrer details
    Rfprofiles = Referrer_leads.objects.all()
    contents = {'Rfprofiles':Rfprofiles}
    return render(request,'referrer.html',contents)

def referrer_details(request, id=None):
    # rendering details corresponding to Referrer ID
    Rfdetails = Referrer_profile.objects.get(Rf_id=id)
    detail = {'Rfdetails':Rfdetails}
    return render(request,'referrer_details.html',detail)

def Add_referrer(request):
    # Handling Referrer details post request
    if request.method=='POST':
        Rfname = request.POST['Rfname']
        Rfemail = request.POST['Rfemail']
        Rfaddress = request.POST['Rfaddress']
        Rfphone = request.POST['Rfphone']
        Rf_stud_name = request.POST['Rf_stud_name']
        Rf_stud_clg = request.POST['Rf_stud_clg']
        Rf_stud_phone = request.POST['Rf_stud_phone']

        
        Rf_profile = Referrer_profile(Rf_name=Rfname,Rf_email=Rfemail,Rf_address=Rfaddress,Rf_phone=Rfphone)
        Rf_profile.save()

        Rf_details = Referrer_leads(Rf_stud_name=Rf_stud_name,Rf_stud_college=Rf_stud_clg,Rf_stud_phone=Rf_stud_phone)
        Rf_details.save()

        messages.warning(request,"Data Entered Successfully") # For notification message
        return redirect('Add_referrer')

    return render(request,'Add_referrer.html')


#For deleting a referrer row
def referrer_delete(request, id=None):
    Rfdelete = Referrer_profile.objects.get(Rf_id=id)
    Rfdelete.delete()
    messages.warning(request,"One Item Deleted") # For notification message
    return redirect('/Admin/referrer')


#For updating a referrer row
def referrer_edit(request, id=None):
    # Handling Referrer Update post request
    if request.method=='POST':
        Rfname = request.POST['Rfname']
        Rfemail = request.POST['Rfemail']
        Rfaddress = request.POST['Rfaddress']
        Rfphone = request.POST['Rfphone']
        Rf_stud_name = request.POST['Rf_stud_name']
        Rf_stud_clg = request.POST['Rf_stud_clg']
        Rf_stud_phone = request.POST['Rf_stud_phone']

        
        Rf_profile = Referrer_profile(Rf_id=id,Rf_name=Rfname,Rf_email=Rfemail,Rf_address=Rfaddress,Rf_phone=Rfphone)
        Rf_profile.save()

        Rf_details = Referrer_leads(RF_id=Referrer_profile(Rf_id=id),Rf_stud_name=Rf_stud_name,Rf_stud_college=Rf_stud_clg,Rf_stud_phone=Rf_stud_phone)
        Rf_details.save()

        messages.warning(request,"One Item Updated.") # For notification message
        return redirect('/Admin/referrer')

    Rfprofile = Referrer_leads.objects.get(RF_id=id)
    return render(request,'Edit_referrer.html',{'Rfprofile':Rfprofile})


# Searching in Referrer model
def referrer_search(request):
    if request.method == 'POST':
        Rfquery = request.POST['Rfsearch']

        if Rfquery:
            match = Referrer_leads.objects.filter(Q(RF_id__Rf_name__icontains = Rfquery) | Q(Rf_stud_name__icontains = Rfquery) | Q(Rf_stud_college__icontains = Rfquery) ) 

            if match:
                return render(request,'referrer_search.html',{'Rfquery':match})
            else:
                messages.error(request,"No Results Found.")
        else:
            return redirect('/Admin/referrer')

    return render(request,'referrer_search.html')