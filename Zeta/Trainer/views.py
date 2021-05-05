from django.shortcuts import render,redirect
from Admin.models import Trainer_profile,Trainer_detail,stud_profile,stud_detail
from django.db.models import Q
from django.contrib import messages

# Create your views here.
def index(request):
    return render(request,'TRindex.html')

# views for trainer Model:
def trainerdetails(request):
    Trdetail = Trainer_detail.objects.all()
    contents = {'Trdetail':Trdetail}
    return render(request,'Trdetails.html',contents)

def trainer_data(request, id=None):
    Trdata = Trainer_detail.objects.get(Tr_id=id)
    detail = {'Trdata':Trdata}
    return render(request,'Trdata.html',detail)

def trainer_search(request):
    if request.method == 'POST':
        Trquery = request.POST['trsearch']

        if Trquery:
            match = Trainer_detail.objects.filter(Q(Tr_id__tr_name__icontains = Trquery) | Q(task_assigned__icontains = Trquery) ) 

            if match:
                return render(request,'Trsearch.html',{'Trquery':match})
            else:
                messages.error(request,"No Results Found.")
        else:
            return redirect('/Trainer/Trdetails')

    return render(request,'Trsearch.html')

# Views for student model:
def studentdetails(request):
    studetail = stud_profile.objects.all()
    content = {'studetail':studetail}
    return render(request,'studetails.html',content)

def student_data(request, id=None):
    studata = stud_detail.objects.get(Stud_id=id)
    data = {'studata':studata}
    return render(request,'studata.html',data)

# Searching in student model
def student_search(request):
    if request.method == 'POST':
        studquery = request.POST['studsearch']

        if studquery:
            match = stud_detail.objects.filter(Q(Stud_id__stud_name__icontains = studquery) | Q(Stud_id__stud_college__icontains = studquery) | Q(stud_course__icontains = studquery))

            if match:
                return render(request,'studsearch.html',{'studquery':match})
            else:
                messages.error(request,"No Results Found.")
        else:
            return redirect('/Trainer/studetails')

    return render(request,'studsearch.html')